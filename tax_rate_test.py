#!/usr/bin/python3
from tax_rate import TaxRate, TaxBracket


def test_tax_rate() -> None:
    federal_single_2023 = TaxRate(
        (
            TaxBracket(11_000, 0.1),
            TaxBracket(44_725, 0.12),
            TaxBracket(95_375, 0.22),
            TaxBracket(182_100, 0.24),
            TaxBracket(231_250, 0.32),
            TaxBracket(578_125, 0.35),
            TaxBracket(float("inf"), 0.37),
        )
    )

    assert (
        federal_single_2023(50_000)
        == 11_000 * 0.1 + (44_725 - 11_000) * 0.12 + (50_000 - 44_725) * 0.22
    )

    assert federal_single_2023(50_000, 1000) == 11_000 * 0.1 + (
        44_725 - 11_000
    ) * 0.12 + (50_000 - 44_725) * 0.22 + 1000 * (0.22 - 0.1)


if __name__ == "__main__":
    test_tax_rate()
