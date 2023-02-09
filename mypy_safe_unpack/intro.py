#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def print_red(text: str) -> None:
    print(f"\x1b[31m{text}\x1b[0m")


def print_green(text: str) -> None:
    print(f"\x1b[32m{text}\x1b[0m")


def print_yellow(text: str) -> None:
    print(f"\x1b[33m{text}\x1b[0m")


def print_blue(text: str) -> None:
    print(f"\x1b[34m{text}\x1b[0m")


def intro_position(age: int, name: str) -> None:
    text = f"{name} is {age} years old."
    if text == "Taro is 3 years old.":
        print_green("POSITION: " + text)
    else:
        print_yellow("POSITION: " + text)


def intro_keyword(*, age: int, name: str) -> None:
    text = f"{name} is {age} years old."
    if text == "Taro is 3 years old.":
        print_green("KEYWORD: " + text)
    else:
        print_yellow("KEYWORD: " + text)
    return
