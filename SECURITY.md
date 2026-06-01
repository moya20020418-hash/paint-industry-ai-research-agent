# Security Policy

## Responsible Use

This project is a public-source research assistant tool. Please follow these guidelines to use it safely and responsibly.

## Do Not Commit

- **API keys or tokens** — Never commit `.env` files, API credentials, or authentication tokens to the repository.
- **Private company data** — Do not include internal business documents, pricing data, customer lists, or other confidential information in `config/`, `inputs/`, or `examples/`.
- **Customer data or personal information** — Do not include names, contact details, or other personally identifiable information (PII) in any committed files.
- **Confidential source URLs** — If a URL requires authentication or leads to a private resource, do not commit it to `config/sources.json`.

## Web Collection Guidelines

- **Respect `robots.txt`** — The default setting `respect_robots_txt: true` must not be changed to `false`.
- **Do not scrape aggressively** — Keep `min_interval_sec` at 2 seconds or higher. Do not reduce access intervals to scrape sites rapidly.
- **Respect site terms of service** — Only collect from sources where web scraping is permitted.
- **Collected text is not fact-checked** — Web-collected text requires human review before business use.

## Generated Reports

- **Human review is required** — Generated reports are templates and research aids. They do not guarantee factual accuracy.
- **Do not share unreviewed reports externally** — Always review generated reports before business use or distribution.
- **Do not use confidential internal documents as inputs** — Only use publicly available sources as inputs to the tool.

## Sample Data

- All files in `examples/` must use public or synthetic data only.
- No real company internal data, pricing, or customer information in examples.

## Reporting Security Issues

If you discover a security issue in this project (such as a pattern that could leak credentials or expose private data), please:

1. Open a GitHub Issue with the label `security`.
2. Do not include sensitive data in the issue.
3. Describe the problem and how it could be exploited.

This is an early-stage open-source project. We will respond to security reports as quickly as possible.
