#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t
import typing_extensions as te


class IntroKwargs(t.TypedDict):
    fullname: str
    birthyear: int


def intro(
    age: int,
    name: str,
    *args: te.Unpack[t.Tuple[int, ...]],
    **kwargs: te.Unpack[t.TypedDict],
) -> None:
    print(f"{name} is {age} years old.")
    print(args)
    print(kwargs)
    return


def main() -> None:
    intro(3, "Taro", 1, 2, fullname="Yamada Taro", birthyear=2020)
    return


if __name__ == "__main__":
    main()
