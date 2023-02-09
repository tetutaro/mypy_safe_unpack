#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t


def intro(age: int, name: str) -> None:
    print(f"{name} is {age} years old.")
    return


class NamedPerson(t.NamedTuple):
    name: str
    age: int


def main() -> None:
    person: NamedPerson = NamedPerson(
        name="Taro",
        age=3,
    )
    intro(**person._asdict())
    return


if __name__ == "__main__":
    main()
