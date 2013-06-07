import unittest
from tbws.service import MemoryDb

class MemoryDbTest(unittest.TestCase):

    def test_mdb(self):
        db = MemoryDb()
        db.put('test', 'test')
        db.get('test')

    def test_when_getting_the_largest_value_within_an_in_memory_database(self):
        db = MemoryDb()
        db.put('test', 'test')
        db.put('test1', 'testt')
        db.put('test2', 'testtt')
        db.put('test3', 'testttt')
        db.put('test4', 'testtttt')
        db.put('test5', 'testtt')
        db.put('test6', 'testtt')
        db.put('test7', 'testt')
        db.put('test8', 'test')
        db.put('test9', 'te')
        if not db.get_largest() == 'testtttt':
            self.fail()

if __name__ == '__main_':
    unittest.main()

