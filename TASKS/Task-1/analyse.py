import networkx as nx
import collections
from collections import Counter


def create_country_graph(countries):
    G = nx.DiGraph()
    G.add_nodes_from(countries)
    
    for source in countries:
        for target in countries:
            if source != target and source[-1].lower() == target[0].lower():
                G.add_edge(source, target)
    
    return G

def find_last_letter_bottlenecks(G):
        letter_counts = collections.defaultdict(int)
        for country in G.nodes():
            letter_counts[country[-1].lower()] += 1
        return dict(sorted(letter_counts.items(), key=lambda x: x[1]))
    
    
def find_bottleneck_letters(G):
    letter_counts = collections.defaultdict(int)
    for country in G.nodes():
        letter_counts[country[0].lower()] += 1
    return dict(sorted(letter_counts.items(), key=lambda x: x[1]))

def find_cyclic_loops(G):
    cycles = []
    for node in G.nodes():
        for path in nx.simple_cycles(G):
            if len(path) > 1:
                cycles.append(path)
    return cycles

def find_shortest_elimination_paths(G):
    out_degrees = dict(G.out_degree())
    sink_nodes = [node for node, out_degree in out_degrees.items() if out_degree == 0]
    elimination_paths = {}
    for country in G.nodes():
        if country not in sink_nodes:
            try:
                elimination_paths[country] = min(len(path) for path in nx.all_simple_paths(G, source=country, target=sink_nodes))
            except nx.exception.NetworkXNoPath:
                elimination_paths[country] = float('inf')
    return elimination_paths

def find_high_to_low_degree_connections(G):
    degree_pairs = []
    for source, target in G.edges():
        source_degree = G.out_degree(source)
        target_degree = G.out_degree(target)
        if source_degree > target_degree:
            degree_pairs.append((source, target))
    return degree_pairs

def find_smallest_sccs(G):
    sccs = sorted(nx.strongly_connected_components(G), key=len)
    return sccs[:5]

def find_high_outdegree_variance_countries(G):
    outdegrees = dict(G.out_degree())
    variance = {country: (degree - sum(outdegrees.values()) / len(outdegrees))**2 for country, degree in outdegrees.items()}
    return sorted(variance.items(), key=lambda x: x[1], reverse=True)[:5]

def find_blocking_country_pairs(G):
    blocking_pairs = []
    for source, target in G.edges():
        if source[-1].lower() == target[0].lower() and target[-1].lower() == source[0].lower():
            blocking_pairs.append((source, target))
    return blocking_pairs

def find_most_diverse_outdegree_countries(G):
    outdegrees = dict(G.out_degree())
    diversity = {country: len(set(country[-1].lower() for neighbor, _ in G.out_edges(country))) for country in G.nodes()}
    return sorted(diversity.items(), key=lambda x: x[1], reverse=True)[:5]

def find_letter_clusters(G):
    letter_clusters = collections.defaultdict(list)
    for country in G.nodes():
        letter_clusters[country[0].lower()].append(country)
    return dict(letter_clusters)


def find_last_letter_clusters(G):
    # Initialize an empty dictionary to store clusters by last letter
    last_letter_clusters = {}
    
    for country in G.nodes():
        # Get the last letter of the country name (strip spaces, convert to lowercase)
        last_letter = country.strip()[-1].lower()
        
        # Add the country to the appropriate cluster
        if last_letter not in last_letter_clusters:
            last_letter_clusters[last_letter] = []
        last_letter_clusters[last_letter].append(country)
    
    return last_letter_clusters

def find_high_betweenness_to_degree_ratio(G):
    betweenness = nx.betweenness_centrality(G)
    degree = nx.degree_centrality(G)
    ratios = {country: betweenness[country] / degree[country] for country in G.nodes()}
    return sorted(ratios.items(), key=lambda x: x[1], reverse=True)[:5]

def find_high_closeness_variance_countries(G):
    closeness = nx.closeness_centrality(G)
    variance = {country: (closeness[country] - sum(closeness.values()) / len(closeness))**2 for country in G.nodes()}
    return sorted(variance.items(), key=lambda x: x[1], reverse=True)[:5]

