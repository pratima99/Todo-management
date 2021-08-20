from flask import request, Response
from flask_restful import Resource
from database.documents.todo import Todo


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
