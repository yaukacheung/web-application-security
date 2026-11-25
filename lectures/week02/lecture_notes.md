# Week 2 Lecture Notes

## Session Title

Web Architecture, Threat Modeling, and Reconnaissance

## Learning Goals

Students should be able to explain modern web tiers, assets and trust boundaries, STRIDE-style threat modeling, passive reconnaissance, attack surface inventories and apply them to map a web application without exploiting it.

## Timing Plan

| Segment | Time | Focus |
| --- | ---: | --- |
| Opening review | 15 min | Connect prior week to current topic |
| Concept block 1 | 35 min | modern web tiers and vocabulary |
| Concept block 2 | 35 min | assets and trust boundaries and trust boundaries |
| Break | 10 min |  |
| Demonstration | 35 min | Controlled work against OWASP Juice Shop |
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

The technical center of this week is modern web tiers. Students should connect the concept to concrete request and response behavior instead of treating it as abstract vocabulary.

### Risk Connection

Missed trust boundaries lead to shallow testing and weak remediation. Ask students to explain the affected asset and the failed security assumption in plain language.

### Defensive Frame

Security testing is useful only when it leads to better controls. For each finding, push students to name the control location, the expected behavior, and a regression test.

## Suggested Discussion Prompts

- What evidence would prove that this issue affects a real asset?
- Where should the application enforce the defensive control?
- What would make this issue higher or lower severity?
- How could a developer accidentally reintroduce this issue later?

## Lab Bridge

The lab asks students to map a web application without exploiting it using OWASP Juice Shop. Remind students to stay inside the written scope and to capture only the evidence needed for the claim.

## Textbook Reference

- [Chapter 2: Web Architecture, Threat Modeling, and Reconnaissance](../../textbook/chapters/02-web-architecture-threat-modeling-and-reconnaissance.md)
