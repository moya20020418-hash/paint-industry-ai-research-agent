# Paint Industry AI Research Agent

**塗料業界AI活用リサーチエージェント**

---

**Paint Industry AI Research Agent** is an early-stage open-source research assistant for small and medium-sized enterprises (SMEs), especially non-engineer business users in traditional industries such as paint, coatings, anticorrosion, infrastructure maintenance, and manufacturing.

The tool helps users collect public web sources, structure research notes, audit source reliability, check numerical claims, and generate practical market research reports focused on AI adoption opportunities.

It is designed for human-in-the-loop research workflows. It does not replace expert judgment, but helps non-engineer users organize information and identify where AI may create practical business value.

---

このツールは、中小企業、とくに塗料・防錆・インフラ補修・製造業などの伝統的産業で働く非エンジニア向けの、初期段階のオープンソースAIリサーチ支援ツールです。

公開Web情報を収集し、調査メモを整理し、ソース信頼性や数値根拠を確認しながら、AI導入機会を発見するための市場調査レポートを作成することを目的としています。

このツールは人間の判断を置き換えるものではなく、中小企業の非エンジニアがAIを活用した調査・提案・業務改善を始めるための補助ツールです。

---

## Project Purpose

Paint, coatings, anticorrosion, infrastructure maintenance, and industrial coating companies can use this tool to:

- Research market trends and competitor activity using publicly available sources
- Identify where AI adoption may create practical business value
- Structure market research findings with clear fact / assumption / insight separation
- Prepare internal proposals and research drafts without engineering support

This project is specifically designed for **non-engineer business users at SMEs** who need structured research support but do not have dedicated data science or engineering teams.

---

## Target Users

- Small and medium-sized enterprises (SMEs)
- Non-engineer business users
- Paint and coatings industry professionals
- Anticorrosion and infrastructure maintenance companies
- Manufacturing SMEs
- Sales, planning, marketing, and operations staff
- Business users who want to adopt AI but do not have in-house engineering teams
- Non-engineer AI adoption champions inside traditional B2B companies

---

## What This Tool Does

- Collects public web sources from configured URLs (respects `robots.txt`)
- Saves collected text into Markdown for review
- Generates structured research reports in Markdown format
- Separates facts, assumptions, and insights clearly
- Provides a source reliability auditing framework (A/B/C/D ranking)
- Checks numerical claims and flags those without sources
- Identifies AI adoption opportunities in the paint and coatings industry
- Helps non-engineer SME users prepare internal research and proposal drafts

---

## Use Cases

- Paint industry market research
- Anticorrosion and infrastructure maintenance research
- Competitor analysis using publicly available information
- AI adoption opportunity discovery for traditional industries
- Internal proposal drafting for AI projects
- Weekly industry intelligence preparation
- Sales support research
- Manufacturing SME AI adoption research

---

## Requirements

- Python 3.10 or higher
- **Core report generation** uses only the Python standard library — no additional installation needed
- **Web collection** (`--collect-web`) requires optional dependencies:

```bash
pip install requests beautifulsoup4 lxml
```

You only need to run this once. If you skip this step, all features except `--collect-web` will work without any installation.

### Check your Python version

```bash
python --version
```

If it shows `Python 3.10.x` or higher, you are ready to start.

---

## Quick Start

### Step 1: Clone or download the repository

```bash
git clone https://github.com/moya20020418-hash/paint-industry-ai-research-agent.git
cd paint-industry-ai-research-agent
```

Or download as a ZIP from GitHub and extract it.

### Step 2: Configure your research sources

Open `config/sources.json` in any text editor (Notepad, TextEdit, VS Code).

Add URLs you want to collect from:

```json
{
  "id": "my_source",
  "name": "Company or Site Name",
  "url": "https://example.com/",
  "source_type": "official_company",
  "priority": "high"
}
```

See `examples/sample_sources.json` for a full configuration example.

### Step 3: Write your research notes

