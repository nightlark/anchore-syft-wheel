Syft Python Distributions
=========================

[![PyPI](https://img.shields.io/pypi/v/anchore-syft.svg)](https://pypi.org/project/anchore-syft)

A project that packages Syft as a Python package, enabling `syft` to be installed from PyPI:

```sh
pip install anchore_syft
```

Afterwards, Syft can be run using either `syft` or `anchore_syft`.

PyPI package versions will follow the `major.minor.patch` version numbers of Syft releases.

Binary wheels for Windows, macOS, and Linux for most CPU architectures supported on PyPI are provided.

[Syft PyPI Package Homepage](https://github.com/nightlark/anchore-syft-wheel)

[Syft Source Code](https://github.com/anchore/syft)

[Syft License](https://github.com/anchore/syft/blob/main/LICENSE): Apache-2.0

Installing Syft
===============

Syft can be installed by pip with:

```sh
pip install anchore_syft
```

or:

```sh
python -m pip install anchore_syft
```

Building from the source dist package requires internet access in order to download one of the pre-compiled release binaries from <https://github.com/anchore/syft/releases>.
Platforms that Syft doesn't provide pre-compiled binaries for will not work at all, unless someone feels inclined to submit a PR that fetches an appropriate Go compiler
to build Syft from source.

Using with pipx
===============

Using `pipx run anchore_syft <args>` will run Syft without any install step, as long as the machine has pipx installed (which includes GitHub Actions runners).

Using with pyproject.toml
=========================

Syft can be added to the `project.dependencies` key in a pyproject.toml file for Python packages that require Syft.

```toml
[project]
dependencies = ["anchore_syft"]
```

License
=======

The code for this project is covered by the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0). Source distributions do not include a copy of the Syft source code or binaries. Binary wheels include a compiled Syft binary, which also falls under the Apache 2.0 license.

Syft is distributed under the [Apache License, Version 2.0](https://github.com/anchore/syft/blob/main/LICENSE). For more information about Syft, visit [https://github.com/anchore/syft](https://github.com/anchore/syft)
