from flask import Flask, Response, request
from flask_restful import Api, Resource
from flask_mongoengine import MongoEngine
import mongoengine as me

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    "db": "tasks",
}
db = MongoEngine(app)


class Todo(me.Document):
    title = me.StringField(required=True)
    time = me.StringField(required=True)


class TodosList(Resource):
    def get(self):
        todos = Todo.objects().to_json()
        return Response(todos, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        Todo(**body).save()
        return {'result': "Todo created successfully"}, 200


class SingleTodo(Resource):
    def get(self, id):
        todo = Todo.objects.get(id=id).to_json()
        # return todo
        return Response(todo, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Todo.objects.get(id=id).update(**body)
        return {'result': "Todo updated successfully"}, 200

    def delete(self, id):
        Todo.objects.get(id=id).delete()
        return {'result': "Todo deleted successfully"}, 200


api.add_resource(TodosList, '/todos')
api.add_resource(SingleTodo, '/todos/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