Open `inputs/sample_input.md` in a text editor and add your research notes, questions, and reference URLs.

See `examples/sample_input.md` for guidance on what to include.

### Step 4: Collect web sources (optional)

> **First-time setup for web collection:** Install the required libraries once before running this step.
> ```bash
> pip install requests beautifulsoup4 lxml
> ```

```bash
python src/main.py --collect-web
```

This collects text from the URLs in `config/sources.json` and saves them to `inputs/web_collected_YYYYMMDD.md`.

### Step 5: Generate a research report

Run the report generator with an input file from the `inputs/` folder.

On Windows:

```powershell
py src/main.py --input sample_input.md
```

On macOS/Linux:

```bash
python src/main.py --input sample_input.md
```

The command above reads:

```text
inputs/sample_input.md
```

The report is saved to:

```text
reports/research_report_YYYYMMDD_HHMMSS.md
```

### Step 6: Review the report

Open the report in any text editor. **Fill in Sections 4-6 with your verified research findings before sharing it.**

### Example Report Output

A sample generated report is available at:

`reports/research_report_webcollect_anticorrosion_20260530.md`

The report demonstrates how the tool separates:

- confirmed facts
- hypotheses
- business implications
- numeric evidence checks
- uncertainty and risks
- QA checklist results

For safety, the tool does not make unsupported claims about market size, growth rate, product performance, or competitor superiority unless reliable source text is available.

The sample report is based on collected public web text and should be treated as an assisted research draft, not as a fully verified market report.

---

## Example Commands

### Windows

```powershell
# Generate a report from the sample input
py src/main.py --input sample_input.md

# Collect web sources from configured URLs
py src/main.py --collect-web

# Generate a report from collected web text
py src/main.py --input web_collected_YYYYMMDD.md

# Generate a report from your own research notes
py src/main.py --input my_research_notes.md

# List available research topics
py src/main.py --list-topics

# List input files in inputs/
py src/main.py --list-inputs

# Generate a report for a specific topic
py src/main.py --topic ai_agent_market
```

### macOS/Linux

```bash
# Generate a report from the sample input
python src/main.py --input sample_input.md

# Collect web sources from configured URLs
python src/main.py --collect-web

# Generate a report from collected web text
python src/main.py --input web_collected_YYYYMMDD.md

# Generate a report from your own research notes
python src/main.py --input my_research_notes.md

# List available research topics
python src/main.py --list-topics

# List input files in inputs/
python src/main.py --list-inputs

# Generate a report for a specific topic
python src/main.py --topic ai_agent_market
```

---

## File Structure

```
paint-industry-ai-research-agent/
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── .gitignore
├── config/
│   ├── topics.json        <- Research topic definitions (edit to add your topics)
│   └── sources.json       <- Source URL configuration (edit to add your sources)
├── inputs/
│   └── sample_input.md    <- Research note template (copy and fill in)
├── reports/               <- Generated reports (not committed to git)
├── examples/
│   ├── sample_sources.json   <- Example source configuration
│   └── sample_input.md       <- Example research notes
├── docs/
│   ├── project-positioning.md
│   └── codex-for-oss-application-draft.md
├── skills/                <- Research agent skill definitions
├── agents/                <- Research agent role definitions
├── workflows/
│   └── daily-market-research-workflow.md   <- Full 9-step research workflow
└── src/
    ├── main.py            <- Entry point (run this)
    ├── config_loader.py   <- Configuration and input loading
    ├── report_generator.py <- Report generation
    ├── web_collector.py   <- Web source collection
    └── templates.py       <- Report templates
```

---

## How to Read Generated Reports

Generated reports use these tags:

| Tag | Meaning |
|-----|---------|
| (none) or [FACT] | Confirmed from a primary source |
| [ASSUMPTION] | Logically derived from confirmed facts |
| [INSIGHT] | Actionable suggestion based on facts and assumptions |
| [NEEDS VERIFICATION] | Source not yet confirmed |
| [SOURCE UNKNOWN] | Unreliable, excluded from report |

