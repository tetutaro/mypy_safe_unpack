#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""関数の引数に **Dict を渡すと怒られるので、
怒られないやり方を探すため、思いつく限りの型で試してみる。

collections.abc に属するものは除外。
collections.abc は非常に勉強になる。

Dict = Set + Mapping。

freezeset と collections.OrderedDict, collections.defaultdict は
さすがにやめておく。

変数そのまま、* をつける、** をつけるの３バージョンでやってみる。
"""
from __future__ import annotations
import typing as t
from collections import namedtuple

from pydantic import BaseModel


def print_red(text: str) -> None:
    print(f"\x1b[31m{text}\x1b[0m")


def print_green(text: str) -> None:
    print(f"\x1b[32m{text}\x1b[0m")


def print_yellow(text: str) -> None:
    print(f"\x1b[33m{text}\x1b[0m")


def print_blue(text: str) -> None:
    print(f"\x1b[34m{text}\x1b[0m")


def intro(age: int, name: str, dummy: t.Optional[t.List] = None) -> None:
    text = f"{name} is {age} years old."
    if text == "Taro is 3 years old.":
        print_green("INTRO: " + text)
    else:
        print_yellow("INTRO: " + text)
    return


def apply(pat: str, person: t.Any) -> None:
    print_blue(f"===  {pat}  ===")
    try:
        print(person)
    except Exception as e:
        print_red(f"PRINT: {e}")
    try:
        intro(person)
    except Exception as e:
        print_red(f"INTRO: {e}")
    print_blue(f"=== * {pat} * ===")
    try:
        print(*person)
    except Exception as e:
        print_red(f"PRINT: {e}")
    try:
        intro(*person)
    except Exception as e:
        print_red(f"INTRO: {e}")
    print_blue(f"=== ** {pat} ** ===")
    try:
        print(**person)
    except Exception as e:
        print_red(f"PRINT: {e}")
    try:
        intro(**person)
    except Exception as e:
        print_red(f"INTRO: {e}")
    return


def main() -> None:
    # Tuple
    Tuple_person: t.Tuple[str, int] = ("Taro", 3)
    apply(pat="Tuple", person=Tuple_person)

    # List
    List_person: t.List[t.Union[str, int]] = ["Taro", 3]
    apply(pat="List", person=List_person)

    # Set
    Set_person: t.Set[t.Union[str, int]] = {"Taro", 3}
    apply(pat="Set", person=Set_person)

    # Dict
    Dict_person: t.Dict[str, t.Union[str, int]] = {
        "name": "Taro",
        "age": 3,
    }
    apply(pat="Dict", person=Dict_person)

    # namedtuple
    namedtuple_Person = namedtuple(
        "Person",
        [
            "name",
            "age",
        ],
    )
    namedtuple_person: namedtuple_Person = namedtuple_Person("Taro", 3)
    apply(pat="namedtuple", person=namedtuple_person)

    # NamedTuple
    class NamedTuple_Person(t.NamedTuple):
        name: str
        age: int

    NamedTuple_person: NamedTuple_Person = NamedTuple_Person(
        name="Taro",
        age=3,
    )
    apply(pat="NamedTuple", person=NamedTuple_person)

    # NamedTuple._asdict()
    apply(pat="NamedTuple.asdict()", person=NamedTuple_person._asdict())

    # TypedDict
    class TypedDict_Person(t.TypedDict):
        name: str
        age: int

    TypedDict_person: TypedDict_Person = TypedDict_Person(
        name="Taro",
        age=3,
    )
    apply(pat="TypedDict", person=TypedDict_person)

    # Class
    class class_Person:
        name: str
        age: int

        def __init__(self: class_Person, name: str, age: int) -> None:
            self.name = name
            self.age = age
            return

    class_person: class_Person = class_Person(name="Taro", age=3)
    apply(pat="class", person=class_person)

    # vars(class)
    apply(pat="vars(class)", person=vars(class_person))

    # BaseModel
    class BaseModel_Person(BaseModel):
        name: str
        age: int

    BaseModel_person: BaseModel_Person = BaseModel_Person(
        name="Taro",
        age=3,
    )
    apply(pat="BaseModel", person=BaseModel_person)

    # BaseModel.dict()
    apply(pat="BaseModel.dict()", person=BaseModel_person.dict())

    return


if __name__ == "__main__":
    main()
