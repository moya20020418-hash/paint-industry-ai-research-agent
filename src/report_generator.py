"""
report_generator.py
Markdownレポートを reports/ フォルダに出力するモジュール
"""
from datetime import datetime
from pathlib import Path

from templates import get_report_template


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def generate_report(
    topic: dict,
    input_text: str,
    generated_at: datetime | None = None,
) -> Path:
    """
    レポートを生成して reports/ に保存する。
    保存したファイルの Path を返す。

    topic     : config/topics.json の1件分のdict
    input_text: inputs/*.md の生テキスト
    generated_at: 生成日時（省略時は現在時刻）
    """
    if generated_at is None:
        generated_at = datetime.now()

    content = get_report_template(topic, input_text, generated_at)

    root = get_project_root()
    reports_dir = root / "reports"
    reports_dir.mkdir(exist_ok=True)

    timestamp = generated_at.strftime("%Y%m%d_%H%M%S")
    topic_id = topic.get("id", "unknown")
    filename = f"research_report_{topic_id}_{timestamp}.md"
    output_path = reports_dir / filename

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    return output_path
