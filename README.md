# web-application-security

Course materials on Web Application Security.

This repository is being built as a complete Markdown-first course with Reveal.js slides, weekly labs, quizzes, exams, Docker-based practice environments, grading rubrics, and CI build automation.

## Contents

- `syllabus/syllabus.md` - course overview, outcomes, policies, weekly plan, and grading model
- `setup/environment_setup.md` - student workstation and lab environment setup
- `docker/docker-compose.yml` - local vulnerable web application lab stack
- `templates/reveal_template.md` - reusable Reveal.js slide template
- `lectures/week01/` through `lectures/week16/` - weekly Reveal.js slides, notes, and PPTX helpers
- `lectures/week01/` through `lectures/week16/` also include student handouts and instructor teaching briefs
- `labs/week01/` through `labs/week16/` - weekly lab manuals with student and instructor editions
- `quizzes/` - 10-question quiz for each week, plus separated student and instructor copies
- `exams/` - midterm, final, student exam copies, instructor exam copies, answer keys, and supplemental exam bank
- `project/` - capstone penetration testing project and grading rubrics
- `docs/` - student guide, instructor guide, and course map
- `textbook/` - complete 16-chapter publishable textbook, online GitHub Pages edition (`textbook/online/`)


## Safety Notice

All offensive security activities in this course are limited to intentionally vulnerable local lab targets or written authorization scopes. Students must not test systems they do not own or have explicit permission to assess.

## Local Commands

Install the slide dependency when needed:

```bash
npm install
```

Preview Week 1 slides:

```bash
npm run slides:week01
```

Regenerate repeated course materials:

```bash
npm run materials:generate
```
# web-application-security
