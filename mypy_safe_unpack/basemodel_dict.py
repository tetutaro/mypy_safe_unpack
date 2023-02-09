#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from pydantic import BaseModel

from mypy_safe_unpack.intro import intro_keyword


class BasePerson(BaseModel):
    name: str
    age: int


def main() -> None:
    person: BasePerson = BasePerson(
        name="Taro",
        age=3,
    )
    intro_keyword(**person.dict())
    return


if __name__ == "__main__":
    main()
