import requests
import unittest

r = requests.get('https://poetrydb.org/author,linecount/Shakespeare;14/lines')
print(r.status_code)

