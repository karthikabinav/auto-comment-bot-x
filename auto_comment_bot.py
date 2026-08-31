"""Automated Comment Bot - adds Thank you comment to new issues."""
import os
# This script demonstrates automation logic.
# In production, this runs via GitHub Actions on issue opened event.
# It posts 'Thank you for your contribution!' to any new issue.
COMMENT_BODY = "Thank you for your contribution!"

def get_comment_for_new_issue(issue_number):
    print(f"Adding comment to issue #{issue_number}: {COMMENT_BODY}")
    return COMMENT_BODY

if __name__ == "__main__":
    print("Auto Comment Bot ready. Listening for new issues...")
