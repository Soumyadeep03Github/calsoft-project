import unittest
import requests


class TestTaskClass(unittest.TestCase):
    """Test Task API class."""

    def test_success(self):
        """Test case success flow."""
        url = 'http://127.0.0.1:5000/api/task'
        data = {'input': 10, 'file_name': 'file_1.txt'}
        resp = requests.post(url, json=data)
        self.assertEqual(resp.status_code, 201)

    def test_failure(self):
        """Test case failure flow."""
        url = 'http://127.0.0.1:5000/api/task'
        data_1 = {"input": 100}
        resp_1 = requests.post(url, json=data_1)
        self.assertEqual(resp_1.status_code, 400)


if __name__ == "__main__":
    test_obj = TestTaskClass()
    test_obj.test_success()
    test_obj.test_failure()
