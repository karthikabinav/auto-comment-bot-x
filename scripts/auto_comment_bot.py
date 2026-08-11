# Automated Comment Bot
# This script demonstrates GitHub automation for adding comments to issues.
# Triggered by GitHub Actions workflow on issues: opened event.

comment_body = "Thank you for your contribution!"

def add_comment(issue_number):
    print(f"Posting comment to issue #{issue_number}: {comment_body}")
    return comment_body

if __name__ == "__main__":
    add_comment(1)
