# Smeagle Python

[![PyPI version](https://badge.fury.io/py/smeagle.svg)](https://badge.fury.io/py/smeagle)
[![ELF ABI Parsing Basic Tests](https://github.com/buildsi/smeagle-py/actions/workflows/basic-tests.yaml/badge.svg)](https://github.com/buildsi/smeagle-py/actions/workflows/basic-tests.yaml)

Generate facts for ELF binaries with debug information.

## Usage

First create a virtual environment and install dependencies.

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -e .
```

Or you can install the latest release from pypi:

```bash
$ pip install smeagle
```

If you need a quick binary with debug, compile the example:

```bash
cd example
make
```

Here is the usage in python:

```python
from smeagle.loader import Loader

ld = Loader("example/libmath-v1.so")
print(ld.corpus.to_json())
```

And an example [dev.py](dev.py) is provided to do the same and print to the terminal:

```bash
$ python dev.py example/libmath-v1.so
```
```
{
    "library": "/home/vanessa/Desktop/Code/smeagle-py/example/libmath-v1.so",
    "locations": [
        {
            "function": {
                "name": "_ZN11MathLibrary10Arithmetic3AddEdd",
                "class": "Function",
                "parameters": [
                    {
                        "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                        "location": "%xmm0",
                        "direction": "import"
                    },
                    {
                        "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                        "location": "%xmm1",
                        "direction": "import"
                    }
                ],
                "return": {
                    "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                    "direction": "export",
                    "location": "%xmm0"
                },
                "direction": "export"
            }
        },
        {
            "function": {
                "name": "_ZN11MathLibrary10Arithmetic8SubtractEdd",
                "class": "Function",
                "parameters": [
                    {
                        "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                        "location": "%xmm0",
                        "direction": "import"
                    },
                    {
                        "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                        "location": "%xmm1",
                        "direction": "import"
                    }
                ],
                "return": {
                    "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                    "direction": "export",
                    "location": "%xmm0"
                },
                "direction": "export"
            }
        },
        {
            "function": {
                "name": "_ZN11MathLibrary10Arithmetic8MultiplyEdd",
                "class": "Function",
                "parameters": [
                    {
                        "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                        "location": "%xmm0",
                        "direction": "import"
                    },
                    {
                        "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                        "location": "%xmm1",
                        "direction": "import"
                    }
                ],
                "return": {
                    "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                    "direction": "export",
                    "location": "%xmm0"
                },
                "direction": "export"
            }
        },
        {
            "function": {
                "name": "_ZN11MathLibrary10Arithmetic6DivideEdd",
                "class": "Function",
                "parameters": [
                    {
                        "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                        "location": "%xmm0",
                        "direction": "import"
                    },
                    {
                        "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                        "location": "%xmm1",
                        "direction": "import"
                    }
                ],
                "return": {
                    "type": "d20be53e889d2cee0c86d0ef9b0fbbc8",
                    "direction": "export",
                    "location": "%xmm0"
                },
                "direction": "export"
            }
        }
    ],
    "types": {
        "d20be53e889d2cee0c86d0ef9b0fbbc8": {
            "type": "double",
            "size": 8,
            "class": "Float"
        }
    }
}
```

## Tests

The test cases are stored in an external repository, so they can be shared. You can
run tests as follows:

```bash
git clone https://github.com/buildsi/smeagle-examples ./tests/examples

# Install extra test deps (assuming smeagle already installed, as shown above)
pip install pytest deepdiff
cd tests/

# Compile tests with a consistent compiler
docker run -t -v $PWD:/code gcc:12.1 bash -c "cd /code && make"

# Run tests
pytest -xs test_examples.py
```

## Authors

 - [@vsoch](https://github.com/vsoch)
 - [@hainest](https://github.com/hainest)

## License

This project is part of Spack. Spack is distributed under the terms of both the MIT license and the Apache License (Version 2.0). Users may choose either license, at their option.

All new contributions must be made under both the MIT and Apache-2.0 licenses.

See LICENSE-MIT, LICENSE-APACHE, COPYRIGHT, and NOTICE for details.

SPDX-License-Identifier: (Apache-2.0 OR MIT)

LLNL-CODE-811652
