from flask import Flask
from flask_restful import Api

from extensions import db
from resources.todo_resource import TodosList, SingleTodo
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "tasks",
}
api = Api(app)
db.init_app(app)


api.add_resource(TodosList, '/todos')
api.add_resource(SingleTodo, '/todos/<string:id>')

if __name__ == '__main__':
    app.run(debug=True, port=5006)
