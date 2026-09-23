# System Architecture
## Safety-First Wellbeing Conversational Agent

### 1. High-Level Architecture

The system follows a human-governed, safety-first architecture.

User
↓
Web Frontend
↓
FastAPI Backend
↓
Journal + Sentiment Processing
↓
Safety Rule Engine
↓
Risk Triage
↓
Human-Governed Agent
↓
Tool Policy
↓
Approval Gate
↓
Human Referral / Support Action
↓
Audit Log
↓
Monitoring and Evaluation

---

## 2. Main Components

### Web Frontend

Provides the user interface for:

- Entering mood
- Writing journal entries
- Viewing journal history
- Viewing wellbeing summaries
- Managing privacy settings

---

### FastAPI Backend

The backend provides API endpoints for:

- Journal processing
- Privacy settings
- Human referrals
- Administrative operations
- Audit logs

---

### Journal Module

The journal module accepts:

- User ID
- Mood score
- Optional journal text

Mood is validated between 1 and 5.

---

### Sentiment Module

The sentiment module analyzes optional journal text.

Possible outputs:

- Positive
- Negative
- Neutral

The prototype uses TextBlob.

---

### Safety Rule Engine

A deterministic safety rule is executed independently
from the sentiment model.

If a configured safety signal is detected, the workflow
can move to HIGH risk.

This provides a safety layer outside the AI model.

---

### Risk Triage

Risk triage combines:

- Mood
- Sentiment
- Safety rule result

The workflow produces:

LOW
MEDIUM
HIGH

These are workflow categories and are not medical diagnoses.

---

### Human-Governed Agent

The agent does not have unrestricted system access.

It can only request tools defined by the tool policy.

---

### Tool Allow-list

Allowed tools include:

- get_user_mood
- get_recent_journal
- generate_support_message
- create_referral

Unknown tools are blocked.

---

### Approval Gate

Sensitive operations require human approval.

Example:

create_referral
↓
Approval Required
↓
Human Decision
↓
Approved / Rejected

---

### Human Referral

HIGH-risk workflow cases can create a referral
for human support staff.

The referral remains pending until reviewed.

---

### Audit Logging

Important actions are recorded.

Examples:

- Journal analyzed
- Tool executed
- Tool blocked
- Approval required
- Human referral reviewed

---

### Privacy Layer

Users can control:

- Journal storage
- Sentiment processing
- Optional facial-expression research
- Sharing with support staff

---

## 3. Data Flow

User submits journal
↓
Input validation
↓
Privacy settings checked
↓
Sentiment analysis
↓
Safety rule evaluation
↓
Risk triage
↓
Decision workflow
↓
Optional human referral
↓
Audit logging

---

## 4. Human-in-the-Loop Design

Normal information request:

User
↓
Agent
↓
Allowed Tool
↓
Result

Sensitive action:

User
↓
Agent
↓
Allowed Tool
↓
Policy Check
↓
Approval Gate
↓
Human Approval
↓
Action
↓
Audit Log

This design limits autonomous execution of sensitive actions.

---

## 5. Safety Boundary

The system is designed as a wellbeing support prototype.

It does not:

- Diagnose medical conditions
- Replace professional care
- Make unrestricted autonomous decisions
- Execute unauthorized tools
- Automatically perform sensitive referral actions
  without the required approval

---

## 6. Technology Stack

Backend:
- Python
- FastAPI
- SQLAlchemy
- SQLite

AI/NLP:
- TextBlob
- Python-based rule logic

Frontend:
- HTML
- CSS
- JavaScript
- Jinja2 templates

Security:
- API-key authentication
- Tool allow-list
- Approval gate
- Input validation

Evaluation:
- scikit-learn
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Robustness tests

Development:
- Git
- Virtual environment
- PowerShell