import os
import sys
import unittest

HERE = os.path.dirname(__file__)
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from linkedlist import LinkedList, DoublyLinkedList, StudentLinkedList


class TestLinkedListBasic(unittest.TestCase):
    def test_append_prepend_delete_search(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.to_list(), [1, 2, 3])
        ll.prepend(0)
        self.assertEqual(ll.to_list(), [0, 1, 2, 3])
        self.assertEqual(ll.search(2), 2)
        self.assertTrue(ll.delete(2))
        self.assertEqual(ll.to_list(), [0, 1, 3])
        self.assertFalse(ll.delete(99))
        self.assertEqual(ll.count_nodes(), 3)


class TestDoublyLinkedList(unittest.TestCase):
    def test_append_prepend_delete(self):
        dl = DoublyLinkedList()
        dl.append('a')
        dl.append('b')
        dl.prepend('z')
        self.assertEqual(dl.to_list(), ['z', 'a', 'b'])
        self.assertTrue(dl.delete('a'))
        self.assertEqual(dl.to_list(), ['z', 'b'])
        self.assertFalse(dl.delete('nope'))


class TestStudentLinkedList(unittest.TestCase):
    def test_add_delete_find_list(self):
        s = StudentLinkedList()
        s.add_student(1002, 'Bob', 3.0)
        s.add_student(1001, 'Alice', 3.5)
        s.add_student(1003, 'Charlie', 2.8)
        # list should be sorted by id
        self.assertEqual([x[0] for x in s.list_all()], [1001, 1002, 1003])
        self.assertEqual(s.find_by_id(1002)[1], 'Bob')
        self.assertTrue(s.delete_by_id(1002))
        self.assertIsNone(s.find_by_id(1002))
        self.assertFalse(s.delete_by_id(9999))


if __name__ == '__main__':
    unittest.main()
