import requests
import unittest

class TestClient(unittest.TestCase):
    def setUp(self):
        self.url = "https://poetrydb.org"

    def test_returns_200(self):
        result = requests.get('https://poetrydb.org/author')
        self.assertEqual(result.status_code, 200)

    def test_check_dictionary(self):
        result = requests.get('https://poetrydb.org/author').json()
        assert isinstance(result, dict), "Response data is not a dictionary"

    def test_check_response_is_not_empty(self):
        result = requests.get('https://poetrydb.org/author/William%20Shakespeare/author,title').json()
        assert len(result) > 0, "'result' dict is empty"

    def test_check_response_key(self):
        result = requests.get('https://poetrydb.org/author').json()
        assert "authors" in result, "Expected 'authors' key not found in the JSON response"

if __name__ == '__main__':
    unittest.main()
