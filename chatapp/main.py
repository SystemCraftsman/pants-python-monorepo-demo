# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import sys

from chatapp.contentbuilder.builder import ContentBuilder


def print_content(content: str) -> None:
    print(ContentBuilder().build(content))


if __name__ == "__main__":
    print_content(sys.argv[1])
