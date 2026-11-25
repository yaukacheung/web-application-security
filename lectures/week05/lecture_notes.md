# Week 5 Lecture Notes

## Session Title

Authentication Design and Password Security

## Learning Goals

Students should be able to explain identity proofing, password storage, rate limiting, MFA, account recovery and apply them to evaluate authentication flows and abuse resistance.

## Timing Plan

| Segment | Time | Focus |
| --- | ---: | --- |
| Opening review | 15 min | Connect prior week to current topic |
| Concept block 1 | 35 min | identity proofing and vocabulary |
| Concept block 2 | 35 min | password storage and trust boundaries |
| Break | 10 min |  |
| Demonstration | 35 min | Controlled work against WebGoat and Juice Shop |
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

The technical center of this week is identity proofing. Students should connect the concept to concrete request and response behavior instead of treating it as abstract vocabulary.

### Risk Connection

Weak authentication turns application exposure into account compromise. Ask students to explain the affected asset and the failed security assumption in plain language.

### Defensive Frame

Security testing is useful only when it leads to better controls. For each finding, push students to name the control location, the expected behavior, and a regression test.

## Suggested Discussion Prompts

- What evidence would prove that this issue affects a real asset?
- Where should the application enforce the defensive control?
- What would make this issue higher or lower severity?
- How could a developer accidentally reintroduce this issue later?

## Lab Bridge

The lab asks students to evaluate authentication flows and abuse resistance using WebGoat and Juice Shop. Remind students to stay inside the written scope and to capture only the evidence needed for the claim.

## Textbook Reference

- [Chapter 5: Authentication Design and Password Security](../../textbook/chapters/05-authentication-design-and-password-security.md)
