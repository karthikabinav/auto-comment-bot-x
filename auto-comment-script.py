import os
import sys
from github import Github

"""Automated Comment Bot Script
Automatically adds a comment "Thank you for your contribution!" to new issues."""

def add_comment_to_issue(token, repo_name, issue_number):
    g = Github(token)
    repo = g.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    issue.create_comment("Thank you for your contribution!")
    print(f"✓ Comment added to issue #{issue_number}")

if __name__ == "__main__":
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-comment-bot-x")
    issue_number = os.getenv("ISSUE_NUMBER")
    if not token or not issue_number:
        print("Missing GITHUB_TOKEN or ISSUE_NUMBER", file=sys.stderr)
        sys.exit(1)
    add_comment_to_issue(token, repo_name, int(issue_number))
