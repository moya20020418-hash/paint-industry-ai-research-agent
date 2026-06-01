"""
main.py
auto-research-agent のエントリポイント

使い方:
    python src/main.py
    python src/main.py --topic ai_agent_market
    python src/main.py --input my_notes.md
"""
import argparse
import sys
from pathlib import Path

# Windows コマンドプロンプトで日本語が文字化けしないよう UTF-8 出力に統一
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf_8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# src/ フォルダを Python パスに追加（他モジュールを import するため）
sys.path.insert(0, str(Path(__file__).parent))

from config_loader import get_default_topic, get_topic_by_id, list_input_files, load_input_file
from report_generator import generate_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="企業・市場調査AIリサーチャー レポート生成ツール"
    )
    parser.add_argument(
        "--topic",
        type=str,
        default=None,
        help="調査テーマID（例: anticorrosion_market）。省略するとデフォルトを使用",
    )
    parser.add_argument(
        "--input",
        type=str,
        default="sample_input.md",
        help="inputs/ フォルダ内の入力ファイル名（デフォルト: sample_input.md）",
    )
    parser.add_argument(
        "--list-topics",
        action="store_true",
        help="利用可能なトピック一覧を表示して終了",
    )
    parser.add_argument(
        "--list-inputs",
        action="store_true",
        help="inputs/ フォルダのファイル一覧を表示して終了",
    )
    parser.add_argument(
        "--collect-web",
        action="store_true",
        help="sources.json に定義された URL からテキストを収集して inputs/ に保存する",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # --list-topics: トピック一覧を表示
    if args.list_topics:
        from config_loader import load_topics
        data = load_topics()
        print("\n利用可能な調査テーマ:")
        for t in data.get("topics", []):
            print(f"  [{t['id']}] {t['name']} ({t.get('priority', '?')}優先度)")
        return

    # --collect-web: Web収集を実行
    if args.collect_web:
        from web_collector import collect_and_save
        collect_and_save()
        return

    # --list-inputs: 入力ファイル一覧を表示
    if args.list_inputs:
        files = list_input_files()
        print("\ninputs/ フォルダのファイル:")
        for f in files:
            print(f"  {f}")
        return

    # 調査テーマを取得
    if args.topic:
        topic = get_topic_by_id(args.topic)
        if topic is None:
            print(f"エラー: トピックID '{args.topic}' が見つかりません。")
            print("利用可能なIDを確認するには: python src/main.py --list-topics")
            sys.exit(1)
    else:
        topic = get_default_topic()

    print(f"\n調査テーマ: {topic['name']}")

    # 入力ファイルを読み込む
    print(f"入力ファイル: inputs/{args.input}")
    input_text = load_input_file(args.input)
    print(f"  → {len(input_text)} 文字を読み込みました")

    # レポートを生成
    print("\nレポートを生成中...")
    output_path = generate_report(topic, input_text)

    print(f"\n完了！レポートを出力しました:")
    print(f"  {output_path}")
    print("\n次のステップ:")
    print("  1. レポートをテキストエディタ（メモ帳等）で開く")
    print("  2. セクション4〜6 に調査結果を手入力する")
    print("  3. セクション10 のQAチェックを確認してから共有する")


if __name__ == "__main__":
    main()
