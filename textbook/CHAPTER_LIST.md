# Web Application Security: Textbook Chapter List

**Author:** Yau Ka Cheung, M.S.  
**Email:** [Yauka.Cheung@etamu.edu](mailto:Yauka.Cheung@etamu.edu)  
**Copyright:** © 2026 Yau Ka Cheung, M.S. All rights reserved.  
**Target Audience:** Undergraduate and graduate students in Cybersecurity and Web Programming, and practicing software engineers  
**Course Companion:** Separated in `textbook/course_companion/`

---

## Front Matter

- **Preface & Course Safety Model** (`00-preface.md`)
  - Purpose of the textbook and how it pairs with weekly lectures and labs
  - Written scope, authorization rules, and ethical boundaries
  - Overview of the local Docker lab stack

---

## Part I: Foundations, Threat Modeling, and Input/Client Injection (Weeks 1–4)

### Chapter 1: Ethics, Authorization, and HTTP Foundations *(Week 1)*
- **Learning Objectives:** Explain written scope and authorization rules; trace the HTTP/1.1 and HTTP/2 request-response cycle; identify trust boundaries and statelessness workarounds.
- **Core Topics:** Rules of engagement, curiosity vs. authorization, HTTP methods, status codes, headers, cookies, client-side vs. server-side validation, minimal evidence collection.
- **Lab Alignment:** Environment validation and baseline HTTP observation across the local Docker stack.
- **Key References:** IETF RFC 9110, IETF RFC 6265, OWASP WSTG v4.2.

### Chapter 2: Web Architecture, Threat Modeling, and Reconnaissance *(Week 2)*
- **Learning Objectives:** Decompose a modern web application into components and data flows; build a lightweight threat model; inventory an application's attack surface without noisy scanning.
- **Core Topics:** Multi-tier and SPA/API architectures, trust boundaries, asset identification, STRIDE-style threat modeling, passive vs. active reconnaissance, endpoint and parameter mapping.
- **Lab Alignment:** Application mapping and attack surface inventory on OWASP Juice Shop.
- **Key References:** OWASP Threat Modeling Cheat Sheet, OWASP WSTG v4.2 (Information Gathering), OWASP ASVS.

### Chapter 3: Input Validation, Encoding, and SQL Injection *(Week 3)*
- **Learning Objectives:** Explain parser confusion as the root cause of injection; construct and test parameterized queries; distinguish validation from encoding and sanitization.
- **Core Topics:** Data vs. code separation, allow-list input validation, SQL injection mechanics (in-band, error-based, blind), parameterized queries / prepared statements, ORM pitfalls, error handling.
- **Lab Alignment:** SQL injection validation and remediation analysis on DVWA and WebGoat.
- **Key References:** OWASP Top 10:2021 (A03 Injection), OWASP SQL Injection Prevention Cheat Sheet, MITRE CWE-89.

### Chapter 4: Cross-Site Scripting and Browser Execution Contexts *(Week 4)*
- **Learning Objectives:** Differentiate reflected, stored, and DOM-based XSS; select context-aware output encoding for HTML, attribute, JavaScript, and URL contexts; evaluate CSP and framework auto-escaping.
- **Core Topics:** Browser parsing and execution contexts, reflected vs. stored vs. DOM XSS, sources and sinks, context-aware encoding, Content Security Policy (CSP), `HttpOnly` cookie limits.
- **Lab Alignment:** Reflected, stored, and DOM XSS testing on OWASP Juice Shop and Mutillidae II.
- **Key References:** MITRE CWE-79, OWASP XSS Prevention Cheat Sheet, MDN Content Security Policy.

---

## Part II: Identity, Session State, and Access Control (Weeks 5–8)

### Chapter 5: Authentication Design and Password Security *(Week 5)*
- **Learning Objectives:** Design secure registration, login, and password-reset flows; choose appropriate password hashing algorithms; mitigate credential stuffing and enumeration.
- **Core Topics:** Password storage (Argon2id, scrypt, bcrypt, PBKDF2), salting and work factors, NIST SP 800-63B guidance, multi-factor authentication (MFA), account enumeration, rate limiting and lockout trade-offs.
- **Lab Alignment:** Authentication flow testing and credential attack controls on WebGoat and OWASP Juice Shop.
- **Key References:** NIST SP 800-63B / 800-63B-4, OWASP Top 10:2021 (A07), MITRE CWE-287.

