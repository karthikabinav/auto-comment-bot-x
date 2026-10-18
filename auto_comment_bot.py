# Automated Comment Bot script
# Adds comment 'Thank you for your contribution!' to any new issue created.
import os
from github import Github

def add_comment(owner, repo, issue_number):
    g = Github(os.environ.get("GITHUB_TOKEN"))
    repository = g.get_repo(f"{owner}/{repo}")
    issue = repository.get_issue(number=issue_number)
    issue.create_comment("Thank you for your contribution!")

if __name__ == "__main__":
    print("Auto Comment Bot ready - will comment: Thank you for your contribution!")
