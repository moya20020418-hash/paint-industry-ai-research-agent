# Contributing to Paint Industry AI Research Agent

Thank you for your interest in contributing. This is an early-stage open-source project, and all contributions are welcome — whether you are an engineer, a business user, or someone working in a traditional industry like paint, coatings, or manufacturing.

## Who Can Contribute

- Engineers who want to improve the Python codebase
- Business users who want to improve documentation or add industry-specific templates
- Non-engineers who spot confusing instructions or want to add use cases
- Anyone who uses the tool and has feedback

**Non-engineer contributions are especially valued.** If you found the documentation confusing, or if a step did not work as described, please open an Issue. Your experience as a non-technical user directly improves the tool for others.

---

## How to Contribute

### 1. Report a Bug or Issue

Open a GitHub Issue and include:

- What you tried to do
- What happened
- What you expected to happen
- Your operating system and Python version

### 2. Suggest an Improvement

Open a GitHub Issue with the label `enhancement` and describe:

- What you want to change and why
- Who it helps (e.g., non-engineer users, SME staff, specific industry)

### 3. Submit a Pull Request

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test that `python src/main.py` still runs correctly
5. Open a Pull Request with a description of what you changed and why

---

## Contribution Areas

### Documentation Improvements

- Improving README clarity for non-engineer users
- Adding step-by-step guides for specific operating systems
- Writing FAQs based on real usage questions
- Translating documentation (Japanese and English)

### Industry Templates

- Adding `config/topics.json` examples for new industries (construction, infrastructure, food manufacturing, etc.)
- Adding `examples/` templates for specific research workflows
- Writing workflow guides for non-engineer staff in traditional industries

### Source Configuration Examples

- Adding `examples/sample_sources.json` entries for government statistics, industry associations, or publicly available market data
- Documenting reliable public sources for specific industries

### Code Improvements

- Improving `src/web_collector.py` for better reliability
- Adding PDF text extraction support
- Improving error messages for non-technical users
- Adding support for new output formats

---

## Source Safety Rules

Before submitting, please verify:

- No API keys or credentials in any file
- No private company data, customer data, or internal documents
- No URLs that require authentication
- No scraping of sites that prohibit it via `robots.txt` or Terms of Service
- All `examples/` content uses public or synthetic data only
- No personally identifiable information (PII)

---

## Pull Request Policy

- Keep Pull Requests focused on one change at a time
- Include a description of what changed and why
- If the change affects `src/`, confirm that `python src/main.py` still runs
- Documentation-only PRs are welcome without code changes

---

## SME-Focused Contributions

This project specifically targets non-engineer business users at small and medium-sized enterprises (SMEs) in traditional industries. Contributions that make the tool more accessible to these users are the highest priority:

- Simpler setup instructions
- Clearer error messages
- Industry-specific research templates
- Non-engineer onboarding guides
- Japanese-language documentation improvements

---

## Questions

If you are unsure about something, open a GitHub Issue and ask. There are no silly questions, especially for non-engineer users contributing for the first time.
