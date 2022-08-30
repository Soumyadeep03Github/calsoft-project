import json
from flask_restful import Resource
from flask import request
import logging as logger

from .handler import FileHandler


class Task(Resource):
    """Task APIs."""

    def post(self):
        """Post method."""
        data = request.get_json()
        logger.debug("Inside the post method of Task API Class.")
        return FileHandler().fetch_file_and_write(data)
