"""
Automated Comment Bot - Example script for learning GitHub automation.
This script demonstrates how to automatically add a comment
Thank you for your contribution! to a newly created issue.
"""

# Example logic (pseudo-code for learning):
# When a new issue is created, call the GitHub API to add a comment.

COMMENT_BODY = "Thank you for your contribution!"

def get_comment_for_new_issue(issue_number):
    """Return the automated comment for a new issue."""
    print(f"New issue #{issue_number} detected.")
    print(f"Adding comment: {COMMENT_BODY}")
    return COMMENT_BODY

if __name__ == "__main__":
    # Example test
    for test_issue in [1, 2, 3]:
        get_comment_for_new_issue(test_issue)
