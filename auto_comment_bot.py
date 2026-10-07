"""Automation script: add Thank you for your contribution to a new issue."""
import json
import os
import urllib.request
COMMENT_BODY = "Thank you for your contribution!"
def add_comment(owner, repo, issue_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    data = json.dumps({"body": COMMENT_BODY}).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req) as resp:
        return resp.status
if __name__ == "__main__":
    owner, repo = os.environ.get("REPO", "").split("/")
    issue_number = int(os.environ.get("ISSUE_NUMBER", "0"))
    token = os.environ.get("GITHUB_TOKEN", "")
    print(add_comment(owner, repo, issue_number, token))