### Chapter 6: Session Management and Cookie Security *(Week 6)*
- **Learning Objectives:** Trace the full session lifecycle from issuance to invalidation; configure cookie attributes securely; identify session fixation and hijacking risks.
- **Core Topics:** Stateless HTTP vs. stateful sessions, session token entropy, `Secure`, `HttpOnly`, `SameSite`, `Domain`, and `Path` cookie flags (RFC 6265), session fixation, idle/absolute timeouts, JWT vs. opaque server-side sessions.
- **Lab Alignment:** Session fixation, hijacking scenarios, and cookie hardening on DVWA and Mutillidae II.
- **Key References:** IETF RFC 6265, OWASP Session Management Cheat Sheet, MITRE CWE-384.

### Chapter 7: Access Control and Object-Level Authorization *(Week 7)*
- **Learning Objectives:** Distinguish authentication from authorization; test for horizontal and vertical privilege escalation and IDOR; implement deny-by-default server-side checks.
- **Core Topics:** RBAC, ABAC, and ownership checks; Insecure Direct Object References (IDOR); horizontal vs. vertical escalation; forced browsing; deny-by-default architecture; multi-role test matrices.
- **Lab Alignment:** Authorization testing and object-level access control on OWASP Juice Shop and WebGoat.
- **Key References:** OWASP Top 10:2021 (A01 Broken Access Control), MITRE CWE-639, OWASP WSTG-ATHZ.

---

## Part III: Browser Boundaries, Server-Side Risks, and Modern APIs (Weeks 9–12)

### Chapter 8: Cross-Site Request Forgery, Clickjacking, and Browser Defenses *(Week 9)*
- **Learning Objectives:** Explain how cross-origin ambient credentials enable CSRF; implement synchronizer tokens and `SameSite` defenses; prevent UI redressing with framing controls.
- **Core Topics:** Same-Origin Policy (SOP), ambient authority, CSRF mechanics (`GET` vs. `POST` state changes), synchronizer token pattern, double-submit cookies, Fetch Metadata headers, clickjacking, `X-Frame-Options`, and CSP `frame-ancestors`.
- **Lab Alignment:** CSRF testing and `SameSite` defense evaluation on WebGoat and Mutillidae II.
- **Key References:** MDN Same-Origin Policy, OWASP CSRF Prevention Cheat Sheet, MITRE CWE-352.

### Chapter 9: File Upload, Path Traversal, and Server-Side File Handling *(Week 10)*
- **Learning Objectives:** Analyze file upload and download pipelines for execution and traversal flaws; enforce server-side path canonicalization and storage isolation.
- **Core Topics:** Path traversal (`../`, URL encoding, null/canonicalization bugs), unrestricted file upload risks, MIME-type vs. magic-byte checks, polyglot files, safe filename generation, outside-webroot and object-storage isolation.
- **Lab Alignment:** Upload validation and path traversal testing on DVWA and Mutillidae II.
- **Key References:** MITRE CWE-22, MITRE CWE-434, OWASP File Upload Cheat Sheet.

### Chapter 10: Server-Side Request Forgery, Deserialization, and Backend Trust *(Week 11)*
- **Learning Objectives:** Trace server-side outbound requests across internal network boundaries; prevent SSRF against metadata services; explain unsafe deserialization gadget risks.
- **Core Topics:** SSRF mechanics, cloud metadata endpoints (e.g., IMDSv1 vs. IMDSv2), DNS rebinding and URL parser discrepancies, egress allow-lists, serialization formats (JSON vs. native binary/Java/PHP/Python), unsafe deserialization defenses.
- **Lab Alignment:** SSRF and service boundary analysis on WebGoat and OWASP Juice Shop.
- **Key References:** OWASP Top 10:2021 (A10 SSRF, A08 Software and Data Integrity Failures), OWASP SSRF Prevention Cheat Sheet, MITRE CWE-918, MITRE CWE-502.

### Chapter 11: API Security and Modern Application Patterns *(Week 12)*
- **Learning Objectives:** Assess REST and JSON APIs against the OWASP API Security Top 10; test object-property authorization and mass assignment; design safe CORS and rate-limiting policies.
- **Core Topics:** REST/JSON and GraphQL attack surfaces, Broken Object Level Authorization (BOLA), Broken Object Property Level Authorization (mass assignment / excessive data exposure), CORS misconfigurations, rate limiting and resource consumption, API inventory management.
- **Lab Alignment:** REST and JSON API testing on OWASP NodeGoat and OWASP Juice Shop.
- **Key References:** OWASP API Security Top 10 (2023), MDN CORS Guide, OWASP REST Security Cheat Sheet.

