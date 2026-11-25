---
title: "Web Application Security - Week 11"
author: "Yau Ka Cheung, M.S."
date: "Week 11"
revealOptions:
  transition: slide
  slideNumber: true
  hash: true
  controls: true
  progress: true
  center: false
---

# Web Application Security

## Week 11: SSRF, Deserialization, and Server-Side Abuse

Senior undergraduate course

---

## Today's Outcomes

By the end of today, you should be able to:

- Explain server-side request forgery
- Apply metadata service exposure
- Evaluate unsafe deserialization
- Connect lecture concepts to this week's lab

---

## Where This Week Fits

Last week established foundations.

This week moves into ssrf, deserialization, and server-side abuse.

The lab target is WebGoat and Juice Shop.

---

## Core Security Question

How can we decide whether application behavior is trustworthy?

Today's answer centers on server-side request forgery and metadata service exposure.

---

## Concept 1: Server-side Request Forgery

- Define the moving parts
- Identify who controls each part
- Record assumptions
- Look for boundary crossings

---

## Why It Matters

Backend services may trust requests that originated from vulnerable application code.

A finding is stronger when it explains the broken assumption.

---

## Concept 2: Metadata Service Exposure

Ask:

- What asset is affected?
- Who can reach it?
- What validates the request?
- What evidence would prove failure?

---

## Concept 3: Unsafe Deserialization

Use a repeatable method:

1. Observe normal behavior
2. Change one variable
3. Compare the result
4. Preserve minimal evidence

---

## Threat Actor Lens

Different actors have different access:

- Anonymous visitor
- Registered user
- Privileged user
- Partner service
- Malicious insider

---

## Asset Lens

Common web assets:

- Accounts
- Session tokens
- Personal data
- Business records
- Administrative actions
- Source and configuration

---

## Trust Boundary Lens

Trust boundaries appear between:

- Browser and server
- API and database
- User role and admin role
- Internal service and external request

---

## Attack Surface Lens

Inventory:

- Routes and endpoints
- Parameters
- Headers
- Cookies
- Uploads
- Authentication states
- Third-party calls

---

## Evidence Standard

Good evidence shows:

- Target
- Request or action
- Actual result
- Expected secure result
- Impact on an asset

---

## Tooling Focus

Useful tools this week:

- Browser developer tools
- Intercepting proxy
- Docker Compose
- Markdown notes
- Target documentation

---

## Demonstration Setup

Target: WebGoat and Juice Shop

Task: trace server-side trust boundaries in controlled exercises.

Constraint: stay inside the written scope.

---

## Demonstration Step 1

Establish baseline behavior.

Record the page, request, role, and expected result before changing anything.

---

## Demonstration Step 2

Change one input or condition.

Avoid changing multiple variables at once because evidence becomes harder to interpret.

---

## Demonstration Step 3

Compare results.

A difference is interesting only when it affects security properties such as confidentiality, integrity, or availability.

---

## Common False Positive Pattern

A tool reports a possible issue.

The tester cannot reproduce impact.

The report should say unconfirmed, not proven.

---

## Common False Negative Pattern

The page looks protected.

The underlying endpoint accepts unauthorized or malformed requests.

Always test the server behavior.

---

## Remediation Thinking

Useful remediation is specific:

- Where should the control live?
- What input or action is constrained?
- How can the team test the fix?
- What regression test would catch recurrence?

---

## Severity Thinking

Severity depends on:

- Exploitability
- Affected users
- Data sensitivity
- Business impact
- Existing compensating controls

---

## Professional Language

Write findings with care:

- State what happened
- Avoid exaggeration
- Separate facts from inference
- Include practical next steps

---

## Lab Connection

This week's lab asks you to trace server-side trust boundaries in controlled exercises.

Your deliverable must include evidence, impact, and remediation notes.

---

## Small Group Prompt

What is the smallest piece of evidence that would prove this week's risk without collecting unnecessary data?

---

## Checkpoint Question

Which trust boundary is most important in this week's topic, and why?

---

## Instructor Demo Debrief

After the demo, identify:

- The asset
- The trust boundary
- The failed assumption
- The best remediation

---

## Quiz Preparation

Know:

- Key vocabulary
- Safe testing sequence
- Evidence standards
- Defensive controls
- Scope boundaries

---

## Key Takeaways

- Server-side request forgery shapes testing strategy
- Metadata service exposure reveals assumptions
- Evidence must support impact
- Remediation belongs in engineering terms

---

## Before Next Week

- Complete the Week 11 lab
- Take the Week 11 quiz
- Update your personal testing checklist
- Bring one question from the lab

---

## Textbook Reading

- Chapter 10: Server-Side Request Forgery, Deserialization, and Backend Trust
- Course Companion: `textbook/course_companion/course_alignment_and_labs.md`
