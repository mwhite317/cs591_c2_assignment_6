import unittest

from solution import *


class MyTestCase(unittest.TestCase):
	def test_url_object(self):
		url = URL_Splitter('https://www.google.com/some-path')
		self.assertIsNotNone(url)

	def test_url(self):
		url = URL_Splitter('https://www.google.com/some-path')
		self.assertEqual(url.url, 'https://www.google.com/some-path')

	def test_sep_object(self):
		url = URL_Splitter('https://www.google.com/some-path')
		self.assertIsNotNone(url.sep)

	def test_sep(self):
		url = URL_Splitter('https://www.google.com/some-path')
		self.assertEqual(url.sep, ['https:', '', 'www.google.com', 'some-path'])

	def test_protocol_object(self):
		url = URL_Splitter('https://www.google.com/some-path')
		self.assertIsNotNone(url.protocol())

	def test_protocol(self):
		url = URL_Splitter('https://cs-people.bu.edu/dharmesh/teaching/')
		self.assertEqual(url.protocol(), 'https')

	def test_domain_object(self):
		url = URL_Splitter('https://www.google.com/some-path')
		self.assertIsNotNone(url.domain())

	def test_domain(self):
		url = URL_Splitter('https://cs-people.bu.edu/dharmesh/teaching/')
		self.assertEqual(url.domain(), 'cs-people.bu.edu')

	def test_path_object(self):
		url = URL_Splitter('https://www.google.com/some-path')
		self.assertIsNotNone(url.path())

	def test_path(self):
		url = URL_Splitter('https://cs-people.bu.edu/dharmesh/teaching/')
		self.assertEqual(url.path(), 'dharmesh/teaching/')

	def test_split(self):
		url = URL_Splitter('https://cs-people.bu.edu/dharmesh/teaching/')
		self.assertEqual(url.split(), "\nProtocol: https \nDomain: cs-people.bu.edu \nPath: dharmesh/teaching/\n")

if __name__ == '__main__':
    unittest.main()