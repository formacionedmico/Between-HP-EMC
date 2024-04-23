import requests
from datetime import datetime
import csv

def current_date_as_YYYY_MM_DD():
  """
    It creates a string in the form of 'YYYY_MM_DD' with the current date.
  """

  return datetime.now().strftime('%Y_%m_%d')

def csv_name_as_currentDate_todoId(todo):
  """
    It creates a string from the current date as 'YYYY_MM_DD' and the 'todo's id as 'YYYY_MM_DD_[todo's id]'.

    Params:

      todo: content as a json.
  """
  return current_date_as_YYYY_MM_DD() + '_' + str(todo['id'])

def create_csv(todo):
  """
    It creates a .csv file inside an existing 'csv' folder with the name given by the function 'csv_name_as_currentDate_todoId()' nad it writes in it todo's keys as headers and todo's content as its content.

    Params:

      todo: content as a json.
  """
  with open('csv/' + csv_name_as_currentDate_todoId(todo), 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=todo.keys())
    writer.writeheader()
    writer.writerow(todo)

def get_todos_aslist_of_jsons(api_url):
  """
    It gets the content of an url and converts it into a list of jsons. A json for each element in the url.

    Params:

      api_url: url containing the information to be requested.

    Return:

      list_of_todos_as_jsons: list of url jsons.
  """
  response = requests.get(api_url)
  list_of_todos_as_jsons = response.json()
  return list_of_todos_as_jsons
