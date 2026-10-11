# Automated Comment Bot
# Adds comment Thank you for your contribution! to any new issue created.
# In GitHub Actions this is handled by .github/workflows/auto-comment.yml.
# This script documents the same logic using the GitHub API:
# POST /repos/{owner}/{repo}/issues/{issue_number}/comments
# body: Thank you for your contribution!
COMMENT_BODY = "Thank you for your contribution!"
print(COMMENT_BODY)
