# Week 15 Lecture Notes

## Session Title

Penetration Testing Methodology and Reporting

## Learning Goals

Students should be able to explain rules of engagement, test planning, finding severity, report writing, executive summaries and apply them to prepare and peer-review capstone findings.

## Timing Plan

| Segment | Time | Focus |
| --- | ---: | --- |
| Opening review | 15 min | Connect prior week to current topic |
| Concept block 1 | 35 min | rules of engagement and vocabulary |
| Concept block 2 | 35 min | test planning and trust boundaries |
| Break | 10 min |  |
| Demonstration | 35 min | Controlled work against Assigned capstone target |
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

The technical center of this week is rules of engagement. Students should connect the concept to concrete request and response behavior instead of treating it as abstract vocabulary.

### Risk Connection

Poor communication prevents useful remediation. Ask students to explain the affected asset and the failed security assumption in plain language.

### Defensive Frame

Security testing is useful only when it leads to better controls. For each finding, push students to name the control location, the expected behavior, and a regression test.

## Suggested Discussion Prompts

- What evidence would prove that this issue affects a real asset?
- Where should the application enforce the defensive control?
- What would make this issue higher or lower severity?
- How could a developer accidentally reintroduce this issue later?

## Lab Bridge

The lab asks students to prepare and peer-review capstone findings using Assigned capstone target. Remind students to stay inside the written scope and to capture only the evidence needed for the claim.

## Textbook Reference

- [Chapter 14 & Appendix B: Scoped Penetration Testing & Reporting](../../textbook/chapters/14-penetration-testing-methodology-and-reporting.md)
