"""Script that automatically adds a comment to any new issue created."""
import os

COMMENT = "Thank you for your contribution!"

def add_comment_to_issue(owner, repo, issue_number):
    # In a real GitHub Action, this would call the GitHub API to post COMMENT
    # to the issue. The workflow in .github/workflows/auto-comment.yml
    # performs this via github.rest.issues.createComment with body=COMMENT.
    print(f"Adding comment to {owner}/{repo}#{issue_number}: {COMMENT}")
    return COMMENT

if __name__ == "__main__":
    issue_number = os.environ.get("ISSUE_NUMBER", "1")
    print(add_comment_to_issue(os.environ.get("REPO_OWNER", "karthikabinav"), os.environ.get("REPO_NAME", "auto-comment-bot-x"), issue_number))
