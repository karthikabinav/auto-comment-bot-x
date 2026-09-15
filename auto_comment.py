#!/usr/bin/env python3
"""Auto comment bot: adds Thank you for your contribution! to new issues."""
import os, sys
from github import Github

COMMENT_BODY = 'Thank you for your contribution!'

def main():
    token = os.environ.get('GITHUB_TOKEN')
    repo_name = os.environ.get('GITHUB_REPOSITORY')
    issue_number = int(os.environ.get('ISSUE_NUMBER', sys.argv[1] if len(sys.argv)>1 else 0))
    if not token or not repo_name or not issue_number:
        print('Missing env vars'); return
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    issue.create_comment(COMMENT_BODY)
    print(f'Commented on issue #{issue_number}')

if __name__ == '__main__':
    main()
