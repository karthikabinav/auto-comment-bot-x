#!/usr/bin/env python3
"""Auto Comment Bot.

A learning script that automatically posts a "Thank you for your
contribution!" comment on GitHub issues using the REST API.

Configuration via environment variables:
    GITHUB_TOKEN       - personal access token with repo scope (keep secret,
                         e.g. load it from an *untracked* .env file)
    GITHUB_REPOSITORY  - "owner/repo"

Usage:
    GITHUB_TOKEN=<token> GITHUB_REPOSITORY=owner/repo python3 comment_bot.py 1 2 3

The production automation for this repo is .github/workflows/auto-comment.yml,
which runs this same logic automatically whenever a new issue is opened.
"""

import json
import os
import sys
import urllib.request

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN")
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-comment-bot-x")
MESSAGE = "Thank you for your contribution!"


def add_comment(issue_number):
    url = f"{API}/repos/{REPOSITORY}/issues/{issue_number}/comments"
    payload = json.dumps({"body": MESSAGE}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.load(resp)


def main():
    if not TOKEN:
        sys.exit("error: GITHUB_TOKEN is not set (never commit it - load from a .env file in .gitignore)")
    numbers = sys.argv[1:] or os.environ.get("ISSUE_NUMBERS", "").split(",")
    if not numbers or numbers == [""]:
        sys.exit("usage: comment_bot.py <issue_number> [<issue_number> ...]")
    for number in numbers:
        number = str(number).strip()
        if not number:
            continue
        status, comment = add_comment(number)
        print(f"issue #{number}: HTTP {status} -> comment id {comment[id]}")


if __name__ == "__main__":
    main()
