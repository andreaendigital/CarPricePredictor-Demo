---
title: CI/CD Pipeline
description: Enterprise-grade 27-step complete DevOps workflow with JIRA integration
tags:
  - CI/CD
  - GitHub Actions
  - Docker
  - JIRA
  - Enterprise DevOps
---

# 🔄 Enterprise DevOps Workflow - 12-Step Pipeline Flow

```mermaid
flowchart TD
    A[📋 Step 1: JIRA Ticket] --> B[Step 2: Branch Creation]
    B --> C[Step 3: Development]
    C --> D[Step 4: Local Testing]
    D --> E[Step 5: Git Commit]
    E --> F[Step 6: Git Push]
    F --> G[Step 7: Pull Request]
    G --> H[Step 8: Code Review]
    H --> I[Step 9: GitHub Trigger]
    I --> J[Container Image Tagging]
    J --> L[Backend: SCRUM-95, pr-142, latest]
    J --> M[Frontend: SCRUM-95, pr-142, latest]


    classDef planning fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef development fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    classDef review fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef cicd fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef build fill:#fce4ec,stroke:#c2185b,stroke-width:2px

    class A planning
    class B,C,D,E,F,G development
    class H review
    class I,J cicd
    class L,M build
```




---

## Step 1: JIRA Ticket Creation

<strong>Product Owner creates user story</strong>

![Step 1](../assets/images/1.jpeg)

![Step 2](../assets/images/2.jpeg)


---

## Step 2: Ticket Assignment

<strong>Developer picks up ticket</strong>

![Step 3](../assets/images/3.jpeg)

---

## Step 3: Branch Creation

![Step 4](../assets/images/4.jpeg)

---

## Step 4: Developer Coding

![Step 5](../assets/images/5.jpeg)


---

## Step 5: Local Testing

![Step 6](../assets/images/6.png)


---

## Step 6: Pre-commit Hooks

![Step 7](../assets/images/7.png)

<strong>Automated quality checks</strong>
- Code formatting (Black)
- Linting (Flake8)

---

## Step 7: Git Commit - Git Push

![Step 8](../assets/images/8.jpeg)


---

## Step 8: Pull Request


<div style="display: flex; gap: 20px; margin: 20px 0; align-items: flex-start;">
<div style="flex: 1; background: #f3e5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #7b1fa2;">

<strong>Create pull request</strong>
- Link to JIRA ticket
- Describe changes
- Add screenshots
- Request reviewers

</div>
<div style="flex: 1; background: #0d1117; padding: 15px; border-radius: 8px; color: #e6edf3; font-size: 12px;">

<h3 style="color: #f0f6fc; margin-top: 0;">Pull Request</h3>
<h4 style="color: #7d8590; margin: 12px 0 6px 0;">Summary</h4>
<p style="margin: 4px 0;"><strong style="color: #f0f6fc;">SCRUM Ticket:</strong> <code style="background: #21262d; padding: 2px 4px; border-radius: 3px; color: #f85149;">SCRUM-XXX</code></p>
<p style="margin: 4px 0;"><strong style="color: #f0f6fc;">Type:</strong></p>
<div style="margin: 2px 0;">☐ Frontend</div>
<div style="margin: 2px 0;">☐ Backend</div>
<div style="margin: 2px 0;">☐ Bug Fix</div>
<div style="margin: 2px 0;">☐ Enhancement</div>

<h5 style="color: #7d8590; margin: 8px 0 4px 0;">What does this PR do?</h5>
<p style="color: #7d8590; margin: 2px 0; font-style: italic;">&lt;!-- Describe your changes here --&gt;</p>

<h5 style="color: #7d8590; margin: 8px 0 4px 0;">Related Issues</h5>
<p style="color: #7d8590; margin: 2px 0; font-style: italic;">&lt;!-- Link related issues: Closes #XXX, Fixes #XXX --&gt;</p>

<hr style="border: none; border-top: 1px solid #21262d; margin: 12px 0;">

<h4 style="color: #7d8590; margin: 12px 0 6px 0;">Testing</h4>
<h5 style="color: #7d8590; margin: 8px 0 4px 0;">Quick Test Commands</h5>
<pre style="background: #161b22; padding: 8px; border-radius: 4px; margin: 4px 0; font-size: 11px; border: 1px solid #30363d;"># Backend Test
python backend/app.py  # Port 5002
# Frontend Test
python frontend/app.py # Port 3000</pre>

<h5 style="color: #7d8590; margin: 8px 0 4px 0;">Testing Status</h5>
<div style="margin: 2px 0;">☐ Backend API tested (Port 5002)</div>
<div style="margin: 2px 0;">☐ Frontend app tested (Port 3000)</div>
<div style="margin: 2px 0;">☐ Integration working</div>
<div style="margin: 2px 0;">☐ Manual testing completed</div>

<h4 style="color: #7d8590; margin: 12px 0 6px 0;">Technical Changes</h4>
<h5 style="color: #7d8590; margin: 8px 0 4px 0;">Backend Changes</h5>
<div style="margin: 2px 0;">☐ New API endpoints added</div>
<div style="margin: 2px 0;">☐ ML prediction logic updated</div>
<div style="margin: 2px 0;">☐ Error handling improved</div>

