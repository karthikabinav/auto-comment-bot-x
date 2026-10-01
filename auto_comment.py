"""Auto Comment Bot script.

Adds the comment 'Thank you for your contribution!' to a new issue.
"""

COMMENT_BODY = "Thank you for your contribution!"

def add_comment(owner, repo, issue_number, github_client):
    """Add thank-you comment to the given issue."""
    return github_client.rest.issues.create_comment(
        owner=owner,
        repo=repo,
        issue_number=issue_number,
        body=COMMENT_BODY,
    )

if __name__ == "__main__":
    print("Auto Comment Bot: ready to comment on new issues.")
    print(COMMENT_BODY)
