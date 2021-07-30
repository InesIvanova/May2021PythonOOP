from Lecture_10_testing.extended_list import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self):
        self.list_integers = IntegerList(5, 6, 7)

    def test_init_creates_all_attributes(self):
        self.assertEqual([5, 6, 7], self.list_integers._IntegerList__data)

    def test_init_takes_non_integers(self):
        list_integers = IntegerList(5.6, "6", 7.2)
        self.assertEqual([], list_integers._IntegerList__data)

    def test_add_integer_is_added(self):
        result = self.list_integers.add(100)
        self.assertEqual([5, 6, 7, 100], result)

    def test_add_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integers.add(5.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_returns_element(self):
        el = self.list_integers.remove_index(0)
        self.assertEqual(5, el)
        self.assertEqual([6, 7], self.list_integers._IntegerList__data)

    def test_remove_index_not_in_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_with_valid_index_returns_element(self):
        el = self.list_integers.get(0)
        self.assertEqual(5, el)
        self.assertEqual([5, 6, 7], self.list_integers._IntegerList__data)

    def test_get_with_not_valid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_adds_element_at_index(self):
        self.list_integers.insert(0, 100)
        self.assertEqual([100, 5, 6, 7], self.list_integers._IntegerList__data)

    def test_insert_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integers.insert(0, 5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_integer_to_non_valid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.insert(3, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_biggest(self):
        res = self.list_integers.get_biggest()
        self.assertEqual(7, res)

    def test_get_index(self):
        index = self.list_integers.get_index(5)
        self.assertEqual(0, index)


if __name__ == "__main__":
    main()