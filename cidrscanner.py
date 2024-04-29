import requests

search_query = input("Enter search query: ")
url = f"https://api.bgpview.io/search?query_term={search_query}"

response = requests.get(url)
data = response.json()

if 'ipv4_prefixes' in data['data']:
    cidr_list = [entry['prefix'] for entry in data['data']['ipv4_prefixes']]
    with open(f"{search_query}.txt", 'w') as file:
        for cidr in cidr_list:
            file.write(cidr + '\n')
    print(f"CIDR addresses saved to {search_query}.txt")
else:
    print("No results found for the given query.")
