#!/usr/bin/python3
import unittest

from tax_calculator import Bracket, Tax


class TestTaxCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.federal_single_2023 = Tax(
            (
                Bracket(11_000, 0.1),
                Bracket(44_725, 0.12),
                Bracket(95_375, 0.22),
                Bracket(182_100, 0.24),
                Bracket(231_250, 0.32),
                Bracket(578_125, 0.35),
                Bracket(float("inf"), 0.37),
            )
        )

    def test_calculate(self) -> None:
        self.assertEqual(
            self.federal_single_2023.calculate(50_000),
            11_000 * 0.1 + (44_725 - 11_000) * 0.12 + (50_000 - 44_725) * 0.22,
        )

        self.assertEqual(
            self.federal_single_2023.calculate(50_000, 1_000),
            11_000 * 0.1
            + (44_725 - 11_000) * 0.12
            + (50_000 - 44_725) * 0.22
            + 1000 * (0.22 - 0.1),
        )
