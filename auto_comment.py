"""Script that automatically adds a comment to a new issue."""
import os
import sys

# Uses GitHub API via curl-like logic in real usage; simplified for learning.
# When a new issue is created, this script adds: Thank you for your contribution!
COMMENT_BODY = "Thank you for your contribution!"

def add_comment(owner, repo, issue_number, token):
    import urllib.request, json
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    data = json.dumps({"body": COMMENT_BODY}).encode()
    req = urllib.request.Request(url, data=data, headers={"Authorization": f"token {token}", "Accept": "application/vnd.github+json", "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as resp:
        return resp.status

if __name__ == "__main__":
    print(COMMENT_BODY)
