# OpenAI Codex for Open Source — Application Draft

> This document is a draft for applying to the OpenAI Codex for Open Source program.
> Edit as needed before submitting.

---

## 1. Project Summary

**Paint Industry AI Research Agent** is an early-stage open-source research assistant for small and medium-sized enterprises (SMEs) in traditional industries such as paint, coatings, anticorrosion, and infrastructure maintenance.

The tool helps non-engineer business users collect public web sources, structure research notes, audit source reliability, check numerical claims, and generate practical market research reports focused on AI adoption opportunities.

It is designed as a human-in-the-loop workflow — it does not replace expert judgment, but helps non-engineer users organize public information and identify where AI may create practical business value.

- **Repository:** (your GitHub repository URL)
- **License:** MIT
- **Language:** Python 3.10+, Markdown
- **Status:** Early-stage open-source project

---

## 2. Why This Project Matters

Many SMEs in traditional industries are aware that AI is changing business, but lack a structured way to evaluate where AI could help them. They do not have internal data science or engineering teams. Their staff are sales managers, operations coordinators, and technical support staff — not software engineers.

At the same time, these companies face real business problems that AI could help with:

- Repetitive technical inquiries that could be structured for AI assistance
- Manual competitor research that takes hours each week
- Internal proposal drafting that lacks structured evidence
- Market trend monitoring that is currently done by reading websites manually

This project focuses on making AI-assisted research workflows accessible to SMEs and non-engineer business users in traditional industries. Many small and medium-sized companies do not have dedicated engineering or data science teams, but still need to understand market changes, competitor activity, and practical AI adoption opportunities. This project provides a structured, human-in-the-loop research workflow that helps users collect public sources, audit claims, and generate practical reports.

The paint and coatings industry is the initial focus, but the framework generalizes to other traditional B2B industries where AI adoption is slower than in software-first sectors.

---

## 3. My Role as Maintainer

I am the primary maintainer and creator of this project. I am responsible for:

- Initial design and implementation of the research workflow
- Maintaining the Python codebase (`src/`)
- Maintaining workflow documentation (`workflows/`)
- Responding to Issues and Pull Requests
- Improving the tool based on real SME use cases
- Maintaining the project direction toward non-engineer accessibility

This is an early-stage project. I am the sole maintainer at this point, building toward a community of contributors from SME and traditional industry backgrounds.

---

## 4. How Codex / ChatGPT Pro / API Credits Would Be Used

If accepted for the Codex for Open Source program, I would use the credits for:

### OSS Maintenance Workflows

- **Issue triage** — Using AI assistance to categorize and respond to GitHub Issues
- **PR review support** — Using AI to review Pull Requests for correctness and non-engineer friendliness
- **Documentation improvement** — Using AI to improve README clarity, translate documentation between Japanese and English, and write non-engineer-friendly guides

### AI Research Workflow Improvement

- **Testing AI-assisted source auditing** — Experimenting with AI-assisted source reliability classification
- **Testing AI-assisted insight generation** — Prototyping AI-assisted extraction of AI adoption opportunities from collected web text
- **Hallucination prevention research** — Using AI to help design fact/assumption/insight separation rules

### SME Use Case Development

- **Developing industry-specific templates** — Using AI assistance to develop research templates for additional traditional industries
- **Non-engineer documentation** — Using AI to review and improve documentation for accessibility to non-technical users

---

## 5. Maintenance Workflows to Improve

Current manual workflows that AI assistance could improve:

| Workflow | Current State | Improvement Goal |
|----------|--------------|-----------------|
| Source auditing | Fully manual A/B/C/D ranking | AI-assisted preliminary ranking |
| Insight extraction | Manual, human-written | AI-assisted draft with human review |
| Documentation | Japanese primary, limited English | Bilingual, non-engineer friendly |
| Issue triage | Manual | AI-assisted categorization |
| PR review | Manual | AI-assisted review for non-engineer accessibility |

---

## 6. Current Limitations

This is an early-stage project. Current limitations include:

- Reports are templates that require manual fill-in for Sections 4-6
- Web collection is limited to plain HTML text extraction (no PDF support yet)
- Source auditing is manual — no AI assistance yet
- No API integration — no external AI calls
- Documentation is primarily in Japanese — English documentation is limited
- Setup requires command-line knowledge — not yet accessible to non-technical users without guidance
- No GUI or web interface — command-line only

These limitations are acknowledged and are the focus of the roadmap.

---

## 7. Roadmap Summary

- **Phase 1 (Complete):** MVP research workflow with structured report generation
- **Phase 2 (Complete):** Web source collection from configured URLs
- **Phase 3:** Paint industry AI opportunity report sections
- **Phase 4:** PDF and government statistics support
- **Phase 5:** AI model integration (Claude / OpenAI API)
- **Phase 6:** Scheduled automation and GitHub Actions
- **Phase 7:** Generalization to other traditional industries
- **Phase 8:** SME-friendly onboarding and non-engineer templates

---

## 8. Suggested Answers for the Application Form

### Describe your role: are you a primary or core maintainer?

> I am the primary maintainer and creator of this project. I designed and built the initial research workflow, Python implementation, and documentation. I am responsible for all aspects of the project at this stage, and I am building toward a community of contributors from SME and traditional industry backgrounds.

### Why is this repository eligible?

> This is an open-source project (MIT License) focused on making AI-assisted research workflows accessible to non-engineer business users in traditional industries. The project is publicly available on GitHub and is designed to be used, adapted, and contributed to by the SME community. It addresses a real gap: many SMEs want to adopt AI-assisted workflows but lack the engineering resources to build or maintain such tools themselves.

### How will you use API credits?

> I will use API credits to improve the tool's OSS maintenance workflows (issue triage, PR review, documentation improvement) and to prototype AI-assisted features within the research workflow itself — specifically AI-assisted source auditing, insight generation, and fact/assumption separation. The goal is to make the tool more useful for non-engineer SME users while maintaining the human-in-the-loop design principle.

### Anything else you want OpenAI to know?

> This project focuses on a specific underserved segment: non-engineer business users at SMEs in traditional industries such as paint, coatings, anticorrosion, and infrastructure maintenance. AI adoption in these industries is slower than in software-first sectors, partly because accessible tools are lacking. This project aims to make structured, source-audited AI research workflows available to people who are not engineers but still need to understand markets, competitors, and AI adoption opportunities.
>
> The project is honest about its early-stage status. I am not claiming it is widely used or production-ready. I am claiming that it addresses a real problem — AI adoption support for non-engineer SME staff — and that OpenAI's resources would meaningfully accelerate the roadmap.
>
> I am committed to maintaining this project as open source, improving documentation for non-technical users, and building the tool toward genuine usefulness for traditional industry SMEs.

---

## Key Messages for the Application

Use these phrases in the application where appropriate:

- "early-stage open-source tool"
- "non-engineer friendly"
- "SME-focused"
- "human-in-the-loop"
- "source-audited research workflow"
- "AI adoption opportunity discovery"
- "practical research assistant"
- "traditional industry AI adoption"
- "public-source research assistant"

Avoid these phrases:

- "enterprise-grade"
- "fully automated intelligence platform"
- "replaces consultants"
- "guarantees accurate research"
- "widely used"
- "industry standard"
