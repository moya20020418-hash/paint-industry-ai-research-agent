"""
web_collector.py
config/sources.json に定義された URL からテキストを収集し、
inputs/web_collected_{YYYYMMDD}.md に保存する。

使い方:
    python src/main.py --collect-web
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"ライブラリが見つかりません: {e}")
    print("pip install requests beautifulsoup4 を実行してください。")
    sys.exit(1)

_PROJECT_ROOT = Path(__file__).parent.parent
_SOURCES_PATH = _PROJECT_ROOT / "config" / "sources.json"
_INPUTS_DIR = _PROJECT_ROOT / "inputs"

_REMOVE_TAGS = [
    "script", "style", "nav", "footer", "header",
    "aside", "noscript", "meta", "link",
]


def load_sources() -> dict:
    with open(_SOURCES_PATH, encoding="utf-8") as f:
        return json.load(f)


def _check_robots(url: str, user_agent: str, timeout: int) -> bool:
    """robots.txt を確認してアクセス可否を返す。取得失敗時は True（許可）とする。"""
    try:
        parsed = __import__("urllib.parse", fromlist=["urlparse"]).urlparse(url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp.can_fetch(user_agent, url)
    except Exception:
        return True


def _get_title(soup: "BeautifulSoup") -> str:
    tag = soup.find("title")
    if tag and tag.get_text(strip=True):
        return tag.get_text(strip=True)[:200]
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)[:200]
    return "(タイトルなし)"


def _extract_text(html: str, max_chars: int) -> str:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup.find_all(_REMOVE_TAGS):
        tag.decompose()
    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned[:max_chars]


def fetch_page(source: dict, settings: dict) -> dict:
    """1件の URL を取得して結果 dict を返す。例外は catch して error フィールドに格納。"""
    url = source["url"]
    user_agent = settings.get("user_agent", "auto-research-agent/0.1")
    timeout = settings.get("request_timeout_sec", 10)
    max_chars = settings.get("max_text_chars", 5000)
    result = {
        "id": source["id"],
        "name": source["name"],
        "url": url,
        "source_type": source.get("source_type", ""),
        "priority": source.get("priority", ""),
        "title": "",
        "status_code": None,
        "fetched_at": datetime.now().isoformat(timespec="seconds"),
        "extracted_text": "",
        "error": "",
    }
    try:
        if settings.get("respect_robots_txt", True):
            if not _check_robots(url, user_agent, timeout):
                result["error"] = "robots.txt により取得不可"
                return result

        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers, timeout=timeout)
        result["status_code"] = response.status_code
        response.encoding = response.apparent_encoding

        if response.status_code != 200:
            result["error"] = f"HTTP {response.status_code}"
            return result

        soup = BeautifulSoup(response.text, "lxml")
        result["title"] = _get_title(soup)
        result["extracted_text"] = _extract_text(response.text, max_chars)
    except requests.exceptions.Timeout:
        result["error"] = f"タイムアウト（{timeout}秒）"
    except requests.exceptions.ConnectionError as e:
        result["error"] = f"接続エラー: {e}"
    except Exception as e:
        result["error"] = f"予期しないエラー: {e}"
    return result


def _build_markdown(results: list[dict], collected_at: str) -> str:
    lines = []
    lines.append("# Web収集結果")
    lines.append("")
    lines.append(f"> **収集日時:** {collected_at}")
    lines.append(f"> **収集件数:** {len(results)} 件")
    successes = [r for r in results if not r["error"]]
    failures = [r for r in results if r["error"]]
    lines.append(f"> **成功:** {len(successes)} 件 / **失敗:** {len(failures)} 件")
    lines.append("")
    lines.append("> **注意:** このファイルは一次資料の「テキスト抽出」であり、事実確認済みの情報ではありません。")
    lines.append("> Source Auditor によるランク付けと、手動での内容確認が必要です。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 収集サマリー")
    lines.append("")
    lines.append("| # | ID | 名称 | URL | ステータス | タイトル | 取得文字数 |")
    lines.append("|---|----|----|-----|-----------|--------|-----------|")
    for i, r in enumerate(results, 1):
        status = r["error"] if r["error"] else f"✓ {r['status_code']}"
        chars = len(r["extracted_text"]) if r["extracted_text"] else 0
        title_short = r["title"][:30] + "…" if len(r["title"]) > 30 else r["title"]
        lines.append(
            f"| {i} | {r['id']} | {r['name']} | {r['url']} | {status} | {title_short} | {chars} |"
        )
    lines.append("")
    if successes:
        lines.append("---")
        lines.append("")
        lines.append("## 収集成功 — 抽出テキスト")
        lines.append("")
        lines.append("> 以下は HTMLからテキストを抽出したものです。")
        lines.append("> 内容の正確性はユーザーが一次資料と照合して確認してください。")
        lines.append("")
        for r in successes:
            lines.append(f"### [{r['id']}] {r['name']}")
            lines.append("")
            lines.append(f"- **URL:** {r['url']}")
            lines.append(f"- **取得日時:** {r['fetched_at']}")
            lines.append(f"- **タイトル:** {r['title']}")
            lines.append(f"- **source_type:** {r['source_type']} / **priority:** {r['priority']}")
            lines.append("")
            lines.append("```text")
            lines.append(r["extracted_text"])
            lines.append("```")
            lines.append("")
    if failures:
        lines.append("---")
        lines.append("")
        lines.append("## 収集失敗")
        lines.append("")
        lines.append("| ID | URL | エラー内容 | 取得試行日時 |")
        lines.append("|----|-----|-----------|------------|")
        for r in failures:
            lines.append(f"| {r['id']} | {r['url']} | {r['error']} | {r['fetched_at']} |")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*このファイルは auto-research-agent の Web収集機能によって自動生成されました。*")
    lines.append("*内容は未検証です。Source Auditor によるランク付けを実施してから分析に使用してください。*")
    return "\n".join(lines)


def collect_and_save() -> Path:
    """全ソースを収集して inputs/web_collected_{YYYYMMDD}.md に保存し、Pathを返す。"""
    import time

    data = load_sources()
    sources = data.get("sources", [])
    settings = data.get("collection_settings", {})
    interval = settings.get("min_interval_sec", 2)

    collected_at = datetime.now().isoformat(timespec="seconds")
    date_str = datetime.now().strftime("%Y%m%d")

    print(f"\nWeb収集を開始します（{len(sources)} 件）")
    results = []
    for i, source in enumerate(sources):
        if i > 0:
            time.sleep(interval)
        print(f"  [{i + 1}/{len(sources)}] {source['name']} ({source['url']}) ...", end=" ", flush=True)
        result = fetch_page(source, settings)
        if result["error"]:
            print(f"失敗: {result['error']}")
        else:
            chars = len(result["extracted_text"])
            print(f"成功 ({chars} 文字)")
        results.append(result)

    _INPUTS_DIR.mkdir(exist_ok=True)
    output_path = _INPUTS_DIR / f"web_collected_{date_str}.md"
    md = _build_markdown(results, collected_at)
    output_path.write_text(md, encoding="utf-8")

    successes = sum(1 for r in results if not r["error"])
    failures = sum(1 for r in results if r["error"])
    print(f"\n収集完了: 成功 {successes} 件 / 失敗 {failures} 件")
    print(f"  → {output_path}")
    return output_path
