# -*- coding: utf-8 -*-

import sys
from difflib import SequenceMatcher
from highlights.pprint import NORMAL, INSERTED, DELETED
from highlights.pprint import pprint_hunk, pprint_pair, is_mergeable

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestPPrint(unittest.TestCase):
    def test_pprint_hunk(self):
        #new, new_lo, new_hi, old, old_lo, old_hi):
        new = ["+print 'hello', 'world'",
               "+",
               "+",
               "+print 'bye world'"]
        old = ["-print 'nice', 'boat'",
               "-print \"bye world\""]
        ret = pprint_hunk(new, 0, 4, old, 0, 2)

        pairs = list(ret)
        self.assertEqual(26, len(pairs))
        self.assertEqual(("-print '", DELETED, False), pairs[0])
        self.assertEqual(("nice", DELETED, True), pairs[1])
        self.assertEqual(("', '", DELETED, False), pairs[2])
        self.assertEqual(("boat", DELETED, True), pairs[3])
        self.assertEqual(("'", DELETED, False), pairs[4])
        self.assertEqual(("\n", NORMAL, False), pairs[5])
        self.assertEqual(("+print '", INSERTED, False), pairs[6])
        self.assertEqual(("hello", INSERTED, True), pairs[7])
        self.assertEqual(("', '", INSERTED, False), pairs[8])
        self.assertEqual(("world", INSERTED, True), pairs[9])
        self.assertEqual(("'", INSERTED, False), pairs[10])
        self.assertEqual(("\n", NORMAL, False), pairs[11])
        self.assertEqual(("+", INSERTED, False), pairs[12])
        self.assertEqual(("\n", NORMAL, False), pairs[13])
        self.assertEqual(("+", INSERTED, False), pairs[14])
        self.assertEqual(("\n", NORMAL, False), pairs[15])
        self.assertEqual(("-print ", DELETED, False), pairs[16])
        self.assertEqual(("\"", DELETED, True), pairs[17])
        self.assertEqual(("bye world", DELETED, False), pairs[18])
        self.assertEqual(("\"", DELETED, True), pairs[19])
        self.assertEqual(("\n", NORMAL, False), pairs[20])
        self.assertEqual(("+print ", INSERTED, False), pairs[21])
        self.assertEqual(("'", INSERTED, True), pairs[22])
        self.assertEqual(("bye world", INSERTED, False), pairs[23])
        self.assertEqual(("'", INSERTED, True), pairs[24])
        self.assertEqual(("\n", NORMAL, False), pairs[25])

    def test_pprint_pair(self):
        cruncher = SequenceMatcher()
        ret = pprint_pair(cruncher,
                          "+print 'hello', 'world'",
                          "-print 'nice', 'boat'")

        pairs = list(ret)
        self.assertEqual(12, len(pairs))
        self.assertEqual(("-print '", DELETED, False), pairs[0])
        self.assertEqual(("nice", DELETED, True), pairs[1])
        self.assertEqual(("', '", DELETED, False), pairs[2])
        self.assertEqual(("boat", DELETED, True), pairs[3])
        self.assertEqual(("'", DELETED, False), pairs[4])
        self.assertEqual(("\n", NORMAL, False), pairs[5])
        self.assertEqual(("+print '", INSERTED, False), pairs[6])
        self.assertEqual(("hello", INSERTED, True), pairs[7])
        self.assertEqual(("', '", INSERTED, False), pairs[8])
        self.assertEqual(("world", INSERTED, True), pairs[9])
        self.assertEqual(("'", INSERTED, False), pairs[10])
        self.assertEqual(("\n", NORMAL, False), pairs[11])

    def test_is_mergeable(self):
        # True/False/True -> ok
        new = [('A', None, True), ('B', None, False), ('C', None, True)]
        old = [('', None, False), ('B', None, False), ('', None, False)]
        self.assertTrue(is_mergeable(new, old, 2))
        self.assertTrue(is_mergeable(old, new, 2))

        # False/False/True -> NG
        new = [('A', None, False), ('B', None, False), ('C', None, True)]
        old = [('A', None, False), ('B', None, False), ('', None, False)]
        self.assertFalse(is_mergeable(new, old, 2))
        self.assertFalse(is_mergeable(old, new, 2))

        # True/False/False -> NG
        new = [('A', None, True), ('B', None, False), ('C', None, False)]
        old = [('', None, False), ('B', None, False), ('C', None, False)]
        self.assertFalse(is_mergeable(new, old, 2))
        self.assertFalse(is_mergeable(old, new, 2))

        # False/False/False -> NG
        new = [('A', None, False), ('B', None, False), ('C', None, False)]
        old = [('A', None, False), ('B', None, False), ('C', None, False)]
        self.assertFalse(is_mergeable(new, old, 2))
        self.assertFalse(is_mergeable(old, new, 2))

        # word/word/word -> ok
        new = [('A', None, True), ('B', None, False), ('C', None, True)]
        old = [('', None, False), ('B', None, False), ('', None, False)]
        self.assertTrue(is_mergeable(new, old, 2))
        self.assertTrue(is_mergeable(old, new, 2))

        # word/space/word -> ok
        new = [('A', None, True), (' ', None, False), ('C', None, True)]
        old = [('', None, False), (' ', None, False), ('', None, False)]
        self.assertTrue(is_mergeable(new, old, 2))
        self.assertTrue(is_mergeable(old, new, 2))

        # word/mark/word -> NG
        new = [('A', None, True), (',', None, False), ('C', None, True)]
        old = [('', None, False), (',', None, False), ('', None, False)]
        self.assertFalse(is_mergeable(new, old, 2))
        self.assertFalse(is_mergeable(old, new, 2))

        # word/word/mark -> ok
        new = [('A', None, True), ('B', None, False), (',', None, True)]
        old = [('', None, False), ('B', None, False), ('', None, False)]
        self.assertTrue(is_mergeable(new, old, 2))
        self.assertTrue(is_mergeable(old, new, 2))

        # mark/word/word -> ok
        new = [(',', None, True), ('B', None, False), ('C', None, True)]
        old = [('', None, False), ('B', None, False), ('', None, False)]
        self.assertTrue(is_mergeable(new, old, 2))
        self.assertTrue(is_mergeable(old, new, 2))

        # mark/mark/mark -> ok
        new = [(',', None, True), (':', None, False), ('.', None, True)]
        old = [('', None, False), (':', None, False), ('', None, False)]
        self.assertTrue(is_mergeable(new, old, 2))
        self.assertTrue(is_mergeable(old, new, 2))

        # mark/word/mark -> ok
        new = [(',', None, True), ('B', None, False), ('.', None, True)]
        old = [('', None, False), ('B', None, False), ('', None, False)]
        self.assertTrue(is_mergeable(new, old, 2))
        self.assertTrue(is_mergeable(old, new, 2))

        # mark/space/mark -> ok
        new = [(',', None, True), (' ', None, False), ('.', None, True)]
        old = [('', None, False), (' ', None, False), ('', None, False)]
        self.assertTrue(is_mergeable(new, old, 2))
        self.assertTrue(is_mergeable(old, new, 2))

        # A/ is /C => A/ is /C -> NG
        new = [('A', None, True), (' is ', None, False), ('C', None, True)]
        old = [('', None, False), (' is ', None, False), ('', None, False)]
        self.assertFalse(is_mergeable(new, old, 2))
        self.assertFalse(is_mergeable(old, new, 2))

        # A/ = /C => A/ = /C -> NG
        new = [('A', None, True), (' = ', None, False), ('C', None, True)]
        old = [('', None, False), (' = ', None, False), ('', None, False)]
        self.assertFalse(is_mergeable(new, old, 2))
        self.assertFalse(is_mergeable(old, new, 2))