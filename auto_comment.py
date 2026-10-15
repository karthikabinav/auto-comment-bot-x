#!/usr/bin/env python3
"""Automatically add a comment to a new issue."""
import os
import sys
import json
import urllib.request

COMMENT_BODY = "Thank you for your contribution!"

def add_comment(owner, repo, issue_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    data = json.dumps({"body": COMMENT_BODY}).encode()
    req = urllib.request.Request(url, data=data, headers={"Authorization": f"token {token}", "Accept": "application/vnd.github+json", "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode()

if __name__ == "__main__":
    owner = os.environ.get("GITHUB_REPOSITORY_OWNER", "karthikabinav")
    repo = "auto-comment-bot-x"
    issue_number = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    token = os.environ.get("GITHUB_TOKEN", "")
    print(f"Adding comment to issue #{issue_number}: {COMMENT_BODY}")
    if token:
        print(add_comment(owner, repo, issue_number, token))
