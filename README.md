\# Safety-First Wellbeing Conversational Agent



\## Overview



This project is a safety-first wellbeing conversational agent designed as an academic prototype.



The system combines self-report journaling, optional sentiment analysis, risk triage, deterministic safety rules, human referral, privacy controls, tool restrictions, approval gates, audit logging, and evaluation.



The system is designed to support wellbeing workflows and is not a medical diagnosis or treatment system.



\---



\## Key Features



\- Self-report journal

\- Mood tracking

\- Optional text sentiment analysis

\- Optional facial-expression research module

\- Crisis safety rule

\- LOW / MEDIUM / HIGH risk triage

\- Human referral workflow

\- Human-in-the-loop approval

\- Tool allow-list

\- Approval gates for sensitive actions

\- Privacy controls

\- Audit logging

\- Admin dashboard

\- User dashboard

\- Security and robustness testing

\- Evaluation metrics

\- Threat model

\- Model card



\---



\## System Architecture



```text

USER

&#x20; |

&#x20; v

Web Frontend

&#x20; |

&#x20; v

FastAPI Backend

&#x20; |

&#x20; +---- Journal

&#x20; |

&#x20; +---- Sentiment Analysis

&#x20; |

&#x20; +---- Optional Expression Module

&#x20; |

&#x20; v

Crisis Safety Rule

&#x20; |

&#x20; v

Risk Triage

&#x20; |

&#x20; v

Human-Governed AI Agent

&#x20; |

&#x20; v

Tool Allow-list

&#x20; |

&#x20; v

Approval Gate

&#x20; |

&#x20; v

Human Referral

&#x20; |

&#x20; v

Audit Logs

&#x20; |

&#x20; v

Monitoring / Evaluation

