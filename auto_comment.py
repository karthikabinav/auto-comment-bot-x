#!/usr/bin/env python3
"""Script that automatically adds a comment to any new issue."""
import os
import sys

def add_comment(owner, repo, issue_number, body="Thank you for your contribution!"):
    # In GitHub Actions this is handled by the workflow; this function documents the comment text.
    print(f"Adding comment to {owner}/{repo}#{issue_number}: {body}")
    return body

if __name__ == "__main__":
    print("Thank you for your contribution!")
