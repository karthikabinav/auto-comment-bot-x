# Script that automatically adds a comment to any new issue created
# Comment: Thank you for your contribution!

def on_new_issue(owner, repo, issue_number):
    body = "Thank you for your contribution!"
    # In a real workflow this would call GitHub API: POST /repos/{owner}/{repo}/issues/{issue_number}/comments with body
    return body

if __name__ == "__main__":
    print("Thank you for your contribution!")
