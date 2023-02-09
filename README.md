# mypy_safe_unpack

find the data container type of Python that can unpack and give it to the function as arguments and pass the mypy test.

## Tests

* `make unpack-everything`
    * print itself
    * give it to the function as positional arguments
    * give it to the function as keyword arguments
    * try above three test with instance (`person`), single-starred instance (`*person`) and double-starred instance (`**person`)
    * testing data container type is...
        * `Tuple`
        * `List`
        * `Set`
        * `Dict`
        * `collections.namedtuple`
        * `typing.NamedTuple`
        * `typing.NamedTuple._asdict()`
        * `typing.TypedDict`
        * `class`
        * `vars(class)`
        * `pydantic.BaseModel`
        * `pydantic.BaseModel.dict()`
* `make unpack-each-type`
    * give double-starred instance to the function as keyword arguments again
        * that can give arguments exactly
        * `Dict`
        * `Dict[Any, Any]`
        * `Dict[str, Any]`
        * `Dict[str, Union[int, str]]`
        * `typing.NamedTuple._asdict()`
        * `typing.TypedDict`
        * `vars(class)`
        * `pydantic.BaseModel.dict()`
* `make mypy-safe-type`
    * do the mypy test that can pass it and can set type hints collectly
        * `typing.NamedTuple._asdict()`
        * `typing.TypedDict`
        * `vars(class)`
        * `pydantic.BaseModel.dict()`
* `make mypy-unsafe-type`
    * do the mypy test that can pass it but use Any (unsafe)
        * `Dict`
        * `Dict[Any, Any]`
        * `Dict[str, Any]`
* `make mypy-failed-type`
    * do the mypy test that failed it
        * `Dict[str, Union[int, str]]`
* `make starrd-expression`
    * add type hints to starrd expressions in the definition of the function
    * check the function works as usual
* `make mypy-stared-expression`
    * do the mypy test to the function with type hints of starred expression
    * `mypy >= 1.0.0` is needed
