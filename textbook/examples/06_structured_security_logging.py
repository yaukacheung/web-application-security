#!/usr/bin/env python3
"""Chapter 13 Sample Code: Structured Security Logging with Redaction."""

import json
import uuid
from datetime import datetime, timezone

SENSITIVE_KEYS = {"password", "token", "authorization", "cookie", "api_key"}


def redact_dict(data: dict) -> dict:
    cleaned = {}
    for k, v in data.items():
        if k.lower() in SENSITIVE_KEYS:
            cleaned[k] = "[REDACTED]"
        else:
            cleaned[k] = v
    return cleaned


def log_security_event(event_type: str, user_id: str, route: str, status: int, extra: dict) -> str:
    # JSON serialization neutralizes newline log injection (CWE-117)
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "correlation_id": str(uuid.uuid4()),
        "event": event_type,
        "user_id": user_id,
        "route": route,
        "status": status,
        "details": redact_dict(extra),
    }
    return json.dumps(record)


if __name__ == "__main__":
    sample_extra = {
        "user_agent": "DemoClient/1.0\nFAKE LOG ENTRY: admin login",
        "password": "secret-value",
        "token": "eyJhbGciOiJIUzI1NiJ9.example",
    }
    print(log_security_event("auth_failure", "student_42", "/api/login", 401, sample_extra))
