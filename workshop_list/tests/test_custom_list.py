from unittest import TestCase, main
from workshop_list.custom_list import CustomList
from workshop_list.tests.helpers.helper_classes import PersonWithDunders, PersonWithoutDunders

class TestCustomList(TestCase):
    def setUp(self):
        self.custom_list = CustomList(1, 2, 3)

    def test_init(self):
        self.assertEqual(self.custom_list._CustomList__values, [1, 2, 3])

    def test_append_adds_element_at_the_end(self):
        self.assertEqual(self.custom_list._CustomList__values, [1, 2, 3])
        self.assertNotEqual(self.custom_list._CustomList__values[-1], 5)
        self.custom_list.append(5)
        self.assertEqual(self.custom_list._CustomList__values, [1, 2, 3, 5])
        self.assertEqual(self.custom_list._CustomList__values[-1], 5)

    def test_add_works_if_list_is_empty(self):
        cl = CustomList()
        self.assertEqual(cl._CustomList__values, [])
        cl.append(5)
        self.assertEqual(cl._CustomList__values, [5])

    def test_append_without_value_raises(self):
        with self.assertRaises(TypeError) as ex:
            # try to call it without argument (but it is required)
            self.custom_list.append()

        self.assertIn("append()", str(ex.exception))

    def test_append_does_not_returns_value(self):
        res = self.custom_list.append(5)
        self.assertIsNone(res)

    def test_remove_removes_element(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        self.custom_list.remove(0)
        self.assertEqual([2, 3], self.custom_list._CustomList__values)
        self.assertEqual(2, self.custom_list._CustomList__values[0])

    def test_remove_with_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            # Calls the method with invalid index
            self.custom_list.remove(100)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_remove_returns_the_removed_element(self):
        el = self.custom_list.remove(0)
        self.assertIsNotNone(el)
        self.assertEqual(1, el)

    def test_get_returns_element_on_the_given_index(self):
        el = self.custom_list.get(0)
        self.assertIsNotNone(el)
        self.assertEqual(1, el)

    def test_get_with_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            # Calls the method with invalid index
            self.custom_list.get(100)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_extend_appends_iterable_to_values(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.extend([100, 200])
        self.assertEqual([1, 2, 3, 100, 200], self.custom_list._CustomList__values)
        self.custom_list.extend((100, 200))
        self.assertEqual([1, 2, 3, 100, 200, 100, 200], self.custom_list._CustomList__values)
        self.custom_list.extend({5, 6})
        self.assertEqual([1, 2, 3, 100, 200, 100, 200, 5, 6], self.custom_list._CustomList__values)

    def test_extend_appends_iterable_to_values_with_empty_values(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        cl.extend([1, 2])
        self.assertEqual([1, 2], cl._CustomList__values)

    def test_extend_non_iterable_as_arg_should_work(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.extend(5)
        self.assertEqual([1, 2, 3, 5], self.custom_list._CustomList__values)

    def test_extend_returns_new_list_and_modifies_old_one(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.extend([100, 200])
        self.assertEqual([1, 2, 3, 100, 200], self.custom_list._CustomList__values)
        self.assertEqual([1, 2, 3, 100, 200], res)
        self.assertNotEqual(id(self.custom_list._CustomList__values), id(res))

    def test_insert_adds_element_to_specific_index_shifts_others_to_right(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        self.custom_list.insert(0, 5)
        self.assertEqual([5, 1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(5, self.custom_list._CustomList__values[0])
        self.assertEqual(1, self.custom_list._CustomList__values[1])

    def test_insert_adds_element_to_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            # Calls the method with invalid index
            self.custom_list.insert(100, 5)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_insert_returns_all_values_with_same_ref(self):
        # Insert should return the same list
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.insert(0, 100)
        self.assertEqual([100, 1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(id(self.custom_list._CustomList__values), id(res))

    def test_pop_removes_last_element_and_returns_it(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(3, self.custom_list._CustomList__values[-1])
        res = self.custom_list.pop()
        self.assertEqual([1, 2], self.custom_list._CustomList__values)
        self.assertEqual(2, self.custom_list._CustomList__values[-1])
        self.assertIsNotNone(res)
        self.assertEqual(3, res)

    def test_pop_with_empy_values_raises(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        with self.assertRaises(IndexError) as ex:
            cl.pop()
        self.assertEqual("No elements in the list", str(ex.exception))

    def test_clear_removes_all_elements_in_the_list(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.clear()
        self.assertEqual([], self.custom_list._CustomList__values)

    def test_clear_works_with_no_values_in_the_list(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        self.custom_list.clear()
        self.assertEqual([], cl._CustomList__values)

    def test_index_returns_value(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        res = self.custom_list.index(1)
        self.assertIsNotNone(res)
        self.assertEqual(res, 0)

    def test_index_raises_when_value_not_found(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertNotIn(100, self.custom_list._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.index(100)
        self.assertEqual("Element is not in the list", str(ex.exception))

    def test_count_returns_count_of_requested_element(self):
        self.assertEqual(1, self.custom_list._CustomList__values.count(1))
        res = self.custom_list.count(1)
        self.assertIsNotNone(res)
        self.assertEqual(1, res)

    def test_count_returns_zero_if_element_is_not_presented(self):
        self.assertEqual(0, self.custom_list._CustomList__values.count(0))
        res = self.custom_list.count(0)
        self.assertIsNotNone(res)
        self.assertEqual(0, res)

    def test_reverse_returns_new_list_with_reversed_values(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.reverse()
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual([3, 2, 1], res)
        self.assertNotEqual(id(res), id(self.custom_list._CustomList__values))

    def test_copy_returns_same_element_different_list(self):
        res = self.custom_list.copy()
        self.assertEqual(res, self.custom_list._CustomList__values)
        self.assertNotEqual(id(res), id(self.custom_list._CustomList__values))

    def test_size(self):
        self.assertEqual(3, len(self.custom_list._CustomList__values))
        res = self.custom_list.size()
        self.assertEqual(3, res)

    def test_add_first_adds_element_to_the_begging_of_the_list(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        self.custom_list.add_first(100)
        self.assertEqual([100, 1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(100, self.custom_list._CustomList__values[0])
        self.assertEqual(1, self.custom_list._CustomList__values[1])

    def test_dictionize_with_even_values(self):
        cl = CustomList(1, 2, 3, 4)
        res = cl.dictionize()
        self.assertTrue(isinstance(res, dict))
        self.assertEqual({1: 2, 3: 4}, res)


    def test_dictionize_with_odd_values(self):
        res = self.custom_list.dictionize()
        self.assertTrue(isinstance(res, dict))
        self.assertEqual({1: 2, 3: ' '}, res)

    def test_move_move_first_n_to_the_end(self):
        elements = [el for el in range(1, 11)]
        self.custom_list._CustomList__values = elements
        self.assertEqual(elements, self.custom_list._CustomList__values)
        self.custom_list.move(5)
        expected = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
        self.assertEqual(expected, self.custom_list._CustomList__values)

    def test_move_invalid_amount_raises(self):
        elements = [el for el in range(1, 11)]
        self.custom_list._CustomList__values = elements
        self.assertEqual(elements, self.custom_list._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            # Bigger amount than the elements in the list
            self.custom_list.move(11)
        self.assertEqual("Invalid amount", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            # Bigger amount than the elements in the list
            self.custom_list.move(-1)
        self.assertEqual("Invalid amount", str(ex.exception))

    def test_sum_raises_if_object_does_not_implement_dunder_add(self):
        cl = CustomList(1, "asd", PersonWithoutDunders())
        with self.assertRaises(ValueError) as ex:
            cl.sum()
        self.assertEqual("All objects must implement dunder add", str(ex.exception))

    def test_sum_with_strings_add_their_length_to_the_sum(self):
        word = "hello"
        self.assertEqual(5, len(word))
        cl = CustomList(1, PersonWithDunders())
        res = cl.sum()
        self.assertEqual(6, res)

    def test_sum_with_custom_object_adds(self):
        cl = CustomList(1, PersonWithDunders())
        res = cl.sum()
        self.assertEqual(6, res)

    def test_overbound_raises_if_object_does_not_implement_dunder_len(self):
        cl = CustomList(1, "asd", PersonWithoutDunders())
        with self.assertRaises(ValueError) as ex:
            cl.overbound()
        self.assertEqual("All objects must implement dunder len", str(ex.exception))

    def test_overbound_with_strings_add_their_length(self):
        word = "hello"
        self.assertEqual(5, len(word))
        cl = CustomList(1, word)
        self.assertEqual(1 , cl._CustomList__values.index(word))

        res = cl.overbound()
        self.assertEqual(1, res)

    def test_overbound_with_custom_object(self):
        word = "hello"
        self.assertEqual(5, len(word))
        cl = CustomList(1, word, PersonWithDunders())

        self.assertEqual(1, cl._CustomList__values.index(word))
        res = cl.overbound()
        # returns 2 because person length is 10
        self.assertEqual(2, res)


if __name__ == "__main__":
    main()