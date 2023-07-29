# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pytest

from chatapp.profanitymasker.masker import ProfanityMasker


def test_one_bad_word() -> None:
    masker = ProfanityMasker()
    assert masker.mask("This is bullshit") == "This is bull***"


def test_two_bad_words() -> None:
    masker = ProfanityMasker()
    assert masker.mask("You bastard. Son of a bitch!") == "You ***. Son of a ***!"
