# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

from chatapp.profanitymasker.masker import ProfanityMasker


class ContentBuilder:
    def __init__(self):
        self.masker = ProfanityMasker()

    def build(self, content: str) -> str:
        content = self.masker.mask(content)
        return content
