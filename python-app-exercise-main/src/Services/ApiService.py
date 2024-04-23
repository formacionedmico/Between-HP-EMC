from sys import stderr
import exercise_edu_functions as functions


class ApiService:
    def __init__(self):
        pass

    def run(self):
        print('Running ApiService', file=stderr)

        # TODO: follow README.md instructions
        api_url = 'https://jsonplaceholder.typicode.com/todos/'

        for todo in functions.get_todos_aslist_of_jsons(api_url):
            functions.create_csv(todo)
