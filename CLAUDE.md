# CLAUDE.md - auto-research-agent

このプロジェクトでは、すべて日本語で回答してください。

## プロジェクト名

**Paint Industry AI Research Agent（塗料業界AI活用リサーチエージェント）**

## プロジェクトの目的

塗料・防錆・インフラ補修・製造業などの伝統的産業に従事する中小企業（SME）の非エンジニアが、公開Web情報を収集し、調査メモを整理し、ソース信頼性や数値根拠を確認しながら、AI導入機会を発見するための市場調査レポートを作成できる、オープンソースのAIリサーチ支援ツール。

**設計方針：**

- **SME-focused（中小企業向け）** — エンジニアチームを持たない中小企業が対象
- **Non-engineer friendly（非エンジニア向け）** — プログラミング知識なしでも使えることを目指す
- **Human-in-the-loop（人間のレビューが前提）** — AIが自動判断するのではなく、人間のレビューを中心に据える
- **Public-source research workflow（公開情報のみ使用）** — 機密情報・内部情報は一切使用しない
- **AI adoption opportunity discovery（AI導入機会の発見）** — 塗料業界・製造業SMEでのAI活用機会を整理する
- **Traditional industry AI adoption（伝統的産業のAI導入支援）** — AI普及が遅い産業への橋渡し

**最重要目的：ハルシネーション防止**

## 開発者の自己位置づけ

このプロジェクトの開発者自身も、**中小企業で働く非エンジニア**である。

外部のエンジニアが上から中小企業向けに作るツールではなく、**中小企業の現場で働く非エンジニア自身が、同じ立場の人たちのために作るOSS** として位置づける。

この視点は、README・CONTRIBUTING・docs/codex-for-oss-application-draft.md・docs/project-positioning.md における重要な文脈として一貫して扱うこと。

利用者だけでなく、**コントリビューターも非エンジニアを想定**する。コードを書く貢献だけでなく、ドキュメント改善・サンプル追加・ユースケース追加も同等の貢献として扱う。

## 価値仮説（断定しない表現）

以下の表現を使うこと：

> 塗料・防錆・製造業・インフラ補修などの伝統的BtoB領域では、特に中小企業や非エンジニアにとって、AI活用やDXを始めるための実務的なワークフローが不足している可能性がある。このプロジェクトは、そのギャップを埋めるための初期段階のOSSです。

以下のような断定は使わないこと：

- 「塗料業界はAI化が全然進んでいない」
- 「DX化が全く進んでいない」

## 安全設計方針

APIキーや認証情報の扱いに関するルール：

- ユーザーにAPIキーを直接ファイルに書かせない
- 将来的なAPI連携では GitHub Secrets・環境変数・OAuth を優先する
- `.env` を使う場合は `.env.example` のみリポジトリに含め、`.env` 本体は `.gitignore` で除外する（設定済み）
- `secrets.json`・`credentials.json` 等の秘密情報ファイルも `.gitignore` に含める（設定済み）

## ファイル構成

```
auto-research-agent/
├─ LICENSE
├─ README.md
├─ CONTRIBUTING.md / ROADMAP.md / SECURITY.md / CODE_OF_CONDUCT.md / .gitignore
├─ config/
│  ├─ topics.json          # 調査テーマ定義（テーマ追加はここを編集）
│  └─ sources.json         # Web収集対象URL（情報源追加はここを編集）
├─ inputs/                 # ユーザーが手動で作成する調査メモ
├─ reports/                # 自動生成されたレポート（Gitには含まない）
├─ examples/               # サンプル設定・サンプル入力（公開用）
├─ docs/                   # プロジェクト位置づけ・Codex応募文
├─ skills/                 # エージェントスキル定義
├─ agents/                 # エージェント役割定義
├─ workflows/
│  └─ daily-market-research-workflow.md  # 9ステップリサーチワークフロー
└─ src/
   ├─ main.py              # エントリポイント（ここを実行する）
   ├─ config_loader.py     # topics.json / inputs/ 読み込み
   ├─ web_collector.py     # Web収集（sources.json のURLからテキスト取得）
   ├─ report_generator.py  # reports/ へのレポート生成
   └─ templates.py         # Markdownテンプレート
```

## 実行方法

```bash
python src/main.py                            # デフォルトテーマでレポート生成
python src/main.py --topic ai_agent_market    # テーマ指定
python src/main.py --input my_notes.md        # 入力ファイル指定
python src/main.py --list-topics              # テーマ一覧
python src/main.py --list-inputs              # inputs/ ファイル一覧
python src/main.py --collect-web              # sources.json のURLからWeb収集
```

## 最重要方針

- 入力にない事実を断定しない
- 事実・推測・示唆を必ず分ける
- 数値には根拠あり/根拠不明を明記する
- 公式資料・一次情報を優先する
- 根拠不明の情報は使用禁止

## 表記ルール

| 層 | タグ | 使用条件 |
|----|------|----------|
| 事実 | （なし or 【事実】） | 一次資料確認済み |
| 推測 | 【推測】 | 事実から論理導出 |
| 示唆 | 【示唆】 | アクション提案 |
| 未確認 | 【要確認】 | 根拠未確認 |
| 除外 | 【根拠不明・除外】 | 使用禁止 |

## 禁止表現

**レポート本文での断定禁止：**
「絶対」「保証」「必ず」「最適」「万能」「問題ありません」「確実に」

**プロジェクト説明・README・応募文での禁止表現：**

| 禁止表現 | 理由 |
|---------|------|
| enterprise-grade | 大企業向け高機能ツールを示唆する |
| fully automated / AI will do everything automatically | 完全自動化の断定 |
| replaces consultants | 専門家を置き換えると断定 |
| guarantees accurate research | 正確性を保証すると断定 |
| widely used / industry standard | 実績がないのに普及済みと主張 |
| 塗料業界はAI化が全然進んでいない | 業界全体の遅れを断定（可能性として表現すること） |
| no human review needed | 人間のレビュー不要と断定 |

**推奨表現：**
early-stage open-source tool / SME-focused / non-engineer friendly / human-in-the-loop / source-audited research workflow / AI adoption opportunity discovery / practical research assistant / traditional industry AI adoption / built by a non-engineer working in an SME, for non-engineer SME workers

## 拡張予定（ロードマップ概要）

詳細は `ROADMAP.md` を参照。

- Phase 3: 塗料業界AI活用機会レポート（SME向け）
- Phase 4: PDF・政府統計対応
- Phase 5: Claude / OpenAI API 連携
- Phase 6: GitHub Actions による定期自動化
- Phase 7: 他の伝統的産業への拡張
- Phase 8: 非エンジニア向けUIと設定テンプレート

## 作業ルール

- 実装前に変更対象ファイルを列挙する
- 既存機能を壊さない
- validateData() 相当のチェックを実施する
