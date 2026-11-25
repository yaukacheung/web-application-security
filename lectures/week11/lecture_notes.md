# Week 11 Lecture Notes

## Session Title

SSRF, Deserialization, and Server-Side Abuse

## Learning Goals

Students should be able to explain server-side request forgery, metadata service exposure, unsafe deserialization, egress controls, service identity and apply them to trace server-side trust boundaries in controlled exercises.

## Timing Plan

| Segment | Time | Focus |
| --- | ---: | --- |
| Opening review | 15 min | Connect prior week to current topic |
| Concept block 1 | 35 min | server-side request forgery and vocabulary |
| Concept block 2 | 35 min | metadata service exposure and trust boundaries |
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

The technical center of this week is server-side request forgery. Students should connect the concept to concrete request and response behavior instead of treating it as abstract vocabulary.

### Risk Connection

Backend services may trust requests that originated from vulnerable application code. Ask students to explain the affected asset and the failed security assumption in plain language.

### Defensive Frame

Security testing is useful only when it leads to better controls. For each finding, push students to name the control location, the expected behavior, and a regression test.

## Suggested Discussion Prompts

- What evidence would prove that this issue affects a real asset?
- Where should the application enforce the defensive control?
- What would make this issue higher or lower severity?
- How could a developer accidentally reintroduce this issue later?

## Lab Bridge

The lab asks students to trace server-side trust boundaries in controlled exercises using WebGoat and Juice Shop. Remind students to stay inside the written scope and to capture only the evidence needed for the claim.

## Textbook Reference

- [Chapter 10: Server-Side Request Forgery, Deserialization, and Backend Trust](../../textbook/chapters/10-ssrf-deserialization-and-server-side-abuse.md)
