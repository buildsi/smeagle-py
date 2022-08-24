# Smeagle Python

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

### Authors

 - [@vsoch](https://github.com/vsoch)
 - [@hainest](https://github.com/hainest)

### License

This project is part of Spack. Spack is distributed under the terms of both the MIT license and the Apache License (Version 2.0). Users may choose either license, at their option.

All new contributions must be made under both the MIT and Apache-2.0 licenses.

See LICENSE-MIT, LICENSE-APACHE, COPYRIGHT, and NOTICE for details.

SPDX-License-Identifier: (Apache-2.0 OR MIT)

LLNL-CODE-811652
