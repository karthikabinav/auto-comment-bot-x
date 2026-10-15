"""Script that automatically adds a comment to a new issue."""
import os

COMMENT_BODY = "Thank you for your contribution!"


def main():
    # In GitHub Actions, the workflow in .github/workflows/auto-comment.yml
    # runs on issues.opened and posts COMMENT_BODY via the GitHub API.
    # This file documents the comment text used by that automation.
    print(COMMENT_BODY)


if __name__ == "__main__":
    main()
