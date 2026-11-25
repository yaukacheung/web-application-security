# 16-Week Course Alignment and Lab Exercises

**Author:** Yau Ka Cheung, M.S.  
**Copyright:** © 2026 Yau Ka Cheung, M.S. All rights reserved.

## Course Safety Rules

All offensive security exercises in this companion apply strictly to intentionally vulnerable local containers started from `docker/docker-compose.yml` or systems covered by explicit written authorization. Never probe public websites, university networks, classmates' devices, or cloud metadata endpoints outside controlled local simulations. Never reuse personal or institutional passwords inside lab targets.

## Local Docker Lab Stack

| Application | Local URL | Primary Lab Focus |
| --- | --- | --- |
| OWASP Juice Shop | `http://localhost:3000` | Reconnaissance, XSS, access control, APIs, SSRF |
| DVWA | `http://localhost:8081` | SQL injection, sessions, file upload, path traversal |
| OWASP WebGoat | `http://localhost:8082/WebGoat` | SQL injection, authentication, IDOR, CSRF, SSRF |
| Mutillidae II | `http://localhost:8083` | XSS, session hardening, CSRF, file handling |
| OWASP NodeGoat | `http://localhost:4000` | REST/JSON API testing, dependency and SDLC review |

---

## Weekly Chapter-to-Lab Mapping

| Week | Textbook Chapter | Lab Exercise & Target |
| --- | --- | --- |
| 1 | Chapter 1: Ethics, Authorization, and HTTP Foundations | Start local Docker stack; verify all 5 localhost targets; inspect baseline HTTP traffic in DevTools; write a 3–5 sentence scope statement. |
| 2 | Chapter 2: Web Architecture, Threat Modeling, and Reconnaissance | Map **OWASP Juice Shop** (`:3000`) manually using DevTools and proxy; identify trust boundaries and build an attack surface inventory. |
| 3 | Chapter 3: Input Validation, Encoding, and SQL Injection | Test SQL injection behavior in **DVWA** (`:8081`) and **WebGoat** (`:8082/WebGoat`); capture minimal evidence and write parameterized fixes. |
| 4 | Chapter 4: Cross-Site Scripting and Browser Execution Contexts | Test reflected, stored, and DOM XSS in **OWASP Juice Shop** (`:3000`) and **Mutillidae II** (`:8083`); identify context-aware encoding and CSP rules. |
| 5 | Chapter 5: Authentication Design and Password Security | Evaluate login, lockout, and password-recovery flows in **WebGoat** (`:8082/WebGoat`) and **Juice Shop** (`:3000`) for enumeration and rate controls. |
| 6 | Chapter 6: Session Management and Cookie Security | Inspect session cookies and login rotation in **DVWA** (`:8081`) and **Mutillidae II** (`:8083`); propose hardened `Set-Cookie` headers. |
| 7 | Chapter 7: Access Control and Object-Level Authorization | Test horizontal and vertical authorization in **Juice Shop** (`:3000`) and **WebGoat** (`:8082/WebGoat`) using controlled multi-account ID swaps. |
| 8 | Chapter 14 & Appendix B (Midterm Practical) | Complete a scoped practical assessment against the assigned local target under exam conditions. |
| 9 | Chapter 8: CSRF, Clickjacking, and Browser Defenses | Craft controlled cross-site form submissions in **WebGoat** (`:8082/WebGoat`) and **Mutillidae II** (`:8083`); inspect `SameSite` and framing headers. |
| 10 | Chapter 9: File Upload, Path Traversal, and Server-Side File Handling | Test upload validation and path traversal boundaries in **DVWA** (`:8081`) and **Mutillidae II** (`:8083`). |
| 11 | Chapter 10: SSRF, Deserialization, and Backend Trust | Analyze server-side request boundaries and unsafe object handling in **WebGoat** (`:8082/WebGoat`) and **Juice Shop** (`:3000`). |
| 12 | Chapter 11: API Security and Modern Application Patterns | Test REST/JSON APIs in **NodeGoat** (`:4000`) and **Juice Shop** (`:3000`) for BOLA, mass assignment, and CORS/rate-limit issues. |
| 13 | Chapter 12: Secure SDLC, Dependency Risk, and Supply Chain | Audit **NodeGoat** (`:4000`) manifests and CI workflows (`.github/workflows/build-course.yml`) for dependency and pipeline risks. |
| 14 | Chapter 13 & Chapter 15: Logging, Monitoring, WAFs, and Intrusion Containment | Trigger representative test patterns locally, inspect access/app logs, and draft high-signal detection rules without leaking tokens. |
| 15–16 | Chapters 14, 15, & 16 (Capstone & Final Synthesis) | Execute the Capstone Penetration Testing Project (`project/capstone_penetration_testing_project.md`) using Appendix B's report template. |
