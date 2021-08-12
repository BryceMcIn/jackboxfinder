# JackBoxFinder
A script to generate and test room codes for jackbox games

# Requirements
- Python 3.6+
- Requests (latest)

# Todo
- Make asyncronous to find valid roomcodes faster
- Strings library not needed. Will remove
- Print if the game is in progress or not
- Print if the game is joinable or not

# Usage
When the script is ran, it will start generating and testing room codes by sending a GET request to the API url. If a valid room is found, the following will print in console:

- " HIT!!! : [Room code] "
