"""Script that automatically adds a comment to any new issue created."""
import os
from github import Github

COMMENT = "Thank you for your contribution!"

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    issue_number = int(os.environ.get("ISSUE_NUMBER", "0"))
    if token and repo_name and issue_number:
        repo = Github(token).get_repo(repo_name)
        repo.get_issue(number=issue_number).create_comment(COMMENT)

if __name__ == "__main__":
    main()
