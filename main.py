import follower_finder
import groupnodes
import Follower_Stats

# get a list of all users 

user_list = ["SarahCAndersen", "fowlcomics", "catana_comics", "Lunarbaboon", "Explosm", \
    "yasmine_surovec", "PhilippaRice", "enzocomics", "PDLComics", "HannahHillam", "shenanigansen",\
    "Oatmeal", "LoadingArtist", "JimBenton", "gemmacorrell", "MrLovenstein", "xkcdComic","JimLee","skottieyoung","beckycloonan"]


# follower_finder takes in the argument of the screen names of a list of twitter users and creates an edge list of all of their followers
# The function uses the twitter API to get follower data in the form of User IDs for each person on the list
# The function outputs this list into the file: 'network_edge.csv'

follower_finder.main_function(user_list)

# Group nodes takes in a very large edge list that was created from the follower_finder main function, and groups similar nodes together.
# It opens the file 'network_edge.csv' and outputs the file 'output_network.csv'
# It takes nodes that have the same sources and combines them into one single node
# The number of followers information is perserved by assigning each edge a weight according to the number of followers
# represented by that connection.

groupnodes.main_func()

# Follower stats takes in the user list, and prints an output to the terminal of the number of shared followers between every user
# The output is in the form of a 2D table, each cell represents the value:
# ( number of shared followers between i and j / number of followers of i) where i is the user in the row, and j is the 
# user in the column of that table. 

Follower_Stats.main_function(user_list)