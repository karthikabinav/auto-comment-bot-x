"""Script that automatically adds a comment to any new issue created."""
import os
import requests

def add_comment(owner, repo, issue_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    data = {"body": "Thank you for your contribution!"}
    return requests.post(url, headers=headers, json=data)

if __name__ == "__main__":
    token = os.environ.get("GITHUB_TOKEN")
    print("Auto-comment bot ready: Thank you for your contribution!")
