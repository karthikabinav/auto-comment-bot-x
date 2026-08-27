#!/usr/bin/env python3
"""
Automated Comment Bot

A script to test GitHub automation for adding comments to issues.
Automatically adds a comment 'Thank you for your contribution!' to any new issue created.
"""
import os
import requests

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_OWNER = "karthikabinav"
REPO_NAME = "auto-comment-bot-x"
COMMENT_BODY = "Thank you for your contribution!"

def add_comment_to_issue(issue_number, body=COMMENT_BODY):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.post(url, json={"body": body}, headers=headers)
    response.raise_for_status()
    return response.json()

def handle_new_issue(issue_number):
    # This function is triggered when a new issue is created
    return add_comment_to_issue(issue_number, "Thank you for your contribution!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        handle_new_issue(int(sys.argv[1]))
