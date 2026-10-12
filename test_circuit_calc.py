import math
import unittest

from circuit_calc import (
    current,
    parallel_resistance,
    parse_value,
    power,
    rc_charge_voltage,
    rc_time_constant,
    ripple_voltage,
    series_resistance,
    voltage,
    voltage_divider,
)


class OhmsLawTest(unittest.TestCase):
    def test_current(self):
        self.assertAlmostEqual(current(12, 4), 3)

    def test_voltage(self):
        self.assertAlmostEqual(voltage(2, 5), 10)

    def test_power(self):
        self.assertAlmostEqual(power(12, 2), 24)

    def test_zero_resistance_is_rejected(self):
        with self.assertRaises(ValueError):
            current(5, 0)


class ResistorTest(unittest.TestCase):
    def test_series(self):
        self.assertAlmostEqual(series_resistance([100, 220, 330]), 650)

    def test_parallel_equal_resistors(self):
        self.assertAlmostEqual(parallel_resistance([100, 100]), 50)

    def test_parallel_three_resistors(self):
        self.assertAlmostEqual(parallel_resistance([10, 20, 20]), 5)

    def test_empty_list_is_rejected(self):
        with self.assertRaises(ValueError):
            parallel_resistance([])

    def test_voltage_divider(self):
        self.assertAlmostEqual(voltage_divider(10, 1000, 1000), 5)


class CapacitorTest(unittest.TestCase):
    def test_time_constant(self):
        self.assertAlmostEqual(rc_time_constant(10_000, 100e-6), 1.0)

    def test_charge_after_one_time_constant(self):
        expected = 5 * (1 - math.exp(-1))
        self.assertAlmostEqual(rc_charge_voltage(5, 10_000, 100e-6, 1.0), expected)

    def test_negative_time_is_rejected(self):
        with self.assertRaises(ValueError):
            rc_charge_voltage(5, 1000, 1e-6, -1)

    def test_full_wave_ripple(self):
        self.assertAlmostEqual(ripple_voltage(0.5, 50, 2200e-6), 0.5 / 0.22)

    def test_half_wave_ripple_is_twice_as_large(self):
        full = ripple_voltage(0.5, 50, 2200e-6, full_wave=True)
        half = ripple_voltage(0.5, 50, 2200e-6, full_wave=False)
        self.assertAlmostEqual(half, 2 * full)


class ParseValueTest(unittest.TestCase):
    def test_plain_number(self):
        self.assertAlmostEqual(parse_value("2.2"), 2.2)

    def test_kilo(self):
        self.assertAlmostEqual(parse_value("4.7k"), 4700)

    def test_micro(self):
        self.assertAlmostEqual(parse_value("100u"), 100e-6)

    def test_milli_and_mega_are_different(self):
        self.assertAlmostEqual(parse_value("5m"), 0.005)
        self.assertAlmostEqual(parse_value("5M"), 5_000_000)

    def test_scientific_notation(self):
        self.assertAlmostEqual(parse_value("1e3"), 1000)

    def test_bad_text_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_value("abc")


if __name__ == "__main__":
    unittest.main()
