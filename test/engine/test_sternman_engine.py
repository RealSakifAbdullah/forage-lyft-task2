import unittest
from datetime import datetime
from engine.models.sternman_engine import SternmanEngine


class TestWilloughbyEngine(unittest.TestCase):

    def test_engine_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())


    def test_engine_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
