#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import annotations


def intro(age: int, name: str) -> None:
    print(f"{name} is {age} years old.")
    return


class Person:
    name: str
    age: int

    def __init__(self: Person, name: str, age: int) -> None:
        self.name = name
        self.age = age


def main() -> None:
    person: Person = Person(
        name="Taro",
        age=3,
    )
    intro(**vars(person))
    return


if __name__ == "__main__":
    main()
