"""Automatically adds a comment to any new issue. Used by the GitHub Actions workflow on issues: opened."""
import os, sys, requests

def add_comment(owner, repo, issue_number):
    token = os.environ.get("GITHUB_TOKEN")
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    return requests.post(url, json={"body": "Thank you for your contribution!"}, headers=headers)

if __name__ == "__main__":
    add_comment(os.environ["GITHUB_REPOSITORY"].split("/")[0], os.environ["GITHUB_REPOSITORY"].split("/")[1], int(sys.argv[1]))
