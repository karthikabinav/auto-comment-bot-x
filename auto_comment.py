#!/usr/bin/env python3
"""Auto-comment bot: adds a comment to a new issue."""
import os, sys
COMMENT = "Thank you for your contribution!"

def add_comment(owner, repo, issue_number, token):
    import urllib.request, json
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    data = json.dumps({"body": COMMENT}).encode()
    req = urllib.request.Request(url, data=data, headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json", "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode()

if __name__ == "__main__":
    print(COMMENT)
    print("Auto-comment bot ready: Thank you for your contribution!")
