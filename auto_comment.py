"""Automated Comment Bot - adds a thank you comment to new issues."""
import os
from github import Github

def add_comment(owner, repo, issue_number):
    token = os.environ.get("GITHUB_TOKEN")
    gh = Github(token)
    issue = gh.get_repo(f"{owner}/{repo}").get_issue(issue_number)
    issue.create_comment("Thank you for your contribution!")

if __name__ == "__main__":
    print("Thank you for your contribution!")
