# Project Memory — Paint Industry AI Research Agent

> このファイルは、プロジェクトの方針・位置づけ・価値仮説・表現ルールを記録する内部ドキュメントです。
> README や Codex応募文を書くときの一貫したガイドラインとして参照してください。
> 新機能の追加や実装計画はここに書きません。

---

## 1. プロジェクトの核心的な位置づけ

### 開発者の自己位置づけ

このプロジェクトの**開発者自身も、中小企業で働く非エンジニア**である。

外部のエンジニアが上から中小企業向けに作るツールではなく、**中小企業の現場で働く非エンジニア自身が、同じ立場の人たちのために作るOSS** として位置づける。

この点は、README・CONTRIBUTING・Codex応募文・project-positioning において重要な差別化ポイントとして一貫して表現すること。

### 英語での表現（応募文・README用）

> This project is built by a non-engineer working in an SME, for non-engineer workers in SMEs. It focuses on traditional B2B industries such as paint, coatings, anticorrosion, manufacturing, and infrastructure maintenance, where AI and DX adoption may be difficult due to limited engineering resources, limited budgets, and lack of dedicated data science teams. The goal is not to replace experts or consultants, but to provide a practical, human-in-the-loop research workflow that helps SME workers collect public information, audit sources, check numerical claims, and identify realistic AI adoption opportunities.

### 日本語での表現（README・社内説明用）

> このプロジェクトは、中小企業で働く非エンジニア自身が、同じように中小企業で働く非エンジニアのために開発しているものです。専門家やコンサルタントを置き換えるものではなく、人間の確認を前提に、公開情報の収集、ソース監査、数値確認、AI導入機会の発見を支援する実務的なリサーチワークフローを提供します。

---

## 2. 対象ユーザー（利用者・コントリビューター共通）

| 対象 | 詳細 |
|------|------|
| 企業規模 | 中小企業（SME） |
| 業種 | 塗料・防錆・製造業・インフラ補修関連の伝統的BtoB産業 |
| 職種 | 営業・企画・マーケティング・技術営業・現場改善担当・総務 |
| 技術レベル | 非エンジニア（プログラミング知識不要を目指す） |
| 状況 | 社内にエンジニアやデータサイエンス部門がない |
| ニーズ | AI化・DX化を進めたいが何から始めればよいか分からない |

### コントリビューターも非エンジニアを想定する

コードを書く貢献だけでなく、以下も同等の貢献として扱う：

- ドキュメント改善・誤字修正
- サンプルデータ・テンプレートの追加
- ユースケースの追加
- 日本語・英語翻訳
- 使ってみた感想・改善提案のIssue

---

## 3. 価値仮説（断定しない表現で記載する）

### 正しい表現

> 塗料・防錆・製造業・インフラ補修などの伝統的BtoB領域では、特に中小企業や非エンジニアにとって、AI活用やDXを始めるための実務的なワークフローが不足している**可能性がある**。このプロジェクトは、そのギャップを埋めるための初期段階のOSSです。

### 禁止表現（業界全体の断定）

- 「塗料業界はAI化が全然進んでいない」→ 根拠なく業界全体を断定している
- 「DX化が全く進んでいない」→ 同上
- 「この業界はデジタル化が遅れている」→ 同上

業界全体の傾向ではなく、「中小企業・非エンジニアにとっての実務的な課題」として表現すること。

---

## 4. プロジェクトの強み

1. **開発者自身が中小企業の非エンジニアであること** — 対象ユーザーと同じ立場から設計している
2. **利用者も非エンジニアを想定** — コマンドラインに不慣れな人でも使えることを目指す
3. **対象領域が伝統的BtoB産業** — AI化・DXの壁が大きい可能性のある産業が対象
4. **Human-in-the-loop設計** — AIが自動判断するのではなく、人間のレビューを前提にする
5. **ソース監査・数値確認の組み込み** — ハルシネーション防止が最重要目的
6. **将来的な拡張性** — 市場調査から財務分析・企業分析・経営分析への拡張を想定
7. **OSSとして公開** — 中小企業でも無料で使える、コミュニティ貢献を歓迎

