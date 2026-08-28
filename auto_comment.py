"""
Automated Comment Bot script.
Automatically adds a comment 'Thank you for your contribution!' to any new issue created.
This script is intended to be used by GitHub Actions workflow (.github/workflows/auto-comment.yml)
or can be run manually with GITHUB_TOKEN, REPO_OWNER, REPO_NAME, ISSUE_NUMBER env vars.
"""
import os
import requests

def add_issue_comment(owner, repo, issue_number, token, body="Thank you for your contribution!"):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    response = requests.post(url, json={"body": body}, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    add_issue_comment(
        os.environ["REPO_OWNER"],
        os.environ["REPO_NAME"],
        int(os.environ["ISSUE_NUMBER"]),
        os.environ["GITHUB_TOKEN"],
    )
    print("Comment added: Thank you for your contribution!")
