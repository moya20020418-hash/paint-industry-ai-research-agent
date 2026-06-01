# Roadmap

This is an early-stage open-source project. The roadmap below reflects the planned direction, not a committed delivery schedule.

---

## Phase 1: MVP Research Workflow (Current)

- [x] Research topic configuration (`config/topics.json`)
- [x] Research note input (`inputs/`)
- [x] Structured Markdown report generation (`reports/`)
- [x] Fact / assumption / insight three-layer separation
- [x] Source reliability auditing framework (manual)
- [x] Numerical claim auditing framework (manual)
- [x] Multi-step research workflow definition (`workflows/`)
- [x] Agent and skill definitions (`agents/`, `skills/`)

---

## Phase 2: Web Source Collection (Current)

- [x] Web text collection from configured URLs (`src/web_collector.py`)
- [x] `robots.txt` compliance
- [x] Collection result saved as Markdown input
- [ ] Improved error handling and retry logic
- [ ] Support for additional content types (JSON, RSS)

---

## Phase 3: Paint Industry AI Opportunity Reports

- [ ] AI adoption opportunity identification section in reports (Sections 11-16 are currently generated as manual-fill stubs — upgrade to AI-assisted content)
- [ ] Paint and coatings industry-specific research templates
- [ ] Anticorrosion and infrastructure maintenance topic templates
- [ ] Competitor AI adoption analysis section
- [ ] Non-engineer-friendly report output format

---

## Phase 4: PDF and Government Statistics Support

- [ ] PDF text extraction (for government statistics, industry reports)
- [ ] Structured data extraction from tables
- [ ] Automatic source ranking for government / public documents
- [ ] Support for Japanese government statistics (e-Stat, MLIT)

---

## Phase 5: AI Model Integration

- [ ] Claude API integration for automated analysis
- [ ] OpenAI API integration option
- [ ] AI-assisted source auditing
- [ ] AI-assisted insight generation with source tracing
- [ ] Hallucination prevention safeguards for AI-generated content

---

## Phase 6: Scheduled Automation and GitHub Actions

- [ ] Scheduled weekly report generation
- [ ] GitHub Actions workflow for automated collection
- [ ] Report diff tracking (what changed week-over-week)
- [ ] Automated source freshness checks

---

## Phase 7: Generalization to Other Traditional Industries

- [ ] Construction and civil engineering templates
- [ ] Food manufacturing templates
- [ ] Logistics and supply chain templates
- [ ] Generic SME industry template framework
- [ ] Multi-language support (English / Japanese)

---

## Phase 8: SME-Friendly Onboarding and Non-Engineer Templates

- [ ] GUI setup wizard (no command line required)
- [ ] Pre-configured industry starter packs
- [ ] Step-by-step video documentation
- [ ] Non-engineer onboarding guide
- [ ] One-click report generation for common SME research tasks
- [ ] Template library for internal proposals and presentations

---

## Contributing to the Roadmap

If you have suggestions for the roadmap — especially for SME use cases or non-engineer improvements — please open a GitHub Issue with the label `roadmap`.
