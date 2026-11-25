# Web Application Security

## Course Information

- **Course level:** Senior undergraduate
- **Format:** 16 weeks
- **Weekly contact time:** 3-hour lecture and 2-hour lab
- **Primary materials:** Markdown readings, Reveal.js slides, Docker lab environments, instructor-provided exercises
- **Prerequisites:** Web development fundamentals, networking basics, command-line fluency, introductory cybersecurity, and at least one programming language

## Course Description

Web Application Security prepares students to assess, design, and defend modern web applications. The course combines secure engineering principles, threat modeling, offensive testing in controlled environments, defensive remediation, and professional reporting. Students work with intentionally vulnerable applications such as OWASP Juice Shop, DVWA, WebGoat, Mutillidae II, and NodeGoat.

The course emphasizes authorization, ethics, repeatability, evidence handling, and risk communication. Students learn how vulnerabilities happen, how attackers exploit them, how defenders detect and prevent them, and how security findings are translated into useful engineering work.

## Learning Outcomes

By the end of the course, students will be able to:

1. Explain core web security concepts, including HTTP, sessions, browser trust boundaries, same-origin policy, and server-side request handling.
2. Map application behavior, data flows, assets, trust boundaries, and likely attack surfaces.
3. Identify and safely validate common web vulnerabilities in authorized lab environments.
4. Analyze authentication, authorization, input handling, state management, API, and client-side security weaknesses.
5. Use professional tools such as browser developer tools, intercepting proxies, scanners, containerized labs, and secure coding references.
6. Recommend practical remediations that reduce risk without ignoring engineering constraints.
7. Produce clear penetration testing reports with evidence, severity, reproduction steps, and remediation guidance.
8. Work ethically within a written scope of authorization.

## Required Tools

- Docker Desktop or Docker Engine with Docker Compose
- Git
- Node.js LTS
- A modern browser with developer tools
- OWASP ZAP or Burp Suite Community Edition
- Visual Studio Code or equivalent editor
- Markdown viewer or editor

## Course Safety Rules

This course includes controlled offensive security practice. Students must follow these rules:

- Only test systems that are part of the assigned lab environment or explicitly listed in a written scope.
- Do not scan, exploit, or probe public systems, university systems, classmates' devices, or cloud services without written permission.
- Do not reuse real credentials in lab applications.
- Do not publish exploit details that identify real third-party systems.
- Stop immediately and notify the instructor if a lab action affects an unintended system.
- Treat discovered credentials, tokens, session values, and personal data as sensitive.

Violations may result in course failure and referral under institutional conduct policies.

## Grading

| Component | Weight |
| --- | ---: |
| Weekly labs | 30% |
| Weekly quizzes | 15% |
| Midterm exam | 15% |
| Final exam | 20% |
| Capstone penetration testing project | 15% |
| Participation and professional practice | 5% |

## Assessment Standards

Student work is graded on technical correctness, ethical conduct, clarity, reproducibility, evidence quality, and remediation judgment. Successful submissions show not only that a vulnerability exists, but also why it matters and how it should be fixed.

## Weekly Schedule

| Week | Lecture Theme | Lab Theme |
| --- | --- | --- |
| 1 | Course orientation, ethics, HTTP foundations, lab setup | Environment validation and baseline web observation |
| 2 | Web architecture, threat modeling, and reconnaissance | Application mapping and attack surface inventory |
| 3 | Input validation, encoding, and injection foundations | SQL injection in controlled lab targets |
| 4 | Cross-site scripting and browser execution contexts | Reflected, stored, and DOM XSS |
| 5 | Authentication design and password security | Authentication testing and credential attack controls |
| 6 | Session management and cookie security | Session fixation, hijacking scenarios, and hardening |
| 7 | Access control and IDOR | Authorization testing and object-level access control |
| 8 | Midterm review and applied practical | Midterm practical exam |
| 9 | CSRF, clickjacking, and browser security controls | CSRF testing and SameSite defenses |
| 10 | File upload, path traversal, and server-side file risks | Upload validation and traversal testing |
| 11 | SSRF, deserialization, and server-side abuse | SSRF lab and service boundary analysis |
| 12 | API security and modern application patterns | REST and JSON API testing |
| 13 | Secure SDLC, dependency risk, and supply chain | Dependency review and CI security checks |
| 14 | Logging, monitoring, incident response, and WAFs | Detection engineering for web attacks |
| 15 | Penetration testing methodology and reporting | Capstone testing workshop |
| 16 | Capstone presentations and final synthesis | Final practical and project presentations |

## Weekly Rhythm

Each week includes:

- Pre-class reading or preparation
- 3-hour lecture with demonstrations and discussion
- 2-hour lab in a controlled environment
- 10-question quiz
- Deliverable or reflection where appropriate

## Lab Submission Format

Unless otherwise specified, lab submissions must include:

- Student name and date
- Target application and version or container tag
- Written scope
- Tools used
- Reproduction steps
- Screenshots or command output as evidence
- Risk explanation
- Remediation recommendation
- Reflection on limitations or false positives

## Capstone Project Summary

Students complete a scoped penetration test against an assigned intentionally vulnerable application. The project includes planning, testing, evidence collection, risk rating, remediation recommendations, and a professional report. Students also deliver a short presentation summarizing the most important findings and lessons learned.

## Academic Integrity

Students may discuss general strategies, but submitted work must be their own. Reusing another student's findings, screenshots, exploit steps, or report language without attribution is not allowed. Use of AI tools must follow institutional policy and must be acknowledged when materially used.

## Accessibility

Students who need accommodations should contact the instructor and the institution's accessibility office as early as possible. Course materials are produced in Markdown to support multiple output formats and assistive workflows.
