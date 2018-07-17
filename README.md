# Shared Follower Finder

This repo contains scripts that are designed to determine the number of shared followers between different Twitter users.

Please look at: main.py for a **full** explanation of the different functions, and that file should be your entry point to using these scripts.

For a quick explanation: 
- **main.py** runs the different scripts
- **follower_finder.py** scrapes twitter follower data using the twitter API and stores it in a file
- **groupnodes.py** groups and simplifies this follower data for easier and faster processing
- **Follower_Stats.py** computes the percent shared followers for each user