<h5 style="color: #7d8590; margin: 8px 0 4px 0;">Frontend Changes</h5>
<div style="margin: 2px 0;">☐ UI components updated</div>
<div style="margin: 2px 0;">☐ CSS styling improvements</div>
<div style="margin: 2px 0;">☐ API integration updated</div>

<hr style="border: none; border-top: 1px solid #21262d; margin: 12px 0;">

<h4 style="color: #7d8590; margin: 12px 0 6px 0;">Screenshots</h4>
<details style="margin: 8px 0;">
<summary style="color: #58a6ff; cursor: pointer;">Click to view screenshots</summary>
<h5 style="color: #7d8590; margin: 6px 0 2px 0;">Before Changes</h5>
<p style="color: #7d8590; margin: 2px 0; font-style: italic;">&lt;!-- Screenshot here --&gt;</p>
<h5 style="color: #7d8590; margin: 6px 0 2px 0;">After Changes</h5>
<p style="color: #7d8590; margin: 2px 0; font-style: italic;">&lt;!-- Screenshot here --&gt;</p>
</details>

<hr style="border: none; border-top: 1px solid #21262d; margin: 12px 0;">

<h4 style="color: #7d8590; margin: 12px 0 6px 0;">Pre-merge Checklist</h4>
<div style="margin: 2px 0;">☐ Code reviewed</div>
<div style="margin: 2px 0;">☐ Services tested locally</div>
<div style="margin: 2px 0;">☐ No breaking changes</div>
<div style="margin: 2px 0;">☐ Ready for deployment</div>

<p style="margin: 8px 0 4px 0;"><strong style="color: #f0f6fc;">Reviewer:</strong> @&lt;!-- username --&gt;</p>

<h5 style="color: #7d8590; margin: 8px 0 4px 0;">Test URLs</h5>
<table style="width: 100%; border-collapse: collapse; margin: 4px 0; font-size: 11px;">
<tr style="background: #21262d;">
<th style="border: 1px solid #30363d; padding: 4px 6px; color: #f0f6fc;">Service</th>
<th style="border: 1px solid #30363d; padding: 4px 6px; color: #f0f6fc;">URL</th>
<th style="border: 1px solid #30363d; padding: 4px 6px; color: #f0f6fc;">Status</th>
</tr>
<tr>
<td style="border: 1px solid #30363d; padding: 4px 6px;">Backend API</td>
<td style="border: 1px solid #30363d; padding: 4px 6px;"><code style="background: #21262d; padding: 1px 3px; border-radius: 2px; color: #f85149;">http://localhost:5002</code></td>
<td style="border: 1px solid #30363d; padding: 4px 6px;">☐ Tested</td>
</tr>
<tr>
<td style="border: 1px solid #30363d; padding: 4px 6px;">Frontend App</td>
<td style="border: 1px solid #30363d; padding: 4px 6px;"><code style="background: #21262d; padding: 1px 3px; border-radius: 2px; color: #f85149;">http://localhost:3000</code></td>
<td style="border: 1px solid #30363d; padding: 4px 6px;">☐ Tested</td>
</tr>
</table>

</div>
</div>

---

## Step 9: Code Review

![Step 9](../assets/images/CodeReview.png)

---

## Step 10: GitHub Trigger

<div style="display: flex; gap: 20px; margin: 20px 0; align-items: flex-start;">
<div style="flex: 1; background: #f3e5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #7b1fa2;">

<strong>CI/CD Pipeline Activation</strong>

<br>

- Event detection
- Workflow triggering
- Environment setup
- Pipeline initialization

<br>

<strong>Container Image Tagging Examples</strong>

<br>

<strong>Backend Tags:</strong>
```
ghcr.io/user/carpriceprediction-backend:SCRUM-95
ghcr.io/user/carpriceprediction-backend:pr-142
ghcr.io/user/carpriceprediction-backend:latest
```

<br>

<strong>Frontend Tags:</strong>
```
ghcr.io/user/carpriceprediction-frontend:SCRUM-95
ghcr.io/user/carpriceprediction-frontend:pr-142
ghcr.io/user/carpriceprediction-frontend:latest
```

<strong>Registry:</strong> ghcr.io | <strong>Platforms:</strong> linux/amd64, linux/arm64

</div>
<div style="flex: 1; background: #f5f5f5; padding: 15px; border-radius: 8px; font-family: monospace;">

```yaml
🔍 GitHub Actions Trigger

name: Car Price Prediction CI/CD Pipeline

on:
  push:
    branches: [ main, develop, 'feature/*', 'SCRUM-*' ]
  pull_request:
    branches: [ main, develop ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}
  PYTHON_VERSION: '3.11'

permissions:
  contents: read
  packages: write
  security-events: write

jobs:
  code-quality:
    name: Code Quality Validation
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.11']

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
    - name: Configure Python
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    - name: Execute quality checks
      run: |
        black --check --diff .
        flake8 .

Trigger Status: Pipeline Started
Run ID: #1234567890
```

</div>
</div>

---

## Step 11: Container Image Tagging Examples

![Step 11](../assets/images/11.png)

## Step 12: Full CI/CD Pipeline Actions Documentation

![Step 12](../assets/images/12.png)
