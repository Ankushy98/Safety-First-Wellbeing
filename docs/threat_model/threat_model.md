# Threat Model
## Safety-First Wellbeing Conversational Agent

### 1. Purpose

This threat model identifies security, privacy and safety risks
associated with the wellbeing AI prototype.

The goal is to prevent unauthorized access, unsafe automated
actions, sensitive-data exposure and approval bypass.

---

## 2. Assets

Important system assets include:

- User journal data
- Mood information
- Sentiment results
- Risk assessments
- Human referral records
- Privacy settings
- Audit logs
- Admin credentials/API key
- System configuration

---

## 3. Threats and Controls

| Threat | Risk | Control |
|---|---|---|
| Unauthorized admin access | High | Admin API key |
| Wrong admin credentials | High | Authentication check |
| Unauthorized tool execution | High | Tool allow-list |
| Referral without human approval | High | Approval gate |
| Invalid referral decision | Medium | Input validation |
| Sensitive journal exposure | High | Privacy controls |
| Unsafe automated action | High | Human governance |
| Audit trail manipulation | High | Controlled audit workflow |
| Unexpected input | Medium | Input validation |
| Unsupported tool request | High | Tool policy |

---

## 4. Tool Security

The agent can only request tools that are explicitly included
in the tool allow-list.

Allowed tools:

- get_user_mood
- get_recent_journal
- generate_support_message
- create_referral

The `create_referral` operation requires human approval.

Unknown tools are blocked.

---

## 5. Authentication

Administrative endpoints require an admin API key.

Requests without a valid API key are rejected.

Security testing includes:

- Missing API key
- Incorrect API key
- Valid API key

---

## 6. Human Approval

Sensitive referral actions cannot be executed automatically.

Workflow:

Agent
→ Tool Policy
→ Approval Gate
→ Human Decision
→ Action
→ Audit Log

This prevents the AI agent from independently performing
sensitive referral actions.

---

## 7. Privacy

The system provides privacy controls for:

- Journal storage
- Sentiment processing
- Optional facial-expression research
- Sharing information with support staff

Only required information should be accessed by system components.

---

## 8. Input Validation

The system validates user-provided values.

Example:

Mood must be between 1 and 5.

Invalid values are rejected by the API.

---

## 9. Auditability

Important system events are recorded in audit logs.

Examples:

- Journal analyzed
- Tool executed
- Tool blocked
- Approval required
- Human referral reviewed

Audit logs support traceability of sensitive actions.

---

## 10. Residual Risks

The prototype still has limitations.

Examples:

- Simple authentication mechanism
- SQLite development database
- Basic sentiment model
- Prototype-level risk rules
- Limited evaluation dataset
- No production deployment security review

A production system would require stronger authentication,
encryption, access control, monitoring and expert security review.

---

## 11. Security Testing Evidence

The prototype was tested for:

- Missing admin credentials
- Invalid admin credentials
- Unauthorized tools
- Approval bypass
- Invalid referral decisions
- Edge-case inputs

The tests demonstrated that unauthorized operations were blocked
and sensitive tool execution required approval.