---

## 5. OpenAI Codex for OSS 応募方針

### 応募での位置づけ

- early-stage open-source project
- SME-focused
- non-engineer friendly
- human-in-the-loop
- source-audited research workflow
- traditional industry AI adoption
- AI adoption opportunity discovery
- public-source research assistant

### Codex / API クレジットの使用用途として強調すること

- OSSメンテナンス（Issue整理・PRレビュー・ドキュメント改善）
- 非エンジニア向けドキュメントの改善・翻訳
- AI支援によるソース監査・インサイト抽出の試作
- サンプルデータ・テンプレートの整備
- 安全なAPI連携設計の実装

### 応募文で強調しないこと

- 「ChatGPT Proを無料で欲しい」という表現
- 個人的な利益への言及

詳細な応募文下書きは `docs/codex-for-oss-application-draft.md` を参照。

---

## 6. 使うべき表現・避けるべき表現

### 使うべき表現

| 表現 | 使う場面 |
|------|---------|
| early-stage open-source tool | プロジェクト概要 |
| SME-focused | ターゲット説明 |
| non-engineer friendly | 設計方針 |
| human-in-the-loop | ワークフロー説明 |
| source-audited research workflow | 機能説明 |
| AI adoption opportunity discovery | ユースケース |
| practical research assistant | ポジショニング |
| traditional industry AI adoption | 対象領域 |
| public-source research assistant | 機能説明 |
| built by a non-engineer working in an SME, for non-engineer SME workers | 開発者説明 |
| designed for analog, traditional B2B industries where AI adoption may be difficult | 対象領域 |

### 避けるべき表現

| 禁止表現 | 理由 |
|---------|------|
| enterprise-grade | 大企業向け高機能ツールを示唆する |
| fully automated intelligence platform | 完全自動化の断定 |
| replaces consultants | 専門家を置き換えると断定 |
| guarantees accurate research | 正確性を保証すると断定 |
| widely used | 実績がないのに普及済みと主張 |
| industry standard | 実績がないのに標準化を主張 |
| AI will do everything automatically | 完全自動化の断定 |
| no human review needed | 人間のレビュー不要と断定 |
| 塗料業界はAI化が全然進んでいない | 業界全体の遅れを断定 |
| DX化が全く進んでいない | 同上 |

---

## 7. 安全設計方針

APIキーや認証情報の扱いに関するルール：

- ユーザーにAPIキーをファイルに直接書かせない
- 将来的なAPI連携では GitHub Secrets・環境変数・OAuth を優先する
- `.env` を使う場合は `.env.example` のみリポジトリに含め、`.env` 本体は `.gitignore` で除外する
- `secrets.json`・`credentials.json` 等の秘密情報ファイルも `.gitignore` に含める
- コマンドラインへのAPIキー直接入力も避ける設計にする
- 初期機能はAPIキー不要で動作すること（標準ライブラリのみで実装済み）

---

## 8. 今後の拡張方向（方針のみ、実装計画ではない）

- 財務分析・企業分析・経営分析への拡張
- 業界比較・競合比較
- 投資判断・与信判断の補助
- 中小企業向け経営支援レポート
- 社内提案・業務改善・AI導入提案の自動化
- 最終目標：「中小企業の非エンジニアでも使えるAIリサーチ／経営分析エージェント」

詳細は `ROADMAP.md` を参照。

---

## 9. このファイルの更新ルール

- 新機能の実装計画はここに書かない（ROADMAP.md に書く）
- コード変更の記録はここに書かない（git log で管理する）
- プロジェクトの目的・ターゲット・表現ルール・価値仮説に関する変更はここに追記する

最終更新：2026-06-01
