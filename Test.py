import unittest
import Logic as l
import os
class TestCRDOperations(unittest.TestCase):
	
	def test_read(self):
		l.load("test\\test-read.json")
		self.assertEqual(l.read("k1"), "k1:v1")
		self.assertEqual(l.read("k2"), "k2:v2")
		self.assertEqual(l.read("k3"), "k3 has been expired")
	
	def test_create(self):
		l.load("test\\test-write.json")
		l.create("key", "value1")
		self.assertEqual(l.read("key"), "key:value1")
		os.remove("test\\test-write.json")
	def test_delete(self):
		l.load("test\\test-delete.json")
		l.create("key", "value1")
		l.create("kee", "value12")
		self.assertEqual(l.delete("key"), "key is successfully deleted")
		os.remove("test\\test-delete.json")
if __name__ == "__main__":

	unittest.main()