# Environment Setup

## Purpose

This guide prepares a local, isolated workstation for Web Application Security labs. The course uses intentionally vulnerable applications. Keep them local, temporary, and separated from sensitive accounts or networks.

## Required Software

- Docker Desktop or Docker Engine
- Docker Compose v2
- Git
- Node.js LTS and npm
- A modern browser
- OWASP ZAP or Burp Suite Community Edition
- Visual Studio Code or another text editor

## Safety Checklist

Before starting any lab:

- Use only the course-provided Docker targets.
- Do not expose lab services to the public internet.
- Do not reuse personal passwords in lab applications.
- Keep browser profiles for labs separate from personal browsing when possible.
- Shut down containers when the lab is complete.
- Record only lab evidence, not unrelated personal or institutional data.

## Repository Setup

From the repository root:

```bash
mkdir -p syllabus lectures labs quizzes exams project setup docker templates .github/workflows
```

Optional local Git initialization:

```bash
git init
git add README.md syllabus setup docker templates lectures labs quizzes exams project
git commit -m "Start web application security course"
```

Do not place access tokens, passwords, private keys, or session cookies into repository files.

## Start the Lab Stack

From the repository root:

```bash
docker compose -f docker/docker-compose.yml up -d
```

Expected local services:

| Application | URL |
| --- | --- |
| OWASP Juice Shop | `http://localhost:3000` |
| DVWA | `http://localhost:8081` |
| WebGoat | `http://localhost:8082/WebGoat` |
| Mutillidae II | `http://localhost:8083` |
| NodeGoat | `http://localhost:4000` |

## Stop the Lab Stack

```bash
docker compose -f docker/docker-compose.yml down
```

To remove local lab data volumes when instructed:

```bash
docker compose -f docker/docker-compose.yml down -v
```

## Browser Preparation

Create a dedicated browser profile named `WAS-Labs` or similar. Disable password saving for lab sites. Clear cookies and site data between labs when instructed so session behavior is repeatable.

## Proxy Tool Preparation

Install either OWASP ZAP or Burp Suite Community Edition. Configure the browser proxy only during labs that require interception, then disable it afterward.

Baseline proxy settings:

- HTTP proxy host: `127.0.0.1`
- HTTP proxy port: `8080` for ZAP or the configured Burp listener port
- HTTPS interception certificate: install only in the dedicated lab browser profile when needed

## Node.js Slide Tooling

Reveal.js slides are written in Markdown. A common local workflow uses `reveal-md`:

```bash
npm install --global reveal-md
reveal-md lectures/week01/slides.md
```

For PPTX generation, install Pandoc and use the helper scripts included with each lecture folder.

## Troubleshooting

### Port Already in Use

If a service fails because a port is busy, stop the conflicting local service or edit `docker/docker-compose.yml` to map the service to another host port.

### Docker Pull Fails

Check internet connectivity, Docker authentication state, and available disk space. Some institutional networks block container registry access.

### Browser Cannot Reach a Target

Confirm that the containers are running:

```bash
docker compose -f docker/docker-compose.yml ps
```

Then confirm the expected URL and port from the service table above.

## Credential Hygiene

If a real access token, password, or private key is accidentally pasted into a project file or prompt, rotate it immediately through the provider's security settings. Treat it as compromised even if it was not committed.
