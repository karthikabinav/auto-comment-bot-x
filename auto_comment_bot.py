#!/usr/bin/env python3
"""
Automated Comment Bot

This script demonstrates GitHub automation for adding comments to new issues.
It can be integrated with GitHub Actions to automatically comment
"Thank you for your contribution!" on every newly opened issue.
"""

import os
import requests

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO_OWNER = os.environ.get("REPO_OWNER", "karthikabinav")
REPO_NAME = os.environ.get("REPO_NAME", "auto-comment-bot-x")

def add_comment(issue_number, body="Thank you for your contribution!"):
    """Add a comment to a GitHub issue"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"body": body}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

if __name__ == "__main__":
    # Example usage for GitHub Actions
    issue_number = os.environ.get("ISSUE_NUMBER")
    if issue_number:
        result = add_comment(int(issue_number))
        print(f"Comment added to issue #{issue_number}")
    else:
        print("No issue number provided")
