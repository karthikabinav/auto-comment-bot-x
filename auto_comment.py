#!/usr/bin/env python3
"""Automatically adds a comment to any new issue."""
import os
from github import Github

COMMENT = "Thank you for your contribution!"

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    issue_number = int(os.environ.get("ISSUE_NUMBER", "0"))
    if token and repo_name and issue_number:
        gh = Github(token)
        repo = gh.get_repo(repo_name)
        issue = repo.get_issue(number=issue_number)
        issue.create_comment(COMMENT)

if __name__ == "__main__":
    main()
