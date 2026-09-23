# Safety-First Wellbeing Conversational Agent
## Model and System Card

### 1. System Overview

The Safety-First Wellbeing Conversational Agent is a safety-oriented
wellbeing support prototype.

The system processes:
- User self-report mood
- Optional journal text
- Text sentiment
- Safety rule signals

The system then performs workflow-based risk triage into:
- LOW
- MEDIUM
- HIGH

The risk level is a workflow classification and is not a medical diagnosis.

---

### 2. Objective

The objective is to demonstrate a safety-first AI workflow where
automated analysis is combined with deterministic safety rules,
restricted tools, human approval and audit logging.

---

### 3. Main Components

The system contains:

1. Journal Module
2. Sentiment Analysis Module
3. Crisis Safety Rule
4. Risk Triage
5. Human-Governed AI Agent
6. Tool Allow-list
7. Approval Gate
8. Human Referral Workflow
9. Privacy Controls
10. Audit Logging
11. Evaluation and Robustness Tests

---

### 4. Sentiment Analysis

The prototype uses TextBlob sentiment analysis.

Possible outputs:

- Positive
- Negative
- Neutral

The sentiment output is used as one input to the risk workflow.

---

### 5. Risk Triage

The prototype uses three workflow categories:

LOW:
Normal/low-risk input.

MEDIUM:
Low mood combined with negative sentiment.

HIGH:
Safety rule signal detected.

These categories are intended for workflow routing and
must not be interpreted as clinical diagnoses.

---

### 6. Human Governance

Sensitive actions require human approval.

Example:

User
→ AI Agent
→ Tool Policy
→ Approval Gate
→ Human Approval
→ Action
→ Audit Log

The system does not allow the agent to independently execute
restricted referral actions.

---

### 7. Tool Policy

Allowed tools include:

- get_user_mood
- get_recent_journal
- generate_support_message
- create_referral

The `create_referral` tool requires human approval.

Unauthorized tools are blocked.

---

### 8. Privacy

The prototype provides controls for:

- Journal storage
- Sentiment analysis
- Facial-expression research module
- Sharing with support staff

The facial-expression module is optional and is not used
as a standalone diagnostic signal.

---

### 9. Safety Limitations

The system is a prototype and does not replace:

- Doctors
- Therapists
- Emergency services
- Human support staff

Automated outputs should not be treated as medical diagnoses.

The system may produce incorrect sentiment or risk classifications.

Human review is required for sensitive referral decisions.

---

### 10. Evaluation

The system includes evaluation for:

- Baseline comparison
- Safety classification
- Sentiment metrics
- Robustness
- Security
- Tool authorization
- Human approval
- Auditability

Metrics include:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

### 11. Security Testing

The prototype was tested for:

- Missing admin authentication
- Invalid admin credentials
- Unauthorized tools
- Approval bypass
- Invalid referral decisions
- Edge-case inputs

Unauthorized actions are blocked and important tool events
are recorded in audit logs.

---

### 12. Intended Use

This prototype is intended for:

- Academic demonstration
- Safety-oriented AI research
- Human-in-the-loop workflow demonstration
- Evaluation of agent governance mechanisms

It is not intended for autonomous clinical decision-making.

---

### 13. Known Limitations

The current prototype uses relatively simple sentiment and
risk rules.

Real-world deployment would require:

- Larger validated datasets
- Expert-reviewed evaluation
- Stronger authentication
- More comprehensive security testing
- Privacy/security review
- Human-support operational procedures
- Further model validation

---

### 14. Version

Prototype Version: 1.0

Status: Academic Prototype