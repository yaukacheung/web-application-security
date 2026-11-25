#!/usr/bin/env python3
"""Chapter 9 Sample Code: Path Traversal Confinement."""

import os
import tempfile


def resolve_safe_upload_path(base_dir: str, user_filename: str) -> str:
    base_real = os.path.realpath(base_dir)
    # Strip any directory components if only flat filenames are expected
    candidate = os.path.realpath(os.path.join(base_real, user_filename))
    if os.path.commonpath([base_real, candidate]) != base_real or candidate == base_real:
        raise ValueError(f"Blocked path traversal attempt: {user_filename!r}")
    return candidate


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp_uploads:
        safe_target = resolve_safe_upload_path(tmp_uploads, "report.pdf")
        print("Allowed path:", safe_target)
        for bad in ["../etc/passwd", "....//....//etc/passwd", "/etc/shadow"]:
            try:
                resolve_safe_upload_path(tmp_uploads, bad)
            except ValueError as exc:
                print("Blocked:", exc)
