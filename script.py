import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

pp = pprint.PrettyPrinter(indent=4)

API_URL = 'https://weatherdbi.herokuapp.com/data/weather/'
city = 'murrieta' # feel free to enter your own city here!
r = requests.get(API_URL + city)
response = r.json()

pp.pprint(response)

forecast_list = response['next_days']
today = datetime.now().strftime("%b-%d-%Y")

to_graph = {} # The empty dictionary to store our shaped data
count = 1 # A global iterator to track each day past current datetime

for d in forecast_list:
    current_date = int(today[4:6]) + count
    this_day = f"{today[0:4]}{current_date}{today[6:]}"
    day_name=d['day']
    count += 1

    to_graph[day_name] = d['max_temp']['f']
print(to_graph)

# expected output should look something like:
#   {'Aug-24-2021': 12,
#    'Aug-25-2021': 14,  
#    'Aug-26-2021': 0 }

# Remember to always label the axes of your graph!
plt.xlabel('Day of Week')
plt.ylabel('Temp')

print('to_graph keys: ', to_graph.keys())
print('to_graph values: ', to_graph.values())

plt.scatter(to_graph.keys(), to_graph.values()) # sets up the graph
plt.show() # paints the graph to your screen
