import requests
import json

def fetch_all_stats():
  data = requests.get('https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true')
  parsed = json.loads(data.text)
  total_deaths = 0
  total_infected = 0
  total_recovered = 0
  for country in parsed:
    total_deaths+=country['deceased']
    total_infected+=country['infected']

  data = {'total_deaths':total_deaths, 'total_infected':total_infected}

  return(data)

def fetch_countries():
  data = requests.get('https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true')
  parsed = json.loads(data.text)
  countries_list=[{'Name' : country['country'], 'Infected' : country['infected'], 'TotalRecovered' : country['recovered'], 'TotalDeaths' : country['deceased'], 'Updated' : country['lastUpdatedApify']} for country in parsed]

  return countries_list


country_stats_list = fetch_countries()
global_stats = fetch_all_stats()
