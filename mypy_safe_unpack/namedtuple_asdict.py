#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t

from mypy_safe_unpack.intro import intro_keyword


class NamedPerson(t.NamedTuple):
    name: str
    age: int


def main() -> None:
    person: NamedPerson = NamedPerson(
        name="Taro",
        age=3,
    )
    intro_keyword(**person._asdict())
    return


if __name__ == "__main__":
    main()
