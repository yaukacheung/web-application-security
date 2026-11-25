# Textbook Sample Code & Defensive Examples

**Author:** Yau Ka Cheung, M.S.  
**Copyright:** © 2026 Yau Ka Cheung, M.S. All rights reserved.

All Python examples use only the Python 3 standard library and run locally without external dependencies. Each file pairs a vulnerable pattern with its corrected server-side implementation for teaching and code-review exercises.

| File | Chapter | Topic |
| --- | --- | --- |
| `01_sql_injection_sqlite.py` | Chapter 3 | String-concatenated SQL vs. parameterized queries & `ORDER BY` allow-list |
| `02_xss_encoding_and_csp.py` | Chapter 4 | Context-aware HTML/JSON escaping and CSP header construction |
| `03_password_hashing_and_timing.py` | Chapter 5 | `pbkdf2_hmac` (SHA-512) password hashing, per-user salts, and `hmac.compare_digest` |
| `04_path_traversal_confinement.py` | Chapter 9 | Naive `../` replacement vs. `realpath` + `commonpath` confinement |
| `06_structured_security_logging.py` | Chapter 13 | Structured JSON logging, CWE-117 newline escaping, and secret redaction |
| `07_csrf_and_session_cookie.js` | Chapters 6 & 8 | Express session cookie flags, session regeneration, and CSRF token check |

Run any Python example directly:

```bash
python3 textbook/examples/01_sql_injection_sqlite.py
```
