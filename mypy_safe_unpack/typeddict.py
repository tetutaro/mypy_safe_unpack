#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t


def intro(age: int, name: str) -> None:
    print(f"{name} is {age} years old.")
    return


class TypedPerson(t.TypedDict):
    name: str
    age: int


def main() -> None:
    person: TypedPerson = TypedPerson(
        name="Taro",
        age=3,
    )
    intro(**person)
    return


if __name__ == "__main__":
    main()