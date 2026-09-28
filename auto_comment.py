"""Automatically add a comment to any new issue. Used by the GitHub Actions workflow in .github/workflows/auto-comment.yml, which runs on issues: opened and posts the comment below."""

COMMENT_BODY = "Thank you for your contribution!"

# The workflow uses actions/github-script to call:
# github.rest.issues.createComment({owner, repo, issue_number, body: COMMENT_BODY})
