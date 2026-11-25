# Preface

**Author:** Yau Ka Cheung, M.S.  
**Contact:** [Yauka.Cheung@etamu.edu](mailto:Yauka.Cheung@etamu.edu)  
**Copyright:** © 2026 Yau Ka Cheung, M.S. All rights reserved.

---

Modern web applications are distributed systems built across browsers, reverse proxies, application servers, databases, and third-party APIs. Every request crosses multiple execution contexts and trust boundaries—and most serious vulnerabilities appear where developers assume data, identity, or network origin can be trusted without verification.

This book bridges **web programming** and **security engineering**. Rather than treating security as a checklist of isolated attack payloads, it teaches how web systems fail from the inside out: how parser confusion causes injection, how ambient browser credentials enable cross-site attacks, how missing server-side ownership checks expose records, and how defenders detect, contain, and remediate real intrusions.

Throughout every chapter, analysis returns to four practical questions:

1. **What can the user control?** (Paths, query strings, headers, cookies, JSON bodies, file metadata, and client-side state.)
2. **What does the server trust?** (Assumptions about identity, origin, file types, backend services, and serialized objects.)
3. **Where are the trust boundaries?** (Browser-to-server, application-to-database, service-to-service, and user-to-admin.)
4. **What control reduces the risk without breaking the engineering workflow?** (Parameterized interfaces, context-aware encoding, server-side authorization, and verifiable regression tests.)

## Structure of the Book

The 16 chapters move from protocol foundations to full-stack defense and scoped security assessment:

- **Part I (Chapters 1–4):** Ethics, authorization, HTTP mechanics, threat modeling, reconnaissance, SQL injection, and cross-site scripting (XSS).
- **Part II (Chapters 5–7):** Authentication design, password storage, session management, cookie attributes, and object-level access control (IDOR).
- **Part III (Chapters 8–11):** Cross-site request forgery (CSRF), clickjacking, file uploads, path traversal, server-side request forgery (SSRF), unsafe deserialization, and REST/GraphQL API security.
- **Part IV (Chapters 12–16):** Secure SDLC, dependency and supply-chain risk, logging, monitoring, WAFs, scoped penetration testing and reporting, web intrusion attack chains and containment, and transport cryptography (TLS/HTTPS).

Appendices A–C provide a containerized lab setup reference, a reusable penetration testing report template, and a master index of cited standards and security advisories.

## Ethics and Safe Testing Scope

Offensive security techniques are dual-use. Every testing technique in this book must stay inside explicit authorization boundaries:

- **Authorized targets only:** Test only systems you own, isolated local lab environments, or targets covered by written authorization.
- **No unauthorized scanning:** Do not probe public websites, institutional networks, or third-party cloud infrastructure without explicit permission.
- **Credential hygiene:** Never reuse real personal or organizational passwords, API keys, or tokens inside test environments.
- **Minimal evidence:** Capture only the request, response, or screenshot needed to prove a technical claim, and redact sensitive tokens or unrelated data.