---

## Part IV: Engineering Lifecycle, Detection, and Professional Practice (Weeks 13–16)

### Chapter 12: Secure SDLC, Dependency Risk, and Software Supply Chain *(Week 13)*
- **Learning Objectives:** Integrate security checks into CI/CD pipelines; evaluate third-party dependency and lockfile risks; apply NIST SSDF practices to web projects.
- **Core Topics:** Secure SDLC gates, Software Composition Analysis (SCA), lockfiles and transitive dependencies, SBOMs, SAST vs. DAST trade-offs, secret scanning, CI/CD pipeline hardening.
- **Lab Alignment:** Dependency review and CI security checks on OWASP NodeGoat and course repository workflows.
- **Key References:** OWASP Top 10:2021 (A06 Vulnerable and Outdated Components), NIST SP 800-218 (SSDF).

### Chapter 13: Security Logging, Monitoring, Incident Response, and WAFs *(Week 14)*
- **Learning Objectives:** Design structured security logs without leaking secrets; write detection rules for common web attacks; evaluate what a WAF can and cannot protect.
- **Core Topics:** Log-worthy security events, log injection and PII/token redaction, correlation IDs, alert fatigue vs. actionable signals, web incident triage, Web Application Firewall (WAF) placement, bypasses, and virtual patching.
- **Lab Alignment:** Detection engineering for web attacks using the local Docker lab stack.
- **Key References:** OWASP Top 10:2021 (A09 Security Logging and Monitoring Failures), NIST SP 800-92, OWASP Logging Cheat Sheet.

### Chapter 14: Scoped Penetration Testing, Evidence, and Remediation Reporting *(Weeks 8, 15, & 16)*
- **Learning Objectives:** Execute a structured web penetration test within written rules of engagement; collect minimal, reproducible evidence; write an executive summary and engineering-ready remediation roadmap.
- **Core Topics:** NIST SP 800-115 and OWASP WSTG workflows, scoping and rules of engagement, evidence handling and redaction, severity rating and business impact, writing actionable findings, regression testing, midterm/capstone practical readiness.
- **Lab Alignment:** Midterm practical preparation (Week 8) and Capstone Penetration Testing Project (Weeks 15–16).
- **Key References:** NIST SP 800-115, OWASP WSTG v4.2, Course Capstone Specification.

### Chapter 15: Web Intrusion, Attack Chains, and Containment *(Synthesis)*
- **Learning Objectives:** Trace how attackers chain web vulnerabilities into full intrusions; recognize web shell and persistence indicators; apply NIST SP 800-61 Rev. 3 containment and secret rotation; interpret empirical Verizon DBIR breach metrics.
- **Core Topics:** Multi-stage intrusion chains, web shells, rogue admin accounts, read-only container filesystems, least-privilege IAM/DB roles, egress filtering, evidence preservation, and containment.
- **Key References:** NIST SP 800-61 Rev. 3, Verizon 2026 DBIR, OWASP Top 10:2021.

### Chapter 16: Transport Cryptography, TLS, and Modern Web Hardening *(Synthesis)*
- **Learning Objectives:** Explain how TLS 1.3 protects confidentiality and integrity; identify deprecated protocols and mixed content risks; configure HSTS and browser security response headers.
- **Core Topics:** HTTPS and TLS 1.3 (RFC 8446), deprecated TLS 1.0/1.1 (RFC 8996), forward secrecy, certificate verification, SSL stripping and HSTS (RFC 6797), `X-Content-Type-Options`, `Referrer-Policy`, and `Permissions-Policy`.
- **Key References:** OWASP Top 10:2021 (A02 Cryptographic Failures), IETF RFC 9110, RFC 8446, RFC 6797, MDN Mixed Content.

---

## Appendices

- **Appendix A: Local Docker Lab Environment & Proxy Setup** (`appendix-a-lab-environment.md`)
- **Appendix B: Penetration Testing Finding & Report Template** (`appendix-b-penetration-testing-report-template.md`)
- **Appendix C: Master Standards & References Index** (`appendix-c-standards-and-references.md`)
- **Appendix D: Glossary of Key Terms** (`appendix-d-glossary.md`)
- **Appendix E: Review Question Answers** (`appendix-e-review-question-answers.md`)
