#!/usr/bin/python3
import unittest
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation"""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_state_id_is_public_class_attribute(self):
        cty = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cty))
        self.assertNotIn("state_id", cty.__dict__)


if __name__ == "__main__":
    unittest.main()
