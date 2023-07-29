# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import green

from chatapp.contentbuilder.builder import ContentBuilder


def print_content() -> None:
    content = ContentBuilder().build("Pantsbuild")
    print(green(content))


if __name__ == "__main__":
    print_content()
