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

from mypy_safe_unpack.intro import (
    intro_position,
    intro_keyword,
    print_blue,
    print_red,
)


def apply_each(person: t.Any, nstar: int) -> None:
    try:
        if nstar == 0:
            print(person)
        elif nstar == 1:
            print(*person)
        else:
            print(**person)
    except Exception as e:
        print_red(f"PRINT: {e}")
    try:
        if nstar == 0:
            intro_position(person)
        elif nstar == 1:
            intro_position(*person)
        else:
            intro_position(**person)
    except Exception as e:
        print_red(f"POSITION: {e}")
    try:
        if nstar == 0:
            intro_keyword(person)
        elif nstar == 1:
            intro_keyword(*person)
        else:
            intro_keyword(**person)
    except Exception as e:
        print_red(f"KEYWORD: {e}")
    return


def apply(pat: str, person: t.Any) -> None:
    # no star expression
    print_blue(f"===  {pat}  ===")
    apply_each(person=person, nstar=0)
    # single star expression
    print_blue(f"=== * {pat} * ===")
    apply_each(person=person, nstar=1)
    # double star expression
    print_blue(f"=== ** {pat} ** ===")
    apply_each(person=person, nstar=2)
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
