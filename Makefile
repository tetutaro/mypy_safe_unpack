.PHONY: unpack-everything
unpack-everything:
	@python -m mypy_safe_unpack.unpack_everything

.PHONY: unpack-each-type
unpack-each-type:
	@echo "Dict"
	@python -m mypy_safe_unpack.dict
	@echo "Dict[Any, Any]"
	@python -m mypy_safe_unpack.dict_any_any
	@echo "Dict[str, Any]"
	@python -m mypy_safe_unpack.dict_str_any
	@echo "Dict[str, Union[str, int]]"
	@python -m mypy_safe_unpack.dict_strict
	@echo "NamedTuple._asdict()"
	@python -m mypy_safe_unpack.namedtuple_asdict
	@echo "TypedDict"
	@python -m mypy_safe_unpack.typeddict
	@echo "vars(class)"
	@python -m mypy_safe_unpack.vars_class
	@echo "BaseModel.dict()"
	@python -m mypy_safe_unpack.basemodel_dict

.PHONY: mypy-safe-type
mypy-safe-type:
	@echo "NamedTuple._asdict()"
	@mypy mypy_safe_unpack/namedtuple_asdict.py
	@echo "TypedDict"
	@mypy mypy_safe_unpack/typeddict.py
	@echo "vars(class)"
	@mypy mypy_safe_unpack/vars_class.py
	@echo "BaseModel.dict()"
	@mypy mypy_safe_unpack/basemodel_dict.py

.PHONY: mypy-unsafe-type
mypy-unsafe-type:
	@echo "Dict"
	@mypy mypy_safe_unpack/dict.py
	@echo "Dict[Any, Any]"
	@mypy mypy_safe_unpack/dict_any_any.py
	@echo "Dict[str, Any]"
	@mypy mypy_safe_unpack/dict_str_any.py

.PHONY: mypy-failed-type
mypy-failed-type:
	@echo "Dict[str, Union[str, int]]"
	@mypy mypy_safe_unpack/dict_strict.py

.PHONY: starred-expression
starred-expression:
	@python -m mypy_safe_unpack.starred_expression

.PHONY: mypy-starred-expression
mypy-starred-expression:
	@mypy --enable-incomplete-feature=Unpack mypy_safe_unpack/starred_expression.py

.PHONY: clean
clean: clean-python clean-package clean-tests clean-system

.PHONY: clean-python
clean-python:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*.pyd' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +

.PHONY: clean-package
clean-package:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf .eggs/
	@find . -name '*.egg-info' -exec rm -rf {} +
	@find . -name '*.egg' -exec rm -rf {} +

.PHONY: clean-tests
clean-tests:
	@rm -rf .pytest_cache/
	@rm -rf .mypy_cache/
	@rm -rf .tox/
	@rm -f .coverage
	@rm -rf htmlcov/

.PHONY: clean-system
clean-system:
	@find . -name '*~' -exec rm -f {} +
	@find . -name '.DS_Store' -exec rm -f {} +

.PHONY: requirements
requirements:
	poetry export --without-hashes -f requirements.txt -o requirements.txt

.PHONY: stubs
stubs:
	stubgen -o . -p mypy_safe_unpack

.PHONY: build-package
build-package:
	$(eval VERSION := $(shell poetry version -s))
	poetry build
	@tar zxf dist/mypy_safe_unpack-$(VERSION).tar.gz -C ./dist
	@cp dist/mypy_safe_unpack-$(VERSION)/setup.py setup.py
	@black setup.py
	@rm -rf dist

.PHONY: install
install:
	python setup.py install

.PHONY: uninstall
uninstall:
	pip uninstall -y mypy-safe-unpack

.PHONY: docs
docs:
	cd docs && make html

.PHONY: tests
tests: tests-python

.PHONY: tests-python
tests-python:
	poetry run pytest

.PHONY: tests-report
tests-report:
	python -u -m pytest -v --cov --cov-report=html

# add new version number.
# do this after committing changes to the local repositry
# and before pushing changes to the remote repository.
.PHONY: version-up
version-up:
ifdef VERSION
	git tag $(VERSION)
	poetry dynamic-versioning
	git add pyproject.toml mypy_safe_unpack/__init__.py
	git commit -m "$(VERSION)"
	git tag -f $(VERSION)
	git push
	git push --tags
else
	@echo "Usage: make version-up VERSION=vX.X.X"
endif
