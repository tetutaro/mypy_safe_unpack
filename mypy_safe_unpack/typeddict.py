#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t

from mypy_safe_unpack.intro import intro_keyword


class TypedPerson(t.TypedDict):
    name: str
    age: int


def main() -> None:
    person: TypedPerson = TypedPerson(
        name="Taro",
        age=3,
    )
    intro_keyword(**person)
    return


if __name__ == "__main__":
    main()
