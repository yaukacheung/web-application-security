# Week 3 Lecture Notes

## Session Title

Input Validation, Encoding, and Injection Foundations

## Learning Goals

Students should be able to explain parser confusion, SQL injection, parameterized queries, allow lists, error handling and apply them to validate injection behavior in intentionally vulnerable forms.

## Timing Plan

| Segment | Time | Focus |
| --- | ---: | --- |
| Opening review | 15 min | Connect prior week to current topic |
| Concept block 1 | 35 min | parser confusion and vocabulary |
| Concept block 2 | 35 min | SQL injection and trust boundaries |
| Break | 10 min |  |
| Demonstration | 35 min | Controlled work against DVWA and WebGoat |
| Defensive controls | 30 min | Prevention, detection, and verification |
| Reporting workshop | 20 min | Evidence, impact, and remediation |
| Lab briefing | 10 min | Scope, deliverables, and safety reminders |

## Instructor Preparation

- Start the local lab stack before class if a live demo is planned.
- Prepare a clean browser profile and proxy configuration.
- Choose one low-risk demonstration path that stays inside the assigned target.
- Prepare an example finding with one strong evidence item and one weak evidence item.

## Key Teaching Points

### Technical Core

The technical center of this week is parser confusion. Students should connect the concept to concrete request and response behavior instead of treating it as abstract vocabulary.

### Risk Connection

Untrusted input can change the meaning of backend queries. Ask students to explain the affected asset and the failed security assumption in plain language.

### Defensive Frame

Security testing is useful only when it leads to better controls. For each finding, push students to name the control location, the expected behavior, and a regression test.

## Suggested Discussion Prompts

- What evidence would prove that this issue affects a real asset?
- Where should the application enforce the defensive control?
- What would make this issue higher or lower severity?
- How could a developer accidentally reintroduce this issue later?

## Lab Bridge

The lab asks students to validate injection behavior in intentionally vulnerable forms using DVWA and WebGoat. Remind students to stay inside the written scope and to capture only the evidence needed for the claim.

## Textbook Reference

- [Chapter 3: Input Validation, Encoding, and SQL Injection](../../textbook/chapters/03-input-validation-encoding-and-sql-injection.md)
