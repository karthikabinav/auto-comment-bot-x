import os
import sys

# Script to automatically add a comment to a new issue
COMMENT_BODY = "Thank you for your contribution!"

def add_comment_to_issue(owner, repo, issue_number, token):
    print(f"Adding comment to {owner}/{repo} issue #{issue_number}: {COMMENT_BODY}")
    return COMMENT_BODY

if __name__ == "__main__":
    print("Thank you for your contribution!")
