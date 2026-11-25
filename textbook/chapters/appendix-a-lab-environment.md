# Appendix A: Local Docker Lab Environment and Proxy Setup

## A.1 Lab Safety Rules

Before starting the lab stack:

- Run only the five course-provided Docker containers locally on your workstation.
- Do not bind or expose lab containers to public networks.
- Never reuse personal, university, or workplace passwords inside lab targets.
- Keep a dedicated browser profile (for example, `WAS-Labs`) with password saving disabled.
- Shut down containers when you finish your lab session.

## A.2 Starting and Stopping the Lab Stack

From the repository root (`web-application-security/`):

```bash
# Start all five lab targets in the background
docker compose -f docker/docker-compose.yml up -d

# Verify container health and port bindings
docker compose -f docker/docker-compose.yml ps

# Stop containers when finished
docker compose -f docker/docker-compose.yml down
```

To reset lab databases and volumes back to a clean state:

```bash
docker compose -f docker/docker-compose.yml down -v
```

## A.3 Authorized Local Targets

| Service Name | Container Name | Local URL | Primary Chapters |
| --- | --- | --- | --- |
| `juice-shop` | `was-juice-shop` | `http://localhost:3000` | Chapters 1, 2, 4, 5, 7, 10, 11 |
| `dvwa` | `was-dvwa` | `http://localhost:8081` | Chapters 1, 3, 6, 9 |
| `webgoat` | `was-webgoat` | `http://localhost:8082/WebGoat` | Chapters 1, 3, 5, 7, 8, 10 |
| `mutillidae` | `was-mutillidae` | `http://localhost:8083` | Chapters 1, 4, 6, 8, 9 |
| `nodegoat` | `was-nodegoat` | `http://localhost:4000` | Chapters 1, 11, 12 |

## A.4 Intercepting Proxy Setup (OWASP ZAP / Burp Suite)

1. Configure your dedicated `WAS-Labs` browser profile to route HTTP/HTTPS traffic through `127.0.0.1:8080` (or your configured proxy listener port).
2. Enable interception only during active lab exercises and disable the browser proxy afterward.
3. If inspecting local TLS traffic, install the proxy CA certificate **only** inside the dedicated lab browser profile—never system-wide.

## A.5 Troubleshooting

- **Port already in use:** Stop the conflicting local service or adjust the host port mapping in `docker/docker-compose.yml`.
- **Container unreachable:** Run `docker compose -f docker/docker-compose.yml ps` and `docker compose -f docker/docker-compose.yml logs <service>` to confirm startup completed.
