"""
Automated Comment Bot
Adds a comment 'Thank you for your contribution!' to any new issue created.
"""
import os

def add_comment_to_issue(owner, repo, issue_number):
    """Simulated function to add automated comment to a new issue."""
    # In real GitHub Actions, this uses github.rest.issues.createComment
    # For local testing, this represents the automation logic
    comment_body = "Thank you for your contribution!"
    print(f"Adding comment to {owner}/{repo}#{issue_number}: {comment_body}")
    return comment_body

if __name__ == "__main__":
    # Example usage - triggered on new issue event
    print("Auto Comment Bot ready - will comment on new issues")
