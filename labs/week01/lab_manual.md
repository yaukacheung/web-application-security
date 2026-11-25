# Week 1 Lab Manual

## Lab Title

Environment Validation and Baseline Web Observation

## Duration

2 hours

## Learning Objectives

By the end of this lab, students will be able to:

- Start and stop the local vulnerable application environment.
- Confirm target URLs and document the authorized scope.
- Use browser developer tools to inspect basic HTTP traffic.
- Capture minimal evidence for a baseline observation.
- Write a short professional lab note.

## Authorized Scope

For this lab, students may interact only with services started from `docker/docker-compose.yml` on their own machine:

- `http://localhost:3000`
- `http://localhost:8081`
- `http://localhost:8082/WebGoat`
- `http://localhost:8083`
- `http://localhost:4000`

No public internet targets are in scope.

## Required Tools

- Docker Compose
- Browser developer tools
- Markdown editor

## Procedure

### Part 1: Start the Environment

From the repository root:

```bash
docker compose -f docker/docker-compose.yml up -d
```

Confirm containers are running:

```bash
docker compose -f docker/docker-compose.yml ps
```

### Part 2: Verify Targets

Visit each target URL from the authorized scope. For each target, record:

- URL
- Whether the page loaded
- Page title or visible application name
- HTTP status code for the main document request
- Any immediate login or setup prompt

### Part 3: Observe HTTP Traffic

Open browser developer tools and use the Network tab. Reload one target and identify:

- One request method
- One request path
- Two request headers
- Response status code
- Two response headers
- Whether a cookie was set

### Part 4: Write a Scope Statement

Write a 3-5 sentence scope statement that explains:

- What systems are allowed
- What systems are not allowed
- What testing methods are permitted this week
- When testing should stop

### Part 5: Stop the Environment

```bash
docker compose -f docker/docker-compose.yml down
```

## Deliverable

Submit a Markdown file containing:

- Name and date
- Scope statement
- Target verification table
- HTTP observation notes
- Two screenshots or copied request/response metadata snippets
- One paragraph reflection on why scope matters

## Grading Rubric

| Criterion | Points |
| --- | ---: |
| Correctly starts and verifies local targets | 20 |
| Scope statement is clear and bounded | 20 |
| HTTP observations are accurate | 25 |
| Evidence is relevant and minimal | 20 |
| Reflection shows professional judgment | 15 |

## Cleanup

Confirm containers are stopped before leaving lab. Do not leave intentionally vulnerable applications running longer than needed.

## Textbook Reading

- [Chapter 1: Ethics, Authorization, and HTTP Foundations](../../textbook/chapters/01-ethics-authorization-and-http-foundations.md)
