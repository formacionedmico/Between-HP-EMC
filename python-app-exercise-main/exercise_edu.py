import exercise_edu_functions as functions

api_url = 'https://jsonplaceholder.typicode.com/todos/'

for todo in functions.get_todos_aslist_of_jsons(api_url):
  functions.create_csv(todo)
