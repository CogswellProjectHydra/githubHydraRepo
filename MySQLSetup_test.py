from MySQLSetup import *

import unittest

class test_sql (unittest.TestCase): 

    def test_insert (self):
        newNote = Hydra_test(notes='te"s"\\ting')
        self.assertFalse (hasattr (newNote, 'id'))
        newNote.insert ()
        self.assert_ (hasattr (newNote, 'id'))

    def test_update (self):
        newNote = Hydra_test()
        newNote.insert ()
        newNote.notes = "here"
        newNote.update ()
        [newNote2] = Hydra_test.fetch ("where id = %d" % newNote.id)
        self.assertEqual (newNote2.notes, "here")
        
if __name__ == '__main__':
    unittest.main( exit=False )
