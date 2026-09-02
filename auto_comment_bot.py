# Automated Comment Bot
# This script demonstrates how to automatically add a comment
# "Thank you for your contribution!" to any new issue.
#
# Usage: Set up as a GitHub Action triggered on `issues: [opened]`
# or run manually with: python auto_comment_bot.py <owner> <repo> <issue_number>

import sys

COMMENT_BODY = "Thank you for your contribution!"

def get_comment_for_new_issue():
    """Return the automated comment for new issues."""
    return COMMENT_BODY

# Example GitHub Actions workflow (save as .github/workflows/auto-comment.yml):
# name: Auto Comment on New Issues
# on:
#   issues:
#     types: [opened]
# jobs:
#   comment:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/github-script@v6
#         with:
#           script: |
#             github.rest.issues.createComment({
#               issue_number: context.issue.number,
#               owner: context.repo.owner,
#               repo: context.repo.repo,
#               body: "Thank you for your contribution!"
#             })

if __name__ == "__main__":
    print(get_comment_for_new_issue())
