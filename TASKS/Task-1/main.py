import networkx as nx
import matplotlib.pyplot as plt

def create_country_graph(countries):
 
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add all countries as nodes
    G.add_nodes_from(countries)
    
    # Create edges based on first and last letter connections
    for source in countries:
        for target in countries:
            if source != target and source[-1].lower() == target[0].lower():
                G.add_edge(source, target)
    
    return G

def visualize_graph(G):

    # Set up the plot with a larger figure size
    plt.figure(figsize=(20, 20))
    
    # Use spring layout for node positioning
    pos = nx.spring_layout(G, k=0.9, iterations=50)
    
    # Calculate node degrees to determine color
    node_degrees = dict(G.degree())
    max_degree = max(node_degrees.values())
    
    # Draw the graph
    plt.title("Country Connection Graph", fontsize=20, fontweight='bold')
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos,
                           node_color=[plt.cm.viridis(node_degrees[node]/max_degree) for node in G.nodes()],
                           node_size=300,
                           alpha=0.8)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos,
                           edge_color='gray',
                           arrows=True,
                           arrowsize=10,
                           arrowstyle='->', 
                           alpha=0.3)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos,
                            font_size=8,
                            font_weight='bold')
    
    # Remove axis
    plt.axis('off')
    
    # Tight layout
    plt.tight_layout()
    
    # Save the graph
    plt.savefig('cities_and_countries.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # List of countries (copied from the provided text)
    
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
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe",
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
    'Omsk', 'Aguascalientes', 'Hargeysa', 'Krasnoyarsk', 'Xinxiang', 'Siliguri'
]


                                                                                            
    
    # Create the graph
    G = create_country_graph(countries)

    # Print some basic graph statistics
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    
    # Visualize the graph
    visualize_graph(G)
    
    # Optional: Additional graph analysis
    print("\nTop 5 countries with most incoming connections:")
    top_in_degree = sorted(G.in_degree, key=lambda x: x[1], reverse=True)[:5]
    for country, in_degree in top_in_degree:
        print(f"{country}: {in_degree} incoming connections")
    
    print("\nTop 5 countries with most outgoing connections:")
    top_out_degree = sorted(G.out_degree, key=lambda x: x[1], reverse=True)[:5]
    for country, out_degree in top_out_degree:
        print(f"{country}: {out_degree} outgoing connections")

if __name__ == "__main__":
    main()