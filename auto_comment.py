"""Script that automatically adds a comment to any new issue."""
import os
from github import Github

COMMENT_BODY = "Thank you for your contribution!"

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    issue_number = int(os.environ.get("ISSUE_NUMBER", "0"))
    if not token or not repo_name or not issue_number:
        return
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    issue.create_comment(COMMENT_BODY)

if __name__ == "__main__":
    main()
