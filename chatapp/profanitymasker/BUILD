# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
python_sources(
    name="lib",
    dependencies=[":bad_words"],
)

# This target sets the metadata for all the Python test files in this directory.
python_tests(
    name="tests",
)

# This target teaches Pants about our JSON file, which allows other targets to depend on it.
resource(
    name="bad_words",
    source="bad_words.json",
)

# This target allows us to build a `.whl` bdist and a `.tar.gz` sdist by auto-generating
#  `setup.py`. See https://www.pantsbuild.org/docs/python-distributions.
#
# Because this target has no source code, Pants cannot infer dependencies. We depend on `:lib`,
#  which means we'll include all the non-test Python files in this directory, and any of
#  their dependencies.
python_distribution(
    name="dist",
    dependencies=[":lib"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="chatapp.profanitymasker",
        version="0.0.1",
        description="A profanity masker.",
    ),
)
