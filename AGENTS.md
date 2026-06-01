# AGENTS.md

## Project Name

Paint Industry AI Research Agent
塗料業界AI活用リサーチエージェント

## Core Positioning

This is an early-stage open-source project for helping SMEs and non-engineer business users adopt AI-assisted research workflows.

The project focuses on traditional B2B industries such as paint, coatings, anticorrosion, manufacturing, and infrastructure maintenance.

The maintainer is also a non-engineer working in an SME. This is an important part of the project's identity: it is built by a non-engineer working in an SME, for non-engineer SME workers.

This project should not be described as an enterprise-grade, fully automated, or production-ready intelligence platform. It is a practical, human-in-the-loop, public-source research assistant.

## Target Users

The main target users are:

* Small and medium-sized enterprises
* Non-engineer business users
* Paint and coatings industry professionals
* Anticorrosion and infrastructure maintenance companies
* Manufacturing SMEs
* Sales, planning, marketing, operations, and technical sales staff
* Business users who want to adopt AI but do not have in-house engineering or data science teams

## Contributor Assumption

Assume that some contributors may also be non-engineers working in SMEs.

Do not treat code contributions as the only valuable contributions.

Important contribution types include:

* Documentation improvements
* Beginner-friendly setup guides
* Sample inputs and reports
* SME use case examples
* Safer workflow suggestions
* Source auditing improvements
* Non-engineer onboarding improvements
* Issue reports written by non-engineer users

## Value Hypothesis

Traditional B2B industries such as paint, coatings, anticorrosion, manufacturing, and infrastructure maintenance may lack accessible AI adoption workflows for SMEs and non-engineer business users.

This project is an early-stage open-source attempt to help fill that gap.

Do not claim that the entire paint industry or all SMEs are not digitized.

Avoid unsupported claims such as:

* The paint industry has no AI adoption.
* DX has not progressed at all.
* This project is industry standard.
* This project replaces consultants.
* This project guarantees accurate research.

Use careful language such as:

* may lack accessible workflows
* may face adoption barriers
* aims to support
* helps users organize public information
* human review is required
* early-stage open-source tool

## Current Purpose

The current purpose is to support:

* Market research
* Competitor analysis
* Industry trend research
* Public web source collection
* Source reliability auditing
* Numerical claim checking
* AI adoption opportunity discovery
* Internal proposal drafting
* SME-friendly research workflows

## Future Expansion

In the future, this project may expand beyond market research into:

* Financial analysis
* Company analysis
* Management analysis
* Industry comparison
* Competitor comparison
* Credit or investment decision support
* SME-focused management support reports
* Internal proposal and AI adoption planning

However, until the OpenAI Codex for OSS application is submitted, prioritize OSS readiness and application quality over major feature expansion.

## Safety and API Key Policy

This project should avoid requiring users or contributors to directly handle API keys.

Important safety principles:

* Do not ask users to paste API keys into source code.
* Do not ask users to put raw API keys into public config files.
* Do not commit real `.env` files.
* If environment variables are used, provide only `.env.example`.
* Keep `.env`, `secrets.json`, `credentials.json`, logs, reports, and collected web data out of Git.
* Prefer safe authentication methods such as GitHub Secrets, environment variables, OAuth, or secure local configuration.
* Keep the initial tool usable without external APIs whenever possible.
* API integration should be treated as a future optional feature with clear safety guidance.

## OpenAI Codex for OSS Application Positioning

For the OpenAI Codex for OSS application, describe the project as:

* early-stage open-source project
* SME-focused
* non-engineer friendly
* human-in-the-loop
* source-audited research workflow
* traditional industry AI adoption
* AI adoption opportunity discovery
* public-source research assistant

Do not say:

* I want ChatGPT Pro for free.
* This is already widely used.
* This is an industry standard.
* This replaces experts or consultants.
* This guarantees accurate research.

Instead, say:

* Codex would help improve OSS maintenance workflows.
* Codex would support issue triage, PR review, documentation improvements, onboarding, and safer contribution workflows.
* Codex would help make the project more accessible to non-engineer contributors.
* API credits would be used to test and improve AI-assisted research workflows safely.

## Core Application Message

Use this idea in application materials:

This project is built by a non-engineer working in an SME, for non-engineer workers in SMEs. It focuses on traditional B2B industries such as paint, coatings, anticorrosion, manufacturing, and infrastructure maintenance, where AI and DX adoption may be difficult due to limited engineering resources, limited budgets, and lack of dedicated data science teams. The goal is not to replace experts or consultants, but to provide a practical, human-in-the-loop research workflow that helps SME workers collect public information, audit sources, check numerical claims, and identify realistic AI adoption opportunities.

## Review Rules for Codex

When reviewing this repository:

1. Check whether README and docs are understandable for non-engineers.
2. Check whether claims are careful and not exaggerated.
3. Check whether implementation and documentation are consistent.
4. Check whether dependency instructions are accurate.
5. Check whether Windows users can follow the setup.
6. Check whether secrets, API keys, logs, reports, and collected web data are excluded from Git.
7. Check whether generated reports remain human-in-the-loop.
8. Check whether Codex for OSS application wording avoids overclaiming.
9. Prefer small, reviewable changes over large rewrites.
10. Do not add major new features unless explicitly asked.

## Work Priority

Until the OpenAI Codex for OSS application is submitted, prioritize:

1. GitHub repository quality
2. README clarity
3. Roadmap clarity
4. Security and privacy guidance
5. Non-engineer onboarding
6. Codex for OSS application wording
7. Initial GitHub Issues
8. Avoiding overclaiming
9. Avoiding secret/API key exposure
10. Keeping the project easy to understand

Do not prioritize major feature expansion until the application is submitted.

## Output Style

When reporting findings, use this format:

* Overall assessment
* Major strengths
* Major risks
* Files that need changes
* Suggested changes
* Risk level
* Whether to edit now or defer
* Next recommended action

When proposing changes, do not immediately make large edits. First explain:

* Problem
* Why it matters
* Suggested change
* Files to edit
* Risk level

Then wait for approval unless the user explicitly asks you to edit.
