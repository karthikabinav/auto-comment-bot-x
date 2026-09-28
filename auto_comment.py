"""Script that automatically adds a comment to any new issue created."""
import os
import sys
from github import Github

COMMENT_BODY = "Thank you for your contribution!"

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    issue_number = int(os.environ.get("ISSUE_NUMBER", sys.argv[1] if len(sys.argv) > 1 else 0))
    client = Github(token)
    repo = client.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    issue.create_comment(COMMENT_BODY)
    print(f"Added comment to issue #{issue_number}: {COMMENT_BODY}")

if __name__ == "__main__":
    main()
