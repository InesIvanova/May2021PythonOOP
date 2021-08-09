from copy import deepcopy


class HashTable:
    """
    A class representing custom dict structures that can be used as python dict,
    this structure uses two lists, so that it can save the keys and values.
    Starts at max capacity 4
    """
    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    @property
    def length(self):
        return self.max_capacity

    def __setitem__(self, key, value):
        """
        Set a key/value pair.
        If the key does not exist as an element in the list,
        then ValueError is raised and we must set the new value.
        If it does exist then we update the current element in the list.
        If max capacity is reached, we resize the lists first, so that
        we do not exceed recursion depth.
        """
        if len([el for el in self.__keys if el is not None]) == self.max_capacity:
            self.__resize()
        try:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        except ValueError:
            index = self.get_available_index(key)
            self.__keys[index] = key
            self.__values[index] = value

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key is not in dict")

    def __len__(self):
        return len([el for el in self.__keys if el is not None])

    def __repr__(self):
        to_str = []
        for key, value in self.items():
            to_str.append(f"{key}: {value}")
        return "{" + ", ".join(to_str) + "}"

    def __resize(self):
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity *= 2

    def __check_index(self, index):
        if index == len(self.__keys):
            return self.__check_index(0)
        if self.__keys[index] is None:
            return index
        # We have collision - take the linear approach here
        return self.__check_index(index+1)

    def keys(self):
        return [el for el in self.__keys if el is not None]

    def values(self):
        """
        Returns only the values where a key in keys list exist.
        It is possible to have None values as an existing key.
        It should return None for keys which are not Nones!
        """
        keys = self.keys()
        values_list = []
        for key in keys:
            index = self.__keys.index(key)
            values_list.append(self.__values[index])
        return values_list

    def get_available_index(self, key):
        """
        Calculates the first available index after the hash method
        :param key:
        :return:
        """
        index = self.hash(key)
        available_index = self.__check_index(index)
        return available_index

    def hash(self, key):
        """
        Create a hash with ascii values from the characters (modulo by the
        max capacity attr)
        :param key:
        :return:
        """
        index = sum([ord(char) for char in key]) % self.max_capacity
        return index

    def get(self, key, default=None):
        """get"""
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def add(self, key, value):
        self.__setitem__(key, value)

    def items(self):
        return list(zip(self.keys(), self.values()))

    def clear(self):
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def copy(self):
        return deepcopy(self)

    def pop(self, key):
        try:
            index = self.__keys.index(key)
            self.__keys[index] = None
            value_element = self.__values[index]
            self.__values[index] = None
            return value_element
        except ValueError:
            raise KeyError('Invalid key')

#
# table = HashTable()
#
# table["name"] = "Pesho"
# table["age"] = 25
#
# print(table)
# print(table.get("name"))
# print(table["age"])
# print(len(table))
# print(table.length)
# print(table.keys())
# print(table.values())
# print(table.items())
# a = table.copy()
# a["name"] = 6
# print(table["name"])
# table.add("fromtest", 5)
# print(table)
