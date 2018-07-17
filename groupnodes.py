import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import datetime

def groupFollowerList(G,searchDegree):
    #degreeList = [node for node in G.nodes if G.degree(node) == searchDegree and isinstance(node,int)]
    degreeList = [node for node in G.nodes if G.degree(node) == searchDegree and any(char.isdigit() for char in node)]

    if len(degreeList) > 0:
        sourceDictionary = dict()

        GedgeList = []

        for node in degreeList:
            predecessor_list = G.predecessors(node)
            sourceDictionary[node] = ""
            for predecessor_node in predecessor_list:
                sourceDictionary[node] = sourceDictionary[node] + predecessor_node + " & "
            sourceDictionary[node] = sourceDictionary[node][:-3]

        # Combine elements in the dictionary
        combinedDictionary = dict()

        for key, value in sourceDictionary.items():
            if not bool(combinedDictionary.get(value)):
                combinedDictionary[value] = []
                combinedDictionary[value].append(key)
            else:
                combinedDictionary[value].append(key)

        outputDictionary = dict()

        for key, value in combinedDictionary.items():
            if len(value) > 1:
                outputDictionary[key] = value

        return outputDictionary
    else:
        return dict()


def mergeNodes(G,nodeList,new_node):
    """
    Merges the selected `nodes` of the graph G into one `new_node`,
    meaning that all the edges that pointed to or from one of these
    `nodes` will point to or from the `new_node`.
    attr_dict and **attr are defined as in `G.add_node`.
    """
    
    if len(nodeList) > 1:

        G.add_node(new_node) # Add the 'merged' node

        addEdgeList = []

        combinedEdgeList = []

        for node in nodeList:
            successor_list = G.successors(node)
            predecessor_list = G.predecessors(node)
            for successor_node in successor_list:
                weight_data = G.get_edge_data(new_node,successor_node)['weight']
                addEdgeList.append([node,successor_node,weight_data])
            for predecessor_node in predecessor_list:
                weight_data = G.get_edge_data(predecessor_node,node)['weight']
                addEdgeList.append([predecessor_node,new_node,weight_data])

        for n1,n2,data in addEdgeList:
            matching = [elem for elem in combinedEdgeList if n1 in elem and n2 in elem]
            if len(matching) == 1:
                matching_index = combinedEdgeList.index(matching[0])
                combinedEdgeList[matching_index][2] = combinedEdgeList[matching_index][2] + 1
            elif len(matching) == 0:
                combinedEdgeList.append([n1,n2,data])
            else: 
                print("Error state occured in combinedEdgeList!")

        for n1,n2,weightValue in combinedEdgeList:
            G.add_edge(n1,n2,weight=weightValue)
        
        for n in nodeList: # remove the merged nodes
            G.remove_node(n)

def combineNodes(G,startDegree):
    for x in reversed(range(1,startDegree + 1)):
        print("{} - Grouping followers for degree: {}".format(datetime.datetime.now(),x))
        mergeNodeDictionary = groupFollowerList(G,x)
        print("Dictionary contains {} lists".format(len(mergeNodeDictionary)))

        totalListLength = len(mergeNodeDictionary)
        currentListIndex = 0
        for key, value in mergeNodeDictionary.items():
            print("{} - ({}/{}) Merging {} nodes for: {}".format(datetime.datetime.now(),currentListIndex, totalListLength, len(value),key))
            mergeNodes(G,value,key + " - Followers")
            currentListIndex = currentListIndex + 1

        #print("{} - Saving network for recovery".format(datetime.datetime.now()))
        #with open('./network_saves/G_' + str(x) + '.pkl', 'wb') as output:
            #pickle.dump(G, output, pickle.HIGHEST_PROTOCOL)

def main_func():

    print("Loading network")
    df = pd.read_csv('network_edge.csv')
    print("Creating graph")
    Graphtype = nx.DiGraph()
    G = nx.from_pandas_edgelist(df, edge_attr='weight', create_using=Graphtype)

    combineNodes(G,20)

    df2 = nx.to_pandas_edgelist(G)
    df2.to_csv('output_network.csv',index=False)

    #pos=nx.spring_layout(G) # positions for all nodes
    #nx.draw(G,pos, with_labels = True)
    #labels = nx.get_edge_attributes(G,'weight')
    #nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    #plt.show()

