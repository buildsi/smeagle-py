#!/usr/bin/env python3

import os
import sys

from smeagle.loader import Loader

path = sys.argv[1]
if not os.path.exists(path):
    sys.exit("%s does not exist" % path)
quiet = False
if "--quiet" in sys.argv:
    quiet = True
ld = Loader(path)
if not quiet:
    print(ld.corpus.to_json())
