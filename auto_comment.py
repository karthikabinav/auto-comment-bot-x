import os
import sys

# Script to automatically add a comment to a new issue
# Listens for new issue events and adds: Thank you for your contribution!
COMMENT_BODY = "Thank you for your contribution!"

def add_comment_to_issue(owner, repo, issue_number, token):
    # This script is designed to be used with GitHub automation (e.g., via GitHub Actions)
    # In a real workflow, it would use the GitHub API to post the comment
    print(f"Adding comment to {owner}/{repo} issue #{issue_number}: {COMMENT_BODY}")
    return COMMENT_BODY

if __name__ == "__main__":
    print("Thank you for your contribution!")
