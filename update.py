"""
    Updates ALL Repositories associated to specified account
    and changes the username (all occurences) in ROOT FOLDER README (if found)
    to the new username specified.
"""
import base64
import github as gh
from pprint import pprint

# Github username.
old_username = input("Please enter OLD Github Username (Username to be removed from README's): ")
new_username = input("Please enter new Github Username (Your username after change): ")
passwd = input("Enter password for authentication of Github v3 API: ")

# Authenticate and instantiate PyGithub Object.
g = gh.Github(new_username, passwd)

# Get user by username.
user = g.get_user(new_username)

for repo in user.get_repos():
    print("UPDATING USERNAME IN REPO: {}\n".format(repo.name))
    readme_contents = base64.b64decode(repo.get_readme().content) # In bytes.

    # Change old_username to new_username in README.md in root folder.
    new_readme_contents = readme_contents.replace(old_username.encode(), 
        new_username.encode())
    
    # Then update the repo with a new commit.
    # NOTE: ASSUMING README IS PLACED IN ROOT FOLDER AND NAMED: 
    # 'README.md' OR 'README.txt'
    readme_file = None
    try:
        readme_file = repo.get_contents("README.md")
    except gh.GithubException:
        # Try with .txt instead.
        readme_file = repo.get_contents("README.txt")
    
    # Update file and make new commit.
    commit_message = "Updated README.md to reflect username change using script."
    repo.update_file(readme_file.path, commit_message, 
        new_readme_contents, readme_file.sha, branch="master")
    
    print("SUCCESSFULLY UPDATED\n\n")