import os
import sys
from github import Github

def comment_on_issue(repo_name, issue_number):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set")
        sys.exit(1)
    g = Github(token)
    repo = g.get_repo(repo_name)
    issue = repo.get_issue(issue_number)
    issue.create_comment("Thank you for your contribution!")
    print(f"Commented on issue #{issue_number}")

if __name__ == "__main__":
    repo = os.getenv("GITHUB_REPOSITORY", "auto-comment-bot-x")
    issue_number = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.getenv("ISSUE_NUMBER", "1"))
    comment_on_issue(repo, issue_number)
