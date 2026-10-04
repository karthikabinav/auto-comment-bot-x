#!/usr/bin/env python3
"""Auto Comment Bot - automatically adds a comment to new GitHub issues."""

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
        sys.exit("error: GITHUB_TOKEN is not set")
    numbers = sys.argv[1:]
    if not numbers:
        sys.exit("usage: comment_bot.py <issue_number> [<issue_number> ...]")
    for number in numbers:
        status, comment = add_comment(number)
        print(f"issue #{number}: HTTP {status} -> comment id {comment.get(chr(105)+chr(100))}")

if __name__ == "__main__":
    main()
