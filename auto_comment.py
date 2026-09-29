import os
import sys

def get_comment_body():
    return "Thank you for your contribution!"

def add_comment_to_issue(owner, repo, issue_number, token=None):
    # Automation script that adds a comment to a newly created issue
    # In a GitHub Actions workflow, this corresponds to calling the GitHub API:
    # POST /repos/{owner}/{repo}/issues/{issue_number}/comments with body "Thank you for your contribution!"
    print(f"Adding comment to {owner}/{repo} issue #{issue_number}: {get_comment_body()}")
    return get_comment_body()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        owner, repo, issue_number = sys.argv[1], sys.argv[2], int(sys.argv[3])
        add_comment_to_issue(owner, repo, issue_number)
    else:
        print("Usage: python auto_comment.py <owner> <repo> <issue_number>")
