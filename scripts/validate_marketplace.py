#!/usr/bin/env python3
"""Validate the Audienti marketplace catalog."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse


ALLOWED_INSTALLATION = {
    "NOT_AVAILABLE",
    "AVAILABLE",
    "INSTALLED_BY_DEFAULT",
}

ALLOWED_AUTHENTICATION = {
    "ON_INSTALL",
    "ON_USE",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def is_valid_git_repo_url(value: object) -> bool:
    if not isinstance(value, str) or not value:
        return False

    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        return False

    return parsed.path.endswith(".git")


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    marketplace_path = repo_root / ".agents" / "plugins" / "marketplace.json"

    try:
        marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing marketplace file: {marketplace_path}")
        return 1
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {marketplace_path}: {exc}")
        return 1

    if marketplace.get("name") != "audienti":
        fail("marketplace name must be 'audienti'")
        return 1

    interface = marketplace.get("interface")
    if not isinstance(interface, dict) or not isinstance(interface.get("displayName"), str):
        fail("interface.displayName must be a string")
        return 1

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list):
        fail("plugins must be an array")
        return 1

    seen_names: set[str] = set()

    for index, plugin in enumerate(plugins):
        if not isinstance(plugin, dict):
            fail(f"plugins[{index}] must be an object")
            return 1

        name = plugin.get("name")
        if not isinstance(name, str) or not name:
            fail(f"plugins[{index}].name must be a non-empty string")
            return 1

        if name in seen_names:
            fail(f"duplicate plugin entry: {name}")
            return 1
        seen_names.add(name)

        source = plugin.get("source")
        if not isinstance(source, dict):
            fail(f"{name}: source must be an object")
            return 1
        if source.get("source") != "url":
            fail(f"{name}: source.source must be 'url'")
            return 1
        if not is_valid_git_repo_url(source.get("url")):
            fail(f"{name}: source.url must be an absolute https git repository URL ending in .git")
            return 1

        policy = plugin.get("policy")
        if not isinstance(policy, dict):
            fail(f"{name}: policy must be an object")
            return 1
        if policy.get("installation") not in ALLOWED_INSTALLATION:
            fail(f"{name}: invalid policy.installation value")
            return 1
        if policy.get("authentication") not in ALLOWED_AUTHENTICATION:
            fail(f"{name}: invalid policy.authentication value")
            return 1

        category = plugin.get("category")
        if not isinstance(category, str) or not category.strip():
            fail(f"{name}: category must be a non-empty string")
            return 1

    print(f"Marketplace valid: {marketplace_path}")
    print(f"Plugin entries: {len(plugins)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
