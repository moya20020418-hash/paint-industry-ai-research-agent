"""
config_loader.py
topics.json と inputs/*.md を読み込むモジュール
"""
import json
from pathlib import Path


def get_project_root() -> Path:
    """auto-research-agent/ のルートパスを返す"""
    return Path(__file__).parent.parent


def load_topics() -> dict:
    """config/topics.json を読み込んで返す"""
    root = get_project_root()
    topics_path = root / "config" / "topics.json"

    if not topics_path.exists():
        raise FileNotFoundError(f"topics.json が見つかりません: {topics_path}")

    with open(topics_path, encoding="utf-8") as f:
        return json.load(f)


def get_topic_by_id(topic_id: str) -> dict | None:
    """指定したIDのトピックを返す。見つからなければ None"""
    data = load_topics()
    for topic in data.get("topics", []):
        if topic.get("id") == topic_id:
            return topic
    return None


def get_default_topic() -> dict:
    """default_topic_id に対応するトピックを返す"""
    data = load_topics()
    default_id = data.get("default_topic_id")
    topic = get_topic_by_id(default_id)
    if topic is None:
        raise ValueError(f"デフォルトトピック '{default_id}' が topics.json に存在しません")
    return topic


def load_input_file(filename: str = "sample_input.md") -> str:
    """inputs/ フォルダ内のMarkdownファイルを読み込んで文字列で返す"""
    root = get_project_root()
    input_path = root / "inputs" / filename

    if not input_path.exists():
        raise FileNotFoundError(f"入力ファイルが見つかりません: {input_path}")

    with open(input_path, encoding="utf-8") as f:
        return f.read()


def list_input_files() -> list[str]:
    """inputs/ フォルダ内の .md ファイル一覧を返す"""
    root = get_project_root()
    inputs_dir = root / "inputs"
    if not inputs_dir.exists():
        return []
    return [f.name for f in inputs_dir.glob("*.md")]
