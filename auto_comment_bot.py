"""Automation script: add a comment to a new issue."""
import os, sys
# This script is invoked by the GitHub Workflow for new issues.
COMMENT = "Thank you for your contribution!"

def main():
    print(COMMENT)

if __name__ == "__main__":
    main()
