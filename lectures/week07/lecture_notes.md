# Week 7 Lecture Notes

## Session Title

Access Control and IDOR

## Learning Goals

Students should be able to explain authorization decisions, horizontal access control, vertical access control, IDOR, deny-by-default design and apply them to test object access using controlled role and identifier changes.

## Timing Plan

| Segment | Time | Focus |
| --- | ---: | --- |
| Opening review | 15 min | Connect prior week to current topic |
| Concept block 1 | 35 min | authorization decisions and vocabulary |
| Concept block 2 | 35 min | horizontal access control and trust boundaries |
| Break | 10 min |  |
| Demonstration | 35 min | Controlled work against Juice Shop and WebGoat |
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

The technical center of this week is authorization decisions. Students should connect the concept to concrete request and response behavior instead of treating it as abstract vocabulary.

### Risk Connection

Authenticated users may access objects or actions they do not own. Ask students to explain the affected asset and the failed security assumption in plain language.

### Defensive Frame

Security testing is useful only when it leads to better controls. For each finding, push students to name the control location, the expected behavior, and a regression test.

## Suggested Discussion Prompts

- What evidence would prove that this issue affects a real asset?
- Where should the application enforce the defensive control?
- What would make this issue higher or lower severity?
- How could a developer accidentally reintroduce this issue later?

## Lab Bridge

The lab asks students to test object access using controlled role and identifier changes using Juice Shop and WebGoat. Remind students to stay inside the written scope and to capture only the evidence needed for the claim.

## Textbook Reference

- [Chapter 7: Access Control and Object-Level Authorization](../../textbook/chapters/07-access-control-and-idor.md)
