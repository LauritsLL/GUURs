## Update usernames in all repository README's

This little script uses the Github v3 API through the awesome library [PyGithub](https://github.com/PyGithub/PyGithub) to update ALL repositories in specified account to reflect a username change

## Installation

1. Clone repository. `git clone https://github.com/LauritsLL/Github-Username-Update-READMEs`
2. Install required packages: `pip3 install PyGithub requests`

Then `cd` into the repo and run the script using the command (assuming you have Python 3 installed):

`$ python3 update.py`

Here's a one-liner for the lazy:

`git clone https://github.com/LauritsLL/Github-Username-Update-READMEs && cd Github-Username-Update-READMEs && python3 update.py`