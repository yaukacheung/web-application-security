#!/usr/bin/env python3
"""Chapter 4 Sample Code: Context-Aware Output Encoding & CSP Header."""

import html
import json
import secrets


def render_html_body_safe(user_query: str) -> str:
    # SECURE for HTML body / quoted attribute context
    safe_text = html.escape(user_query, quote=True)
    return f'<p>Search results for: <span class="q">{safe_text}</span></p>'


def embed_json_in_script_safe(user_profile: dict) -> str:
    # SECURE for passing data to client-side JS: JSON + escape '</' to prevent script breakout
    serialized = json.dumps(user_profile).replace("<", "\\u003c").replace(">", "\\u003e")
    return f'<script id="profile-data" type="application/json">{serialized}</script>'


def build_csp_header() -> tuple[str, str]:
    nonce = secrets.token_urlsafe(16)
    policy = (
        f"default-src 'self'; "
        f"script-src 'self' 'nonce-{nonce}'; "
        f"object-src 'none'; "
        f"base-uri 'self'; "
        f"frame-ancestors 'none'"
    )
    return nonce, policy


if __name__ == "__main__":
    payload = '<img src=x onerror="alert(1)">'
    print("HTML encoded:", render_html_body_safe(payload))
    print("Safe JSON script:", embed_json_in_script_safe({"name": "</script><script>alert(1)</script>"}))
    nonce_val, csp = build_csp_header()
    print("Generated CSP:", csp)
