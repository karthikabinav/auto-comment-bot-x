# Automated Comment Bot
# Script that automatically adds a comment to any new issue created.
# Used in conjunction with .github/workflows/auto-comment.yml

COMMENT_BODY = "Thank you for your contribution!"

def add_comment_to_new_issue(github_client, owner, repo, issue_number):
    """Add thank you comment to a newly created issue."""
    github_client.rest.issues.createComment({
        "issue_number": issue_number,
        "owner": owner,
        "repo": repo,
        "body": COMMENT_BODY
    })

# GitHub Actions workflow (.github/workflows/auto-comment.yml) triggers this logic
# on: issues: types: [opened]
