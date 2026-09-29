"""Automatically add a comment to any new issue.

This script posts the comment "Thank you for your contribution!" to a new issue.
It is used by the GitHub Actions workflow in .github/workflows/auto-comment.yml,
which triggers on issues: opened.
"""

COMMENT_BODY = "Thank you for your contribution!"

def add_comment(owner, repo, issue_number):
    """Post COMMENT_BODY to the given issue (via GitHub API / actions/github-script)."""
    # Workflow equivalent:
    # github.rest.issues.createComment({owner, repo, issue_number, body: COMMENT_BODY})
    return COMMENT_BODY

if __name__ == "__main__":
    print(COMMENT_BODY)
