---
title: "Web Application Security - Week 1"
author: "Yau Ka Cheung, M.S."
date: "Week 1"
revealOptions:
  transition: slide
  slideNumber: true
  hash: true
  controls: true
  progress: true
  center: false
---

# Web Application Security

## Week 1: Orientation, Ethics, HTTP, and Lab Setup

Senior undergraduate course

---

## Today's Outcomes

By the end of today, you should be able to:

- Explain the course safety model
- Describe the HTTP request and response cycle
- Identify common web application trust boundaries
- Start the local vulnerable app environment
- Record baseline evidence professionally

---

## Course Rhythm

- 3-hour weekly lecture
- 2-hour weekly lab
- Weekly quiz
- Midterm and final practical components
- Capstone penetration testing project

---

## What We Mean by Web Application Security

Web application security studies how web systems fail, how those failures are abused, and how engineering teams prevent, detect, and fix them.

---

## The Professional Frame

Security testing is not just technical.

It is also:

- Authorized
- Scoped
- Documented
- Reproducible
- Communicated responsibly

---

## Authorization Is the First Control

Before testing, know:

- Who owns the system
- What is in scope
- What is out of scope
- What testing methods are allowed
- When testing must stop

---

## Course Safety Boundary

Allowed:

- Assigned local Docker targets
- Instructor-provided scopes
- Your own intentionally vulnerable code

Not allowed:

- Public websites
- University systems
- Classmates' devices
- Any target without explicit permission

---

## Controlled Targets This Semester

- OWASP Juice Shop
- DVWA
- WebGoat
- Mutillidae II
- NodeGoat

These applications are intentionally vulnerable and should stay local.

---

## Security Mindset

Good testers ask:

- What can the user control?
- What does the server trust?
- What data crosses boundaries?
- What assumptions can fail?
- What evidence supports the finding?

---

## Web Application Building Blocks

- Browser
- Network
- Web server
- Application code
- Database
- Third-party services
- Identity provider

---

## HTTP in One Slide

The browser sends a request.

The server returns a response.

State is layered on top using cookies, tokens, sessions, storage, and application logic.

---

## Request Anatomy

Common request elements:

- Method
- Path
- Query string
- Headers
- Cookies
- Body

---

## Response Anatomy

Common response elements:

- Status code
- Headers
- Cookies
- Body
- Redirect location
- Cache instructions

---

## Methods Matter

Common methods:

- `GET` retrieves
- `POST` submits
- `PUT` replaces
- `PATCH` modifies
- `DELETE` removes

Applications do not always enforce method meaning correctly.

---

## Status Codes as Signals

- `2xx` success
- `3xx` redirect
- `4xx` client-side problem
- `5xx` server-side problem

Status codes help map behavior, but they do not prove security by themselves.

---

## Headers as Security Controls

Headers can influence:

- Cookie handling
- Browser framing
- Content execution
- Transport security
- Caching
- Cross-origin access

---

## Cookies and Sessions

HTTP is stateless.

Applications often use cookies to connect many requests to one user session.

Session handling mistakes can become authentication or authorization failures.

---

## Trust Boundaries

A trust boundary exists wherever data moves between zones with different control or assumptions.

Examples:

- Browser to server
- App to database
- App to payment provider
- Admin user to normal user

---

## User-Controlled Inputs

Inputs include more than visible form fields:

- URL paths
- Query parameters
- Headers
- Cookies
- JSON bodies
- File uploads
- Hidden fields

---

## Client-Side Controls Are Not Enough

Browser validation improves usability.

Server-side validation enforces security.

Anything delivered to the browser can be inspected, modified, replayed, or removed.

---

## Threat Modeling Preview

We will repeatedly ask:

- What are we protecting?
- Who might attack it?
- How could the attack happen?
- What would the impact be?
- Which controls reduce the risk?

---

## Lab Evidence

Useful evidence is:

- Dated
- Scoped
- Reproducible
- Minimal
- Relevant to the claim
- Free of unrelated private data

---

## Finding Format

A professional finding includes:

- Title
- Severity
- Affected asset
- Description
- Reproduction steps
- Evidence
- Impact
- Remediation

---

## Tooling This Semester

- Browser developer tools
- Intercepting proxy
- Docker Compose
- Markdown reports
- Screenshots and request logs
- Secure coding references

---

## Starting the Lab Stack

From the repository root:

```bash
docker compose -f docker/docker-compose.yml up -d
```

Then visit the local URLs listed in the setup guide.

---

## Baseline Observation

For each assigned target, record:

- URL
- Page title
- Visible authentication options
- Interesting request paths
- Cookies set before login
- Response status codes

---

## Common Week 1 Mistakes

- Testing outside scope
- Capturing too much unrelated data
- Confusing a bug with a vulnerability
- Treating scanner output as proof
- Forgetting to shut down lab containers

---

## Mini Exercise

Open browser developer tools.

Visit one local lab target.

Find:

- One request header
- One response header
- One cookie or confirmation that no cookie was set

---

## Week 1 Lab Preview

The lab asks you to:

- Start the local environment
- Verify each target
- Observe baseline HTTP behavior
- Capture evidence
- Write a short scope statement

---

## Key Takeaways

- Authorization comes before technique
- HTTP is simple, but applications add complex state
- User-controlled data appears in many places
- Evidence quality matters
- Local labs keep practice ethical and repeatable
- Before next week: complete the lab and quiz

---

## Textbook Reading

- Chapter 1: Ethics, Authorization, and HTTP Foundations
- Course Companion: `textbook/course_companion/course_alignment_and_labs.md`
