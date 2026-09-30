# Auto Comment Bot script
# This script is invoked by GitHub Actions when a new issue is opened
# and adds the comment: Thank you for your contribution!
import os

COMMENT = "Thank you for your contribution!"

def main():
    print(COMMENT)

if __name__ == "__main__":
    main()
