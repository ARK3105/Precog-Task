import networkx as nx
import numpy as np
from collections import defaultdict
import infomap
import leidenalg
import igraph as ig



def apply_leiden_algorithm(countries):

    # Create the graph
    G = create_graph(countries)
    
    # Convert the NetworkX graph to an igraph object
    ig_graph = ig.Graph.from_networkx(G)
    
    # Apply the Leiden algorithm for community detection
    partition = leidenalg.find_partition(ig_graph, leidenalg.ModularityVertexPartition)
    
    # /// print all the communities
    print("Leiden Partition Communities:")
    print(partition)
    
    
    return partition

def directed_infomap(G):

    # Create mapping between node names and indices
    nodes = list(G.nodes())
    node_to_idx = {node: idx for idx, node in enumerate(nodes)}
    
    im = infomap.Infomap("--directed --two-level")
    
    # Add nodes first
    for node in nodes:
        im.add_node(node_to_idx[node])
    
    # Add edges to Infomap network
    for source, target in G.edges():
        im.add_link(node_to_idx[source], node_to_idx[target])
    
    # Run Infomap
    im.run()
    
    # Convert results to dictionary using original node names
    communities = {}
    for node in im.tree:
        if node.is_leaf:
            original_node = nodes[node.node_id]
            communities[original_node] = node.module_id
    
    # print("Infomap Communities:", communities)  # Debugging
    return communities



def evaluate_directed_communities(G, communities):
 
    metrics = {}
    
    # 1. Directed Modularity
    def directed_modularity():
        m = G.number_of_edges()
        if m == 0:
            return 0
        
        Q = 0
        for u, v in G.edges():
            if communities[u] == communities[v]:
                k_in_u = G.in_degree(u)
                k_out_v = G.out_degree(v)
                Q += 1 - (k_in_u * k_out_v) / m
        
        return Q / m
     
    
    metrics['directed_modularity'] = directed_modularity()

    
    return metrics

def analyze_communities(G):
    results = {}
   
    print(f"\nRunning Infomap algorithm...")  # Debugging
    communities = directed_infomap(G)
    metrics = evaluate_directed_communities(G, communities)
    results['Infomap'] = {
        'communities': communities,
        'metrics': metrics
    }
    
    return results

def create_graph(countries):
    G = nx.DiGraph()
 
    G.add_nodes_from(countries)
    
    for source in countries:
        for target in countries:
            if source != target and source[-1].lower() == target[0].lower():
                G.add_edge(source, target)
    
    return G



def print_community_results(communities):

    # Reverse the community mapping so we can group countries by community
    community_groups = defaultdict(list)
    for country, community in communities.items():
        community_groups[community].append(country)
    
    # Print each community and its countries
    for community, countries in sorted(community_groups.items()):
        print(f"\nCommunity {community }:")
        print(", ".join(sorted(countries)))


def analyze_communities_2(partition, countries,G):

    # Get the membership list
    membership = partition.membership
    
    # Count number of communities
    num_communities = len(set(membership))
    
    # Group countries by community
    communities = {}
    for idx, community_id in enumerate(membership):
        if community_id not in communities:
            communities[community_id] = []
        communities[community_id].append(countries[idx])
    
    # Calculate modularity
    modularity = partition.quality()

    analysis = {
        "num_communities": num_communities,
        "communities": communities,
        "modularity": modularity
    }
    return analysis

def main():
    countries = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", 
        "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", 
        "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", 
        "Belarus", "Belgium", "Belize", "Benin", "Bhutan", 
        "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", 
        "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", 
        "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", 
        "China", "Colombia", "Comoros", "Congo", "Costa Rica", 
        "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", 
        "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", 
        "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", 
        "Eswatini", "Ethiopia", "Fiji", "Finland", "France", 
        "Gabon", "Gambia", "Georgia", "Germany", "Ghana", 
        "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", 
        "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", 
        "India", "Indonesia", "Iran", "Iraq", "Ireland", 
        "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", 
        "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", 
        "South Korea", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", 
        "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", 
        "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", 
        "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", 
        "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", 
        "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", 
        "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", 
        "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", 
        "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", 
        "Paraguay", "Peru", "Philippines", "Poland", "Portugal", 
        "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", 
        "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", 
        "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", 
        "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", 
        "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", 
        "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", 
        "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", 
        "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", 
        "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", 
        "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", 
        "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]
   


    G = create_graph(countries)

    print("Starting community analysis...\n")
    results = analyze_communities(G)

      # Print community results for each algorithm
    for algo_name, result in results.items():
        print(f"\n{algo_name} Results:")
        print_community_results(result['communities'])
        print("\nMetrics:")
        for metric, value in result['metrics'].items():
            print(f"{metric}: {value:.4f}")
            
    
    # Detect communities
    partition = apply_leiden_algorithm(countries)
    
    # Analyze results
    analysis = analyze_communities_2(partition, countries,G)
    
    # Print results
    print(f"Number of communities: {analysis['num_communities']}")
    print(f"Modularity score: {analysis['modularity']:.4f}")
    
    # Print members of each community
    for community_id, members in analysis['communities'].items():
        print(f"\nCommunity {community_id}:")
        print(members)



if __name__ == "__main__":
    main()