Japanese tags:

| タグ | 意味 |
|------|------|
| 【事実】 | 一次資料で確認済み |
| 【推測】 | 事実から論理的に推測した内容 |
| 【示唆】 | 推測をもとにした行動提案 |
| 【要確認】 | 根拠が未確認 |
| 【根拠不明】 | 使用禁止 |

**Important:** The generated report is a structured template. Sections 4-6 require you to fill in your own verified findings. Do not treat the template itself as research output.

---

## Safety and Limitations

- **This tool does not guarantee factual correctness.** Generated reports are templates that require human review.
- **Web-collected text must be source-audited.** Collected text is raw HTML extraction, not verified fact.
- **It does not replace human review.** All reports should be reviewed before business use.
- **Respect `robots.txt` and site terms.** The tool is configured to respect `robots.txt` by default. Do not change this setting.
- **Do not include confidential or private company data.** Only use publicly available sources.
- **Generated reports should be reviewed before business use.** Do not share unreviewed reports externally.
- **This project is an early-stage tool, not a finished product.** Expect limitations and rough edges.

---

## Research Workflow

The full 9-step research workflow is documented in `workflows/daily-market-research-workflow.md`.

| Step | Agent | Role |
|------|-------|------|
| 1 | Input Loader | Load and organize topics and research notes |
| 2 | Researcher | Classify facts, assumptions, and unverified items |
| 3 | Source Auditor | Rate source reliability (A/B/C/D) |
| 4 | Numeric Checker | Verify numerical claims have sources |
| 5 | Competitor Analyst | Organize competitor and market comparison |
| 6 | Insight Agent | Extract market, business, and AI adoption insights |
| 7 | Red Team Critic | Identify weak claims, missing perspectives, bias |
| 8 | QA Agent | Final hallucination and source check |
| 9 | Report Writer | Generate final Markdown report |

To use the workflow with Claude Code:

```
Follow workflows/daily-market-research-workflow.md and create a market research report
from inputs/sample_input.md for the topic: anticorrosion_market
```

---

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the full roadmap.

Highlights:

- PDF and government statistics support
- AI-assisted source auditing and insight generation (Claude / OpenAI API)
- Scheduled weekly reports and GitHub Actions
- Multi-industry support (construction, food manufacturing, logistics)
- SME-friendly onboarding and non-engineer templates

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

Non-engineer contributions are especially welcome: documentation improvements, use case descriptions, and industry-specific templates.

---

## Windows Users Note

If Japanese characters appear garbled in the command prompt, this is a display issue only. The generated Markdown files are saved correctly. Open them in VS Code or Notepad to view them properly.

On some Windows systems, the `python` command may not work (it opens the Microsoft Store instead). Use the `py` launcher instead:

```powershell
py src/main.py --list-topics
py src/main.py --collect-web
py -m pip install requests beautifulsoup4 lxml
```

---

## Frequently Asked Questions

**Q: `python` command not found or opens the Microsoft Store**
A: Use the `py` launcher instead: `py src/main.py`. If `py` is also not found, download Python from [python.org](https://www.python.org/) and make sure to check "Add Python to PATH" during installation.

**Q: `ModuleNotFoundError`**
A: Run `py src/main.py` (not `python`) from the project root directory. If the error is about `requests` or `bs4`, run `py -m pip install requests beautifulsoup4 lxml` first.

**Q: The report is mostly blank**
A: This is expected. The tool generates a structured template. Fill in Sections 4-6 (confirmed facts, assumptions, insights) and Sections 11-16 (AI adoption opportunities) with your own research findings.

**Q: Can I use this without programming knowledge?**
A: Yes, with guidance. You need to run a few commands in the terminal. See the Quick Start section. More user-friendly options are planned for future releases.

---

## License

MIT License — see [LICENSE](LICENSE).
