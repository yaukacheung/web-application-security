# Textbook Peer-Reviewer & Publisher Audit Report

**Author / Instructor:** Yau Ka Cheung, M.S.  
**Department:** Department of Computer Science and Information Systems, East Texas A&M University  
**Email:** [Yauka.Cheung@etamu.edu](mailto:Yauka.Cheung@etamu.edu)  
**Reviewed Directory:** `textbook/`  
**Source Curriculum:** `syllabus/syllabus.md`, `docs/course_map.md`, `docker/docker-compose.yml`, `lectures/week01–16`, `labs/week01–16`, `project/capstone_penetration_testing_project.md`  
**Audit Date:** 2026-11-24

---

## 1. Curriculum & Technical Accuracy Audit (Peer-Reviewer Check)

| Check | Result | Notes |
| --- | --- | --- |
| **16-Week Syllabus & Synthesis Alignment** | Pass | Preface + Chapters 1–14 map directly to Weeks 1–16; Chapters 15–16 add dedicated coverage of web intrusion attack chains/containment (`NIST SP 800-61 Rev. 3`) and transport cryptography/TLS (`OWASP A02:2021`, `RFC 8446`, `RFC 6797`). |
| **Docker Lab Stack Accuracy** | Pass | All `localhost` URLs and ports match `docker/docker-compose.yml` (`3000` Juice Shop, `8081` DVWA, `8082/WebGoat` WebGoat, `8083` Mutillidae II, `4000` NodeGoat). |
| **No Fabricated Claims or Citations** | Pass | All cited standards and empirical statistics (MITRE 2025 CWE Top 25 scores, Verizon 2026 DBIR web breach & KEV remediation metrics, IETF RFCs 9110/6265/8446/8996/6797, OWASP Top 10:2021, OWASP API Top 10 2023, OWASP WSTG v4.2, OWASP ASVS, NIST SP 800-61r3/800-63B-4/800-92/800-115/800-218, MDN Web Docs) use verified canonical sources. |
| **Visuals, Diagrams & Charts** | Pass | 6 vector SVG figures (`textbook/chapters/assets/fig-01` through `fig-06`) embedded in Chapters 1, 3, 5, 8, 10, and 15 and copied automatically to `online/assets/` and `publish/assets/`. |
| **Safety & Scope Consistency** | Pass | Every chapter and appendix reinforces written authorization, local-only Docker targets, credential hygiene, and minimal evidence collection. |

---

## 2. Editorial, Style & AI-Footprint Audit (Publisher Check)

| Check | Result | Notes |
| --- | --- | --- |
| **Instructor Voice & Style** | Pass | Direct, practical, engineering-focused prose matching `syllabus/syllabus.md` and `lectures/week01/lecture_notes.md`. |
| **AI-Footprint Scan** | Pass | Automated scan across all 20 Markdown files returned **0 hits** for common AI filler phrases (*delve, tapestry, ever-evolving, paramount, moreover, furthermore, leverage, synergistic, holistic, seamless, myriad, plethora, testament, crucial to note, in conclusion*). |
| **Placeholder Scan** | Pass | Automated scan returned **0 placeholders** (`TBD`, `[XX]`, `[Insert`, `TODO`). |
| **Online & Publishable Build** | Pass | `textbook/scripts/build_book.py` generated 20 HTML chapter pages + `index.html` in `textbook/online/`, plus `Web_Application_Security_Textbook.md` and print-ready `Web_Application_Security_Textbook.html` in `textbook/publish/`. |

---

## 3. Publishing Notes for GitHub

- **GitHub Markdown Reading:** Share `textbook/README.md` and `textbook/CHAPTER_LIST.md` directly in the repository.
- **GitHub Pages Online Edition:** Point GitHub Pages to `textbook/online/` (or run `mkdocs gh-deploy` using `textbook/mkdocs.yml`).
- **PDF Print Edition:** Open `textbook/publish/Web_Application_Security_Textbook.html` in a browser and use **Print → Save as PDF**, or convert `textbook/publish/Web_Application_Security_Textbook.md` with Pandoc when available.
