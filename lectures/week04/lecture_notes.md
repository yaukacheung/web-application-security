# Week 4 Lecture Notes

## Session Title

Cross-Site Scripting and Browser Execution Contexts

## Learning Goals

Students should be able to explain browser execution contexts, reflected XSS, stored XSS, DOM XSS, context-aware output encoding and apply them to distinguish XSS variants and recommend encoding controls.

## Timing Plan

| Segment | Time | Focus |
| --- | ---: | --- |
| Opening review | 15 min | Connect prior week to current topic |
| Concept block 1 | 35 min | browser execution contexts and vocabulary |
| Concept block 2 | 35 min | reflected XSS and trust boundaries |
| Break | 10 min |  |
| Demonstration | 35 min | Controlled work against OWASP Juice Shop and Mutillidae II |
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

The technical center of this week is browser execution contexts. Students should connect the concept to concrete request and response behavior instead of treating it as abstract vocabulary.

### Risk Connection

Attacker-controlled script can act inside a user's browser session. Ask students to explain the affected asset and the failed security assumption in plain language.

### Defensive Frame

Security testing is useful only when it leads to better controls. For each finding, push students to name the control location, the expected behavior, and a regression test.

## Suggested Discussion Prompts

- What evidence would prove that this issue affects a real asset?
- Where should the application enforce the defensive control?
- What would make this issue higher or lower severity?
- How could a developer accidentally reintroduce this issue later?

## Lab Bridge

The lab asks students to distinguish XSS variants and recommend encoding controls using OWASP Juice Shop and Mutillidae II. Remind students to stay inside the written scope and to capture only the evidence needed for the claim.

## Textbook Reference

- [Chapter 4: Cross-Site Scripting and Browser Execution Contexts](../../textbook/chapters/04-cross-site-scripting-and-browser-execution-contexts.md)
