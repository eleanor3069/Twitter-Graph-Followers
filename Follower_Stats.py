import pandas as pd
import networkx as nx



def find_share_users(G,personA,personB):
    if personA == personB: 
        return '-'

    personAdict = dict()
    personA_follower_count = 0
    personBdict = dict()
    personA_follower_iterator = G.successors(personA)
    personB_follower_iterator = G.successors(personB)

    for person in personA_follower_iterator:
        edge_data = G.get_edge_data(personA,person)
        edge_weight = edge_data['weight']
        personAdict[person] = edge_weight
        personA_follower_count += edge_weight

    for person in personB_follower_iterator:
        edge_data = G.get_edge_data(personB,person)
        edge_weight = edge_data['weight']
        personBdict[person] = edge_weight
    

    share_follower_count = 0 

    for  key, value in personAdict.items():
        result = personBdict.get(key)
        if result is not None:
            share_follower_count += value

    return share_follower_count / personA_follower_count

def main_function(user_list):

    df = pd.read_csv('output_network.csv')
    graphtype = nx.DiGraph()
    
    print('creating graph')
    G = nx.from_pandas_edgelist(df,edge_attr='weight',create_using= graphtype)

    print_string = 'share followers,'

    for user in user_list:
        print_string += user+',' 

    print_string = print_string[:-1]
    print(print_string)

    for userA in user_list: 
        print_string = ''
        print_string += userA + ","
        for userB in user_list:
            share_follower_result = find_share_users(G,userA,userB)
            print_string += str(share_follower_result) + ','

        print_string = print_string[:-1]
        print(print_string)

user_list = ["SarahCAndersen", "fowlcomics", "catana_comics", "Lunarbaboon", "Explosm", \
"yasmine_surovec", "PhilippaRice", "enzocomics", "PDLComics", "HannahHillam", "shenanigansen",\
 "Oatmeal", "LoadingArtist", "JimBenton", "gemmacorrell", "MrLovenstein", "xkcdComic","JimLee","skottieyoung","beckycloonan"]

main_function(user_list)