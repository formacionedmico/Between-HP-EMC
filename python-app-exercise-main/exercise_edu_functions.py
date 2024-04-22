import requests
from datetime import datetime
import csv

def current_date_as_YYYY_MM_DD():
  return datetime.now().strftime('%Y_%m_%d')

def csv_name_as_currentDate_todoId(todo):
  return current_date_as_YYYY_MM_DD() + '_' + str(todo['id'])

def create_csv(todo):
  with open('csv/' + csv_name_as_currentDate_todoId(todo), 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=todo.keys())
    writer.writeheader()
    writer.writerow(todo)

def get_todos_aslist_of_jsons(api_url):
  response = requests.get(api_url)
  list_of_todos_as_jsons = response.json()
  return list_of_todos_as_jsons
