from project.hotel import Hotel
from project.room import Room
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 3)
        self.hotel = Hotel("Some Hotel")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.room.number, 1)
        self.assertEqual(self.room.capacity, 3)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(self.room.is_taken, False)

    def test_take_room_success(self):
        self.room.take_room(2)
        self.assertEqual(self.room.is_taken, True)
        self.assertEqual(self.room.guests, 2)

    def test_take_room_not_enough_capacity(self):
        result = self.room.take_room(4)
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(result, "Room number 1 cannot be taken")

    def test_take_room_not_free(self):
        self.room.take_room(1)
        result = self.room.take_room(1)
        self.assertEqual(self.room.is_taken, True)
        self.assertEqual(self.room.guests, 1)
        self.assertEqual(result, "Room number 1 cannot be taken")

    def test_free_room_success(self):
        self.room.take_room(1)
        self.room.free_room()
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)

    def test_free_room_not_taken(self):
        result = self.room.free_room()
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(result, "Room number 1 is not taken")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.hotel.name, "Some Hotel")
        self.assertEqual(self.hotel.rooms, [])
        self.assertEqual(self.hotel.guests, 0)

    def test_class_methods_creates_a_hotel(self):
        hotel = Hotel.from_stars(3)
        self.assertEqual(hotel.name, "3 stars Hotel")
        self.assertEqual(self.hotel.rooms, [])
        self.assertEqual(self.hotel.guests, 0)

    def test_add_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.assertEqual(self.hotel.rooms, [room])

    def test_take_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        self.assertEqual(self.hotel.rooms[0].is_taken, True)

    def test_free_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        self.hotel.free_room(1)
        self.assertEqual(self.hotel.guests, 0)
        self.assertEqual(self.hotel.rooms[0].is_taken, False)
        self.assertEqual(self.hotel.rooms[0].guests, 0)

    def test_print_status(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        res = self.hotel.status().strip()
        actual = 'Hotel Some Hotel has 3 total guests\nFree rooms: \nTaken rooms: 1'
        self.assertEqual(res, actual)


from project.hotel import Hotel
from project.room import Room
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 3)
        self.hotel = Hotel("Some Hotel")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.room.number, 1)
        self.assertEqual(self.room.capacity, 3)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(self.room.is_taken, False)

    def test_take_room_success(self):
        self.room.take_room(2)
        self.assertEqual(self.room.is_taken, True)
        self.assertEqual(self.room.guests, 2)

    def test_take_room_not_enough_capacity(self):
        result = self.room.take_room(4)
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(result, "Room number 1 cannot be taken")

    def test_take_room_not_free(self):
        self.room.take_room(1)
        result = self.room.take_room(1)
        self.assertEqual(self.room.is_taken, True)
        self.assertEqual(self.room.guests, 1)
        self.assertEqual(result, "Room number 1 cannot be taken")

    def test_free_room_success(self):
        self.room.take_room(1)
        self.room.free_room()
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)

    def test_free_room_not_taken(self):
        result = self.room.free_room()
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(result, "Room number 1 is not taken")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.hotel.name, "Some Hotel")
        self.assertEqual(self.hotel.rooms, [])
        self.assertEqual(self.hotel.guests, 0)

    def test_class_methods_creates_a_hotel(self):
        hotel = Hotel.from_stars(3)
        self.assertEqual(hotel.name, "3 stars Hotel")
        self.assertEqual(self.hotel.rooms, [])
        self.assertEqual(self.hotel.guests, 0)

    def test_add_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.assertEqual(self.hotel.rooms, [room])

    def test_take_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        self.assertEqual(self.hotel.rooms[0].is_taken, True)

    def test_free_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        self.hotel.free_room(1)
        self.assertEqual(self.hotel.guests, 0)
        self.assertEqual(self.hotel.rooms[0].is_taken, False)
        self.assertEqual(self.hotel.rooms[0].guests, 0)

    def test_print_status(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        res = self.hotel.status().strip()
        actual = 'Hotel Some Hotel has 3 total guests\nFree rooms: \nTaken rooms: 1'
        self.assertEqual(res, actual)


if __name__ == "__main__":
    unittest.main()