def find_gateway_countries(G):
    wcc = [comp for comp in nx.weakly_connected_components(G)]
    gateway_countries = set()
    for i in range(len(wcc)):
        for j in range(i+1, len(wcc)):
            for country in wcc[i]:
                for neighbor in G.neighbors(country):
                    if neighbor in wcc[j]:
                        gateway_countries.add(country)
                        gateway_countries.add(neighbor)
    return list(gateway_countries)

def find_balanced_connection_countries(G):
    in_degrees = dict(G.in_degree())
    out_degrees = dict(G.out_degree())
    balanced = {country: abs(in_degrees[country] - out_degrees[country]) for country in G.nodes()}
    return sorted(balanced.items(), key=lambda x: x[1])[:5]

def find_high_incoming_to_outgoing_ratio(G):
    in_degrees = dict(G.in_degree())
    out_degrees = dict(G.out_degree())
    ratios = {country: in_degrees[country] / out_degrees[country] for country in G.nodes()}
    return sorted(ratios.items(), key=lambda x: x[1], reverse=True)[:5]

def find_sink_connection_countries(G):
    out_degrees = dict(G.out_degree())
    sink_nodes = [node for node, out_degree in out_degrees.items() if out_degree == 0]
    sink_connections = {country: sum(1 for neighbor in G.neighbors(country) if neighbor in sink_nodes) for country in G.nodes()}
    return sorted(sink_connections.items(), key=lambda x: x[1], reverse=True)[:5]

def find_gateway_connection_countries(G):
    out_degrees = dict(G.out_degree())
    gateway_nodes = find_gateway_countries(G)
    gateway_connections = {country: sum(1 for neighbor in G.neighbors(country) if neighbor in gateway_nodes) for country in G.nodes()}
    return sorted(gateway_connections.items(), key=lambda x: x[1], reverse=True)[:5]

def find_high_degree_connection_countries(G):
    out_degrees = dict(G.out_degree())
    high_degree_nodes = {country for country, degree in out_degrees.items() if degree > 1}
    high_degree_connections = {country: sum(1 for neighbor in G.neighbors(country) if neighbor in high_degree_nodes) for country in G.nodes()}
    return sorted(high_degree_connections.items(), key=lambda x: x[1], reverse=True)[:5]

def find_low_degree_connection_countries(G):
    out_degrees = dict(G.out_degree())
    low_degree_nodes = {country for country, degree in out_degrees.items() if degree == 1}
    low_degree_connections = {country: sum(1 for neighbor in G.neighbors(country) if neighbor in low_degree_nodes) for country in G.nodes()}
    return sorted(low_degree_connections.items(), key=lambda x: x[1], reverse=True)[:5]

def find_high_betweenness_connection_countries(G):
    out_degrees = dict(G.out_degree())
    betweenness = nx.betweenness_centrality(G)
    high_betweenness_nodes = {country for country, value in betweenness.items() if value > 0.1}
    high_betweenness_connections = {country: sum(1 for neighbor in G.neighbors(country) if neighbor in high_betweenness_nodes) for country in G.nodes()}
    return sorted(high_betweenness_connections.items(), key=lambda x: x[1], reverse=True)[:5]

def find_low_betweenness_connection_countries(G):
    out_degrees = dict(G.out_degree())
    betweenness = nx.betweenness_centrality(G)
    low_betweenness_nodes = {country for country, value in betweenness.items() if value < 0.01}
    low_betweenness_connections = {country: sum(1 for neighbor in G.neighbors(country) if neighbor in low_betweenness_nodes) for country in G.nodes()}
    return sorted(low_betweenness_connections.items(), key=lambda x: x[1], reverse=True)[:5]


def find_strategic_countries_from_graph(G):
    # Extract country names from graph nodes
    country_list = list(G.nodes)    

    # Count frequency of last letters
    last_letters = [country[-1].lower() for country in country_list]
    last_letter_counts = Counter(last_letters)

    # Count frequency of starting letters
    start_letters = [country[0].lower() for country in country_list]
    start_letter_counts = Counter(start_letters)

    # Identify **strategic letters**: High last-letter count, Low start-letter count
    strategic_letters = {
        letter for letter, count in last_letter_counts.items()
        if count > 1 and start_letter_counts.get(letter, 0) < 2  # Rare as start letter
    }

    # Find **strategic countries** ending in these letters
    strategic_countries = [
        country for country in country_list if country[-1].lower() in strategic_letters
    ]

    return strategic_countries, strategic_letters



