#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import annotations

from mypy_safe_unpack.intro import intro_keyword


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
    intro_keyword(**vars(person))
    return


if __name__ == "__main__":
    main()
