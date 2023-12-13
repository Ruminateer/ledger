#!/usr/bin/python3

import sys
import csv
from evaluate import evaluate


class Transaction:
    people = {}

    def __init__(self, creditor: str, amount: float, debtors: list, notes: list):
        self.creditor = creditor
        self.amount = amount
        self.debtors = debtors if debtors else Transaction.people
        self.note = notes

        Transaction.people[self.creditor] -= self.amount
        amountpp = self.amount / len(self.debtors)
        for p in self.debtors:
            Transaction.people[p] += amountpp

    @classmethod
    def from_list(cls, l: list):
        if not l:
            return ""
        return Transaction(l[0], evaluate(l[1]), l[2].split(), l[3:])

    def __str__(self) -> str:
        debtors_str = (
            ",".join(self.debtors)
            if len(self.debtors) < len(Transaction.people)
            else "all"
        )
        result = f"{self.creditor} paid {self.amount:.2f} for {debtors_str}"
        if self.note:
            result += f"\t# {' '.join(self.note)}"
        return result


def load_names(filename: str) -> None:
    with open(filename, encoding="utf-8", newline="") as file:
        for row in csv.reader(file, skipinitialspace=True):
            for cell in row:
                if cell:
                    Transaction.people[cell] = 0


def settle_transactions(filenames: list) -> None:
    for filename in filenames:
        with open(filename, encoding="utf-8", newline="") as file:
            for row in csv.reader(file, skipinitialspace=True):
                print(Transaction.from_list(row))
    print("\nSummary:")
    for p, amount in Transaction.people.items():
        print(f"{p} owes {amount:.2f}")


if __name__ == "__main__":
    load_names(sys.argv[1])
    settle_transactions(sys.argv[2:])