def call_all_functions(G):
    bottleneck_letters = find_bottleneck_letters(G)
    print(f"All 26 bottleneck letters: {', '.join(f'{letter}: {count}' for letter, count in list(bottleneck_letters.items())[-26:])}")
    
    last_letter_bottlenecks = find_last_letter_bottlenecks(G)
    print(f"All 26 bottleneck letters: {', '.join(f'{letter}: {count}' for letter, count in list(last_letter_bottlenecks.items())[-26:])}")

    
    print("Letters that do not appear as the first letter of any country:")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in bottleneck_letters:
            print(letter.upper(), end=" ")
    print()
    
    print("Letters that do not appear as the last letter of any country:")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in last_letter_bottlenecks:
            print(letter.upper(), end=" ")
    print()
    


    letter_clusters = find_letter_clusters(G)
    print("Clusters of countries by starting letter:")
    for letter, countries in sorted(letter_clusters.items(), key=lambda item: len(item[1])):
        print(f"{letter.upper()}: {', '.join(sorted(countries))}")  # Sort countries alphabetically within each cluster

        
    # Print the clusters by last letter 
    last_letter_clusters = find_last_letter_clusters(G)
    print("\nClusters of countries by last letter:")
    for letter, countries in sorted(last_letter_clusters.items(), key=lambda item: len(item[1])):
        print(f"{letter.upper()}: {', '.join(sorted(countries))}")  # Sort countries alphabetically within each cluster
    
    
    
    strategic_countries, strategic_letters = find_strategic_countries_from_graph(G)
    print("Strategic Letters:", strategic_letters)
    print("Strategic Countries:", strategic_countries)
    
    # cyclic_loops = find_cyclic_loops(G)
    # if cyclic_loops:
    #     print("Found cyclic loops in the game:")
    #     for loop in cyclic_loops:
    #         print(f"- {' -> '.join(loop)}")
    # else:
    #     print("No cyclic loops found in the game.")

    # elimination_paths = find_shortest_elimination_paths(G)
    # print("Top 5 countries with the shortest paths to elimination:")
    # for country, path_length in sorted(elimination_paths.items(), key=lambda x: x[1])[:5]:
    #     print(f"{country}: {path_length} steps to a dead-end")

    high_to_low_connections = find_high_to_low_degree_connections(G)
    print("Top 5 high-degree to low-degree country connections:")
    for source, target in high_to_low_connections[:5]:
        print(f"{source} -> {target}")

    smallest_sccs = find_smallest_sccs(G)
    print(f"The 5 smallest strongly connected components have {', '.join(str(len(scc)) for scc in smallest_sccs)} countries each.")

    high_outdegree_countries = find_high_outdegree_variance_countries(G)
    print("Countries with the highest variance in outgoing connections:")
    for country, variance in high_outdegree_countries:
        print(f"{country}: {variance:.2f}")

    # blocking_pairs = find_blocking_country_pairs(G)
    # print("Country pairs that block each other:")
    # for source, target in blocking_pairs:
    #     print(f"{source} <-> {target}")

    diverse_countries = find_most_diverse_outdegree_countries(G)
    print("Countries with the most diverse outgoing connections:")
    for country, diversity in diverse_countries:
        print(f"{country}: {diversity} unique outgoing options")
    

    

    high_ratio_countries = find_high_betweenness_to_degree_ratio(G)
    print("Countries with the highest betweenness-to-degree ratio:")
    for country, ratio in high_ratio_countries:
        print(f"{country}: {ratio:.2f}")

    high_variance_countries = find_high_closeness_variance_countries(G)
    print("Countries with the highest variance in closeness centrality:")
    for country, variance in high_variance_countries:
        print(f"{country}: {variance:.2f}")

    gateway_countries = find_gateway_countries(G)
    print(f"The {len(gateway_countries)} gateway countries are: {', '.join(gateway_countries)}")

    balanced_countries = find_balanced_connection_countries(G)
    print("Countries with the most balanced incoming and outgoing connections:")
    for country, diff in balanced_countries:
        print(f"{country}: {diff} difference")

    high_incoming_ratio_countries = find_high_incoming_to_outgoing_ratio(G)
    print("Countries with the highest ratio of incoming to outgoing connections:")
    for country, ratio in high_incoming_ratio_countries:
        print(f"{country}: {ratio:.2f}")

    sink_connection_countries = find_sink_connection_countries(G)
    print("Countries with the most outgoing connections to sink nodes:")
    for country, count in sink_connection_countries:
        print(f"{country}: {count} connections")

    gateway_connection_countries = find_gateway_connection_countries(G)
    print("Countries with the most outgoing connections to gateway nodes:")
    for country, count in gateway_connection_countries:
        print(f"{country}: {count} connections")

    high_degree_connection_countries = find_high_degree_connection_countries(G)
    print("Countries with the most outgoing connections to high-degree nodes:")
    for country, count in high_degree_connection_countries:
        print(f"{country}: {count} connections")

    low_degree_connection_countries = find_low_degree_connection_countries(G)
    print("Countries with the most outgoing connections to low-degree nodes:")
    for country, count in low_degree_connection_countries:
        print(f"{country}: {count} connections")

    high_betweenness_connection_countries = find_high_betweenness_connection_countries(G)
    print("Countries with the most outgoing connections to high-betweenness nodes:")
    for country, count in high_betweenness_connection_countries:
        print(f"{country}: {count} connections")

    low_betweenness_connection_countries = find_low_betweenness_connection_countries(G)
    print("Countries with the most outgoing connections to low-betweenness nodes:")
    for country, count in low_betweenness_connection_countries:
        print(f"{country}: {count} connections")

