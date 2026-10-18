"""Automated Comment Bot: adds a comment to any new issue created."""
import os
import sys

COMMENT_BODY = "Thank you for your contribution!"

def add_comment(owner, repo, issue_number, token):
    import urllib.request
    import json
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    data = json.dumps({"body": COMMENT_BODY}).encode()
    req = urllib.request.Request(url, data=data, headers={"Authorization": f"token {token}", "Accept": "application/vnd.github+json", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode()

if __name__ == "__main__":
    # Usage: python auto_comment.py <owner> <repo> <issue_number>
    owner = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("REPO_OWNER", "karthikabinav")
    repo = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("REPO_NAME", "auto-comment-bot-x")
    issue_number = int(sys.argv[3]) if len(sys.argv) > 3 else int(os.environ.get("ISSUE_NUMBER", "0"))
    token = os.environ.get("GITHUB_TOKEN", "")
    if issue_number:
        print(add_comment(owner, repo, issue_number, token))
    else:
        print(COMMENT_BODY)
