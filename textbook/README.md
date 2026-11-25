# Web Application Security

**Author:** Yau Ka Cheung, M.S.  
**Contact:** [Yauka.Cheung@etamu.edu](mailto:Yauka.Cheung@etamu.edu)  
**Copyright:** © 2026 Yau Ka Cheung, M.S. All rights reserved.

A publishable, Markdown-first textbook on **Secure Engineering, Threat Modeling, and Scoped Testing** for modern web applications, with a GitHub-ready online edition and separate course companion materials.

## Textbook Contents

- [Chapter List](CHAPTER_LIST.md)
- [Preface](chapters/00-preface.md)
- **Part I: Foundations, Threat Modeling, and Input/Client Injection**
  - [Chapter 1: Ethics, Authorization, and HTTP Foundations](chapters/01-ethics-authorization-and-http-foundations.md)
  - [Chapter 2: Web Architecture, Threat Modeling, and Reconnaissance](chapters/02-web-architecture-threat-modeling-and-reconnaissance.md)
  - [Chapter 3: Input Validation, Encoding, and SQL Injection](chapters/03-input-validation-encoding-and-sql-injection.md)
  - [Chapter 4: Cross-Site Scripting and Browser Execution Contexts](chapters/04-cross-site-scripting-and-browser-execution-contexts.md)
- **Part II: Identity, Session State, and Access Control**
  - [Chapter 5: Authentication Design and Password Security](chapters/05-authentication-design-and-password-security.md)
  - [Chapter 6: Session Management and Cookie Security](chapters/06-session-management-and-cookie-security.md)
  - [Chapter 7: Access Control and Object-Level Authorization](chapters/07-access-control-and-idor.md)
- **Part III: Browser Boundaries, Server-Side Risks, and Modern APIs**
  - [Chapter 8: Cross-Site Request Forgery, Clickjacking, and Browser Defenses](chapters/08-csrf-clickjacking-and-browser-security-controls.md)
  - [Chapter 9: File Upload, Path Traversal, and Server-Side File Handling](chapters/09-file-upload-path-traversal-and-server-side-file-risks.md)
  - [Chapter 10: Server-Side Request Forgery, Deserialization, and Backend Trust](chapters/10-ssrf-deserialization-and-server-side-abuse.md)
  - [Chapter 11: API Security and Modern Application Patterns](chapters/11-api-security-and-modern-application-patterns.md)
- **Part IV: Engineering Lifecycle, Detection, Intrusion Defense, and Practice**
  - [Chapter 12: Secure SDLC, Dependency Risk, and Software Supply Chain](chapters/12-secure-sdlc-dependency-risk-and-supply-chain.md)
  - [Chapter 13: Security Logging, Monitoring, Incident Response, and WAFs](chapters/13-logging-monitoring-incident-response-and-wafs.md)
  - [Chapter 14: Scoped Penetration Testing, Evidence, and Remediation Reporting](chapters/14-penetration-testing-methodology-and-reporting.md)
  - [Chapter 15: Web Intrusion, Attack Chains, and Containment](chapters/15-web-intrusion-attack-chains-and-containment.md)
  - [Chapter 16: Transport Cryptography, TLS, and Modern Web Hardening](chapters/16-transport-cryptography-tls-and-web-hardening.md)
- **Appendices**
  - [Appendix A: Local Docker Lab Environment & Proxy Setup](chapters/appendix-a-lab-environment.md)
  - [Appendix B: Penetration Testing Finding & Report Template](chapters/appendix-b-penetration-testing-report-template.md)
  - [Appendix C: Master Standards & References Index](chapters/appendix-c-standards-and-references.md)
  - [Appendix D: Glossary of Key Terms](chapters/appendix-d-glossary.md)
  - [Appendix E: Review Question Answers](chapters/appendix-e-review-question-answers.md)

## Editions, Sample Code & Separate Course Companion

- **Course Alignment & Weekly Lab Exercises (Separated):** [course_companion/README.md](course_companion/README.md)
- **Sample Code & Defensive Examples:** [examples/README.md](examples/README.md)
- **Chapters 15–16 Student Assessment:** [assessments/chapter15_16_quiz_student.md](assessments/chapter15_16_quiz_student.md)
- **Online Web Edition (GitHub Pages Ready):** `online/index.html`
- **Leanpub Manuscript Bundle:** `leanpub/manuscript/` ([Upload Guide](leanpub/LEANPUB_UPLOAD_GUIDE.md))
- **Compiled Single-File Manuscript:** `publish/Web_Application_Security_Textbook.md`
- **Print-Ready HTML Edition (for PDF export):** `publish/Web_Application_Security_Textbook.html`
- **Instructor Answer Key (Private — Exclude from Student Repos):** `instructor/review_question_solutions.md`
- **Publishing Guide:** [PUBLISHING_GUIDE.md](PUBLISHING_GUIDE.md)
- **Quality & Publisher Audit:** [AUDIT_REPORT.md](AUDIT_REPORT.md)

To rebuild the online HTML site, compiled publishable edition, and Leanpub manuscript after editing any chapter:

```bash
python3 textbook/scripts/build_book.py && python3 textbook/scripts/export_leanpub.py
```