def main():
    countries = [
    'Tokyo', 'Delhi', 'Shanghai', 'Dhaka', 'Sao Paulo', 'Cairo', 'Mexico City',
    'Beijing', 'Mumbai', 'Osaka', 'Chongqing', 'Karachi', 'Kinshasa', 'Lagos',
    'Istanbul', 'Buenos Aires', 'Kolkata', 'Manila', 'Guangzhou', 'Tianjin',
    'Lahore', 'Bangalore', 'Rio de Janeiro', 'Shenzhen', 'Moscow', 'Chennai',
    'Bogota', 'Jakarta', 'Lima', 'Paris', 'Bangkok', 'Hyderabad', 'Seoul', 'Nanjing',
    'Chengdu', 'London', 'Luanda', 'Tehran', 'Ho Chi Minh City', 'Nagoya', 'Xi-an',
    'Ahmedabad', 'Wuhan', 'Kuala Lumpur', 'Hangzhou', 'Suzhou', 'Surat', 'Dar es Salaam',
    'New York City', 'Baghdad', 'Shenyang', 'Riyadh', 'Hong Kong', 'Foshan', 'Dongguan',
    'Pune', 'Santiago', 'Haerbin', 'Madrid', 'Khartoum', 'Toronto', 'Johannesburg',
    'Belo Horizonte', 'Dalian', 'Singapore', 'Qingdao', 'Zhengzhou', 'Ji nan Shandong',
    'Abidjan', 'Barcelona', 'Yangon', 'Addis Ababa', 'Alexandria', 'Saint Petersburg',
    'Nairobi', 'Chittagong', 'Guadalajara', 'Fukuoka', 'Ankara', 'Hanoi', 'Melbourne',
    'Monterrey', 'Sydney', 'Changsha', 'Urumqi', 'Cape Town', 'Jiddah', 'Brasilia', 'Kunming',
    'Changchun', 'Kabul', 'Hefei', 'Yaounde', 'Ningbo', 'Shantou', 'New Taipei', 'Tel Aviv',
    'Kano', 'Shijiazhuang', 'Montreal', 'Rome', 'Jaipur', 'Recife', 'Nanning', 'Fortaleza',
    'Kozhikode', 'Porto Alegre', 'Taiyuan Shanxi', 'Douala', 'Ekurhuleni', 'Malappuram',
    'Medellin', 'Changzhou', 'Kampala', 'Antananarivo', 'Lucknow', 'Abuja', 'Nanchang',
    'Wenzhou', 'Xiamen', 'Ibadan', 'Fuzhou Fujian', 'Salvador', 'Casablanca', 'Tangshan Hebei',
    'Kumasi', 'Curitiba', 'Bekasi', 'Faisalabad', 'Los Angeles', 'Guiyang', 'Port Harcourt',
    'Thrissur', 'Santo Domingo', 'Berlin', 'Asuncion', 'Dakar', 'Kochi', 'Wuxi', 'Busan',
    'Campinas', 'Mashhad', 'Sanaa', 'Puebla', 'Indore', 'Lanzhou', 'Ouagadougou', 'Kuwait City',
    'Lusaka', 'Kanpur', 'Durban', 'Guayaquil', 'Pyongyang', 'Milan', 'Guatemala City', 'Athens',
    'Depok', 'Izmir', 'Nagpur', 'Surabaya', 'Handan', 'Coimbatore', 'Huaian', 'Port-au-Prince',
    'Zhongshan', 'Dubai', 'Bamako', 'Mbuji-Mayi', 'Kiev', 'Lisbon', 'Weifang', 'Caracas',
    'Thiruvananthapuram', 'Algiers', 'Shizuoka', 'Lubumbashi', 'Cali', 'Goiania', 'Pretoria',
    'Shaoxing', 'Incheon', 'Yantai', 'Zibo', 'Huizhou', 'Manchester', 'Taipei', 'Mogadishu',
    'Brazzaville', 'Accra', 'Bandung', 'Damascus', 'Birmingham', 'Vancouver', 'Toluca de Lerdo',
    'Luoyang', 'Sapporo', 'Chicago', 'Tashkent', 'Patna', 'Bhopal', 'Tangerang', 'Nantong',
    'Brisbane', 'Tunis', 'Peshawar', 'Medan', 'Gujranwala', 'Baku', 'Hohhot', 'San Juan',
    'Belem', 'Rawalpindi', 'Agra', 'Manaus', 'Kannur', 'Beirut', 'Maracaibo', 'Liuzhou',
    'Visakhapatnam', 'Baotou', 'Vadodara', 'Barranquilla', 'Phnom Penh', 'Sendai', 'Taoyuan',
    'Xuzhou', 'Houston', 'Aleppo', 'Tijuana', 'Esfahan', 'Nashik', 'Vijayawada', 'Amman',
    'Putian', 'Multan', 'Grande Vitoria', 'Wuhu Anhui', 'Mecca', 'Kollam', 'Naples', 'Daegu',
    'Conakry', 'Yangzhou', 'Havana', 'Taizhou Zhejiang', 'Baoding', 'Perth', 'Brussels',
    'Linyi Shandong', 'Bursa', 'Rajkot', 'Minsk', 'Hiroshima', 'Haikou', 'Daqing', 'Lome',
    'Lianyungang', 'Yancheng Jiangsu', 'Panama City', 'Almaty', 'Semarang', 'Hyderabad', 'Valencia',
    'Davao City', 'Vienna', 'Rabat', 'Ludhiana', 'Quito', 'Benin City', 'La Paz', 'Baixada Santista',
    'West Yorkshire', 'Can Tho', 'Zhuhai', 'Leon de los Aldamas', 'Quanzhou', 'Matola', 'Datong',
    'Sharjah', 'Madurai', 'Raipur', 'Adana', 'Santa Cruz', 'Palembang', 'Mosul', 'Cixi', 'Meerut',
    'Gaziantep', 'La Laguna', 'Batam', 'Turin', 'Warsaw', 'Jiangmen', 'Varanasi', 'Hamburg',
    'Montevideo', 'Budapest', 'Lyon', 'Xiangyang', 'Bucharest', 'Yichang', 'Yinchuan', 'Shiraz',
    'Kananga', 'Srinagar', 'Monrovia', 'Tiruppur', 'Jamshedpur', 'Suqian', 'Aurangabad', 'Qinhuangdao',
    'Stockholm', 'Anshan', 'Glasgow', 'Xining', 'Makassar', 'Hengyang', 'Novosibirsk', 'Ulaanbaatar',
    'Onitsha', 'Jilin', 'Anyang', 'Auckland', 'Tabriz', 'Muscat', 'Calgary', 'Phoenix', 'Qiqihaer',
    'N-Djamena', 'Marseille', 'Cordoba', 'Jodhpur', 'Kathmandu', 'Rosario', 'Tegucigalpa',
    'Ciudad Juarez', 'Harare', 'Karaj', 'Medina', 'Jining Shandong', 'Abu Dhabi', 'Munich', 'Ranchi',
    'Daejon', 'Zhangjiakou', 'Edmonton', 'Mandalay', 'Gaoxiong', 'Kota', 'Natal', 'Nouakchott',
    'Jabalpur', 'Huainan', 'Grande Sao Luis', 'Asansol', 'Philadelphia', 'Yekaterinburg', 'Gwangju',
    'Yiwu', 'Chaozhou', 'San Antonio', 'Gwalior', 'Ganzhou', 'Homs', 'Niamey', 'Mombasa', 'Allahabad',
    'Basra', 'Kisangani', 'San Jose', 'Amritsar', 'Taizhou Jiangsu', 'Chon Buri', 'Jiaxing', 'Weihai',
    'Hai Phong', 'Ottawa', 'Zurich', 'Taian Shandong', 'Queretaro', 'Joao Pessoa', 'Kaifeng', 'Cochabamba',
    'Konya', 'Liuyang', 'Liuan', 'Rizhao', 'Kharkiv', 'Dhanbad', 'Nanchong', 'Dongying', 'Belgrade',
    'Zunyi', 'Zhanjiang', 'Bucaramanga', 'Uyo', 'Copenhagen', 'San Diego', 'Shiyan', 'Taizhong',
    'Bareilly', 'Pointe-Noire', 'Adelaide', 'Suweon', 'Mwanza', 'Mianyang Sichuan', 'Samut Prakan',
    'Maceio', 'Qom', 'Antalya', 'Joinville', 'Tengzhou', 'Yingkou', 'Ad-Dammam', 'Suzhou', 'Tanger',
    'Freetown', 'Helsinki', 'Aligarh', 'Moradabad', 'Pekan Baru', 'Maoming', 'Lilongwe', 'Porto',
    'Prague', 'Astana', 'Jieyang', 'Fushun Liaoning', 'Mysore', 'Abomey-Calavi', 'Ruian', 'Fes',
    'Port Elizabeth', 'Florianopolis', 'Ahvaz', 'Bukavu', 'Dallas', 'Nnewi', 'Kazan', 'Jinhua',
    'San Luis Potosi', 'Baoji', 'Durg-Bhilainagar', 'Bhubaneswar', 'Kigali', 'Sofia', 'Pingdingshan Henan',
    'Dublin', 'Puning', 'Chifeng', 'Zhuzhou', 'Bujumbura', 'Zhenjiang Jiangsu', 'Liupanshui',
    'Barquisimeto', 'Islamabad', 'Huaibei', 'Tasikmalaya', 'Maracay', 'Bogor', 'Da Nang', 'Nanyang Henan',
    'Nizhniy Novgorod', 'Xiangtan Hunan', 'Pizhou', 'Tiruchirappalli', 'Chelyabinsk', 'Mendoza', 'Luohe',
    'Xiongan', 'Chandigarh', 'Merida', 'Jinzhou', 'Benxi', 'Binzhou', 'Aba', 'Chiang Mai', 'Bazhong',
    'Quetta', 'Kaduna', 'Guilin', 'Saharanpur', 'Hubli-Dharwad', 'Yueqing', 'Guwahati', 'Mexicali',
    'Salem', 'Maputo', 'Tripoli', 'Haifa', 'Bandar Lampung', 'Bobo-Dioulasso', 'Amsterdam', 'Shimkent',
    'Omsk', 'Aguascalientes', 'Hargeysa', 'Krasnoyarsk', 'Xinxiang', 'Siliguri',
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


    G = create_country_graph(countries)
    call_all_functions(G)

if __name__ == "__main__":
    main()
