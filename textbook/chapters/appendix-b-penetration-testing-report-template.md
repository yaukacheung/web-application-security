# Appendix B: Penetration Testing Finding and Report Template

Use this template for weekly lab evidence notes, practical exams, and the capstone penetration testing report.

---

## B.1 Engagement Header and Scope Statement

- **Author / Student Name:**
- **Date:**
- **Target Application & Container Tag:** (e.g., `bkimminich/juice-shop:latest` at `http://localhost:3000`)
- **Written Scope:** State explicitly what host/port is in scope, what methods are permitted, and what systems are excluded.
- **Tools Used:** (e.g., Browser DevTools, OWASP ZAP, `curl`)

## B.2 Executive Summary (Capstone / Full Report)

Write 1–2 concise paragraphs summarizing:

- What was assessed and under what authorization boundaries.
- Overall risk posture and systemic themes observed.
- Highest-priority remediation actions.

## B.3 Finding Template (Repeat for Each Validated Finding)

### Finding [ID]: [Concise Title Naming Weakness and Location]

- **Severity:** Critical / High / Medium / Low / Informational
- **Affected Asset:** `METHOD /path` (and parameter/header name)
- **Scope Confirmation:** Confirmed inside written scope (`http://localhost:<port>`).
- **Description:** Plain-language explanation of the failed security assumption and trust boundary.
- **Reproduction Steps:**
  1. Step 1 (exact preconditions, e.g., authenticated as User A).
  2. Step 2 (exact request or action).
  3. Step 3 (observed response proving the flaw).
- **Evidence:** Minimal HTTP request/response snippet or targeted screenshot with unrelated tokens/PII redacted.
- **Impact:** Concrete effect on confidentiality, integrity, or availability.
- **Remediation:** Specific server-side or configuration fix, naming the exact control location.
- **Regression Test Recommendation:** Automated test case to verify the fix and prevent recurrence.

## B.4 Remediation Roadmap Table

| Priority Window | Finding ID(s) | Action | Owner / Layer |
| --- | --- | --- | --- |
| Immediate (0–7 days) | | | |
| Short-term (30 days) | | | |
| Long-term (60–90 days) | | | |
