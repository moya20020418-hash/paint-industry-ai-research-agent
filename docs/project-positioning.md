# Project Positioning

## Paint Industry AI Research Agent — 塗料業界AI活用リサーチエージェント

This document explains the positioning and rationale behind this project.

---

## Why Paint and Coatings Industry?

The paint, coatings, anticorrosion, and infrastructure maintenance industry is a critical part of Japan's industrial infrastructure. Bridge maintenance, anticorrosion treatment, and infrastructure repair are ongoing government priorities backed by public spending.

At the same time, this industry has characteristics that make AI adoption challenging:

- Many companies are small or medium-sized, without dedicated IT or data science teams
- Products are highly technical, requiring compatibility checks and regulatory knowledge
- Sales and support processes involve repetitive technical inquiries that are good candidates for AI assistance
- Market research and competitive intelligence are typically done manually

This makes it a meaningful target for practical AI adoption support tools.

---

## Why SMEs?

Many SMEs do not have dedicated data science or software engineering teams. Traditional B2B industries often lack accessible AI adoption workflows. Non-engineer staff still need to perform market research, competitor analysis, and internal proposal drafting.

This tool aims to make AI-assisted research workflows accessible without requiring advanced programming knowledge.

Specifically:

- Large companies can hire consultants or build internal tools. SMEs generally cannot.
- Non-engineer staff at SMEs are often the ones who most need structured research support.
- Business users who want to propose AI adoption internally need a way to collect evidence and structure arguments — without writing code.
- AI tools that require API keys, Python expertise, or cloud setup are inaccessible to most SME staff.

This project targets the gap between "generic AI chatbots" and "enterprise AI platforms" — providing a structured, human-in-the-loop research workflow that SME staff can actually use.

---

## Why AI Adoption Research?

Many SMEs in traditional industries are at the stage of asking: "Should we adopt AI? Where would it help? What would it cost?" They lack a structured way to answer these questions.

This tool is designed to help non-engineer staff:

1. Collect publicly available information about their market and competitors
2. Identify where competitors may or may not be using AI
3. Structure the analysis with clear fact/assumption/insight separation
4. Generate a research report that can be used as the basis for an internal proposal
5. Identify specific business processes where AI adoption may create practical value

---

## Why Open Source?

Open-source distribution allows:

- SMEs to use the tool without licensing costs
- Business users to adapt the tool to their specific industry or company context
- Community contributions to improve the tool for more industries and use cases
- Transparent methodology — users can see exactly how reports are structured and what assumptions are made
- Trust — users can verify that the tool does not send their research data to external services

---

## Why Non-Engineer Friendly?

The tool uses simple configuration files. Users can add URLs without writing code. Reports are generated as Markdown. The workflow separates facts, assumptions, and insights. Human review remains central.

Specifically:

- `config/topics.json` can be edited in any text editor to add research topics
- `config/sources.json` can be edited to add URLs without writing Python
- `inputs/` accepts plain text Markdown files — users can write research notes naturally
- Reports are plain Markdown files that open in any text editor or viewer
- The workflow is documented in plain language that non-engineers can follow
- No cloud setup, no API keys, no database — just Python and text files

---

## Difference from Generic Web Scraping Tools

Generic web scraping tools collect data but do not structure or audit it. This tool:

- Separates collected text from verified facts
- Requires source auditing (A/B/C/D reliability ranking) before facts are used
- Flags numerical claims without sources as unreliable
- Produces structured research reports rather than raw data dumps
- Is designed for business research workflows, not data engineering

---

## Difference from Generic AI Chatbots

Generic AI chatbots (ChatGPT, Claude, etc.) can produce fluent text but:

- May confabulate (hallucinate) facts
- Do not maintain a structured source audit trail
- Do not separate facts from assumptions in a verifiable way
- Are not designed for multi-session structured research workflows

This tool provides a structured workflow that keeps human judgment central and makes the source of every claim traceable.

---

## Expected Users

| User Type | How They Use This Tool |
|-----------|------------------------|
| Sales staff at paint/coatings SME | Collect competitor information, prepare customer proposals |
| Planning staff at manufacturing SME | Research market trends, identify AI adoption opportunities |
| Operations staff | Analyze product compatibility inquiry patterns |
| Business managers at traditional B2B companies | Prepare internal AI adoption proposals |
| Non-engineer AI adoption champions | Collect evidence for AI project proposals |

---

## Ethical Considerations

- **No confidential data in public examples** — All sample files use public or synthetic data.
- **`robots.txt` compliance** — The tool respects `robots.txt` by default.
- **Human review required** — The tool explicitly states that generated reports must be reviewed before business use.
- **No hallucination by design** — The workflow separates facts (with sources) from assumptions and insights.
- **No guarantees of accuracy** — The tool does not claim to produce factually correct reports; it produces structured templates that require human verification.
- **Transparent methodology** — The workflow is fully documented and auditable.

---

## Target Users Summary

- Small and medium-sized enterprises (SMEs)
- Non-engineer business users
- Paint and coatings industry professionals
- Anticorrosion and infrastructure maintenance companies
- Manufacturing SMEs
- Sales, planning, marketing, and operations staff
- Business users who want to adopt AI but do not have in-house engineering teams
- Non-engineer AI adoption champions inside traditional B2B companies
