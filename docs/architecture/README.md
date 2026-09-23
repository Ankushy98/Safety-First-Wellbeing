# Safety-First Wellbeing Conversational Agent

## Overview

The Safety-First Wellbeing Conversational Agent is an academic
prototype designed to demonstrate a safety-oriented AI workflow
for wellbeing support.

The system combines user self-report, journal analysis,
sentiment analysis, deterministic safety rules, risk triage,
human approval, referral workflow and audit logging.

The system is not a medical diagnostic system and does not
replace doctors, therapists or professional support.

---

## Key Features

- Self-report mood input
- Journal entry
- Text sentiment analysis
- Deterministic safety rule
- LOW / MEDIUM / HIGH risk triage
- Human-governed AI agent
- Tool allow-list
- Human approval gate
- Human referral workflow
- Privacy controls
- Admin authentication
- Audit logging
- Robustness testing
- Security testing
- Evaluation metrics

---

## System Architecture

```text
User
 |
 v
Web Frontend
 |
 v
FastAPI Backend
 |
 +------------------+
 |                  |
 v                  v
Journal          Sentiment
 |                  |
 +--------+---------+
          |
          v
   Safety Rule Engine
          |
          v
     Risk Triage
          |
          v
 Human-Governed Agent
          |
          v
    Tool Allow-list
          |
          v
    Approval Gate
          |
          v
 Human Referral / Action
          |
          v
      Audit Log
          |
          v
 Monitoring / Evaluation