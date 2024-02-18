import networkx as nx
from collections import OrderedDict

drugs_list = []
proteins_list = []
disjointed_proteins = []
Dict = {}

# Create an empty graph from networkx
G = nx.Graph()

# open the tsv file to read
with open ('DTIsubset.tsv','r') as file1:
    # go/ iterate  through each line of the file and strip and split except for the line having "Drug_name"
    for line in file1:
        if 'Drug_name' not in line:
            line = line.strip().split('\t')
            # add the drug names at 0th index
            drugs_list.append(line[0])
            # add the protein names at 1st index
            proteins_list.append(line[1])
            # add edges between drugs and proteins to complete te empty graph
            G.add_edge(line[0],line[1], weight=line[2])
            # print(drugs_list)

            # eliminate the duplicates using set
            drugs_list2 = list(set(drugs_list))
            proteins_list2 = list(set(proteins_list))

# print(drugs_list2)
# print(proteins_list2)

# find tau(X) - take x as the drug
# iterate through the drugs list and get the neighbors for each of the drug (neighbors-proteins)
# neighbors set = tau(X)
for drug in drugs_list2:
    list1_protein_neighbors = list(G.neighbors(drug))
    #print(list1_protein_neighbors)
    list1_set_tau_x = set(list1_protein_neighbors)
    #print(list1_set_tau_x)
    # seperate the proteins that are disjointed (no connectins)
    for protein in proteins_list2:
        if protein not in list1_set_tau_x:
                # get the neighbors of disjointed proteins - drugs
                list2_drug_neighbors = list(G.neighbors(protein))
                # print(list2_drug_neighbors)
                x = []
                # get the protein neighbors of drugs
                # neighbors set = tau bar y
                for element in list2_drug_neighbors:
                    list3_protein_neighbors = list(G.neighbors(element))
                    #print(list3_protein_neighbors)
                    set_list3_protein_neighbors = set(list3_protein_neighbors)
                    #print(set_list3_protein_neighbors)
                    x += set_list3_protein_neighbors
                    # print(x)
                    tau_bar_y = set(x)
                    #list3_union_set_tau_bar_y = set.union(set_list3_protein_neighbors)
                    #print(list3_union_set_tau_bar_y)

                    ans = set.intersection(list1_set_tau_x, tau_bar_y)
                    # print(ans)
                    # print(len(ans))
                    common_neighbor_score = len(ans)
        # print(common_neighbor_score)

                    Dict[drug,protein] = common_neighbor_score
# print(Dict)

descending_dict = OrderedDict(sorted(Dict.items(), key=lambda t: t[1], reverse= True))
print(descending_dict)







