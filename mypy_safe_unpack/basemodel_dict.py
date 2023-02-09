#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from pydantic import BaseModel


def intro(age: int, name: str) -> None:
    print(f"{name} is {age} years old.")
    return


class BasePerson(BaseModel):
    name: str
    age: int


def main() -> None:
    person: BasePerson = BasePerson(
        name="Taro",
        age=3,
    )
    intro(**person.dict())
    return


if __name__ == "__main__":
    main()
