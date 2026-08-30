"""Automated Comment Bot - adds Thank you comment to new issues."""
import os
# This script demonstrates GitHub automation for adding comments to issues.
# In production, this logic runs via GitHub Actions (.github/workflows/auto-comment.yml)
# or via webhook handling.
COMMENT_BODY = "Thank you for your contribution!"

def get_comment_for_new_issue(issue_number):
    """Return comment payload for a new issue."""
    return {
        "issue_number": issue_number,
        "body": COMMENT_BODY
    }

if __name__ == "__main__":
    print(f"Bot ready. Comment message: {COMMENT_BODY}")
