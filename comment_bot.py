import os
import requests

def add_comment(owner, repo, issue_number, body="Thank you for your contribution!", token=None):
    """Add a comment to a GitHub issue."""
    token = token or os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GitHub token required")
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"body": body}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    import sys
    # Usage: python comment_bot.py <owner> <repo> <issue_number> [comment]
    if len(sys.argv) < 4:
        print("Usage: python comment_bot.py <owner> <repo> <issue_number> [comment]")
        sys.exit(1)
    owner = sys.argv[1]
    repo = sys.argv[2]
    issue_number = int(sys.argv[3])
    comment = sys.argv[4] if len(sys.argv) > 4 else "Thank you for your contribution!"
    result = add_comment(owner, repo, issue_number, comment)
    print(f"Comment added: {result.get(\"html_url\")}")
