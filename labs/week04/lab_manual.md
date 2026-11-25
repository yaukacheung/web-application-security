# Week 4 Lab Manual

## Lab Title

Reflected, Stored, and DOM XSS

## Duration

2 hours

## Authorized Scope

Work only with the local Docker targets assigned for this course. For this lab, the primary target is OWASP Juice Shop and Mutillidae II. Do not test public systems, institutional systems, classmates' machines, or any service outside the course scope.

## Learning Objectives

By the end of this lab, students will be able to:

- Distinguish xss variants and recommend encoding controls.
- Identify relevant assets, trust boundaries, and assumptions.
- Capture minimal evidence that supports a specific security claim.
- Recommend a practical defensive control.

## Required Tools

- Docker Compose
- Browser developer tools
- Intercepting proxy when instructed
- Markdown editor

## Safety Notes

- Keep targets local.
- Do not use real credentials.
- Do not copy unrelated personal data into the report.
- Stop testing if a request leaves the intended local environment.

## Procedure

### Part 1: Start and Verify

Start the lab stack:

```bash
docker compose -f docker/docker-compose.yml up -d
```

Confirm that OWASP Juice Shop and Mutillidae II is reachable and record the URL, page title, authentication state, and current role.

### Part 2: Baseline Mapping

Create a short inventory of relevant requests, inputs, roles, and state changes. Record normal behavior before attempting any test variation.

### Part 3: Controlled Test

Perform the assigned exercise for reflected, stored, and dom xss. Change one variable at a time and compare the result to the baseline behavior.

### Part 4: Defensive Analysis

Explain which defensive control should prevent the issue. Be specific about whether the control belongs in routing, authorization logic, input validation, output encoding, storage, logging, or deployment configuration.

### Part 5: Cleanup

Stop the lab stack:

```bash
docker compose -f docker/docker-compose.yml down
```

## Deliverable

Submit a Markdown report with:

- Name and date
- Target and scope
- Baseline behavior
- Test steps
- Evidence
- Impact
- Remediation
- Reflection on limitations

## Grading Rubric

| Criterion | Points |
| --- | ---: |
| Scope and setup are correct | 15 |
| Baseline mapping is accurate | 20 |
| Controlled test is reproducible | 25 |
| Evidence supports the claim | 20 |
| Remediation is practical and specific | 15 |
| Reflection is thoughtful | 5 |

## Textbook Reading

- [Chapter 4: Cross-Site Scripting and Browser Execution Contexts](../../textbook/chapters/04-cross-site-scripting-and-browser-execution-contexts.md)
