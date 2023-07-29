# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from chatapp.contentbuilder.builder import ContentBuilder


def test_ordinary_content() -> None:
    greeter = ContentBuilder()
    assert greeter.build("This is an ordinary content") == "This is an ordinary content"

def test_content_with_bad_words() -> None:
    greeter = ContentBuilder()
    assert greeter.build("This is a shitty content") == "This is a ***ty content"
