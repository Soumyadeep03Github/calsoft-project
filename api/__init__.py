from flask_restful import Api

from app import flaskAppInstance

from .task_api import Task


restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(Task,"/api/task")
