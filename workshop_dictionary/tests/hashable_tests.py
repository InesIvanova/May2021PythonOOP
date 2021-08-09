from unittest import TestCase, main

from workshop_dictionary.hashable_live_demo import HashTable


class TestHashTable(TestCase):
    def setUp(self):
        self.table = HashTable()

    def test_init(self):
        self.assertEqual([None, None, None, None], self.table._HashTable__keys)
        self.assertEqual([None, None, None, None], self.table._HashTable__values)
        self.assertEqual(4, self.table.max_capacity)

    def test_set_item_key_does_not_exist_set_key_value(self):
        self.assertNotIn("test", self.table._HashTable__keys)
        self.assertNotIn(5, self.table._HashTable__values)

        self.table["test"] = 5

        self.assertIn("test", self.table._HashTable__keys)
        self.assertIn(5, self.table._HashTable__values)

    def test_set_item_key_exist_replace_value(self):
        self.table["test"] = 5
        self.assertIn("test", self.table._HashTable__keys)
        self.assertIn(5, self.table._HashTable__values)

        self.table["test"] = 10
        self.assertIn("test", self.table._HashTable__keys)
        self.assertIn(10, self.table._HashTable__values)
        self.assertNotIn(5, self.table._HashTable__values)

    def test_set_item_full_dict_resizes(self):
        self.assertEqual(0, len(self.table.keys()))
        self.table["name"] = "test"
        self.table["age"] = 10
        self.table["color"] = "blue"
        self.table["id"] = 5012

        self.assertEqual(4, len(self.table.keys()))
        self.assertEqual(4, self.table.max_capacity)

        self.table["resize"] = True
        self.assertEqual(5, len(self.table.keys()))
        self.assertEqual(8, self.table.max_capacity)

    def test_collision_is_handled(self):
        self.assertEqual(0, len(self.table.keys()))
        self.table["name"] = "test"
        index = self.table.hash("name")
        self.assertEqual(1, index)

        index = self.table.hash("age")
        self.assertEqual(1, index)

        # Collision should be handled and age should be on index 2
        self.assertEqual(2, self.table.get_available_index("age"))
        self.table["age"] = 10
        self.assertEqual(2, self.table._HashTable__keys.index("age"))

    def test_get_existing_value_by_key_returns_value(self):
        self.table["name"] = "test"
        self.assertIn("name", self.table._HashTable__keys)
        self.assertIn("test", self.table._HashTable__values)

        res = self.table["name"]
        self.assertEqual("test", res)

    def test_getitem_unexisting_key_raises(self):
        self.assertNotIn("name", self.table._HashTable__keys)
        with self.assertRaises(KeyError) as ex:
            self.table["name"]
        self.assertEqual("'Key is not in dict'", str(ex.exception))

    def test_get_unexisting(self):
        self.assertNotIn("name", self.table._HashTable__keys)
        res = self.table.get("name")
        self.assertIsNone(res)

    def test_get_with_default_returns_default_when_key_does_not_exist(self):
        self.assertNotIn("name", self.table._HashTable__keys)
        res = self.table.get("name", default="Some str")
        self.assertIsNotNone(res)
        self.assertEqual("Some str", res)


if __name__ == "__main__":
    main()