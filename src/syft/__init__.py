import os
import platform
import subprocess
import sys
import glob
from ._version import __version__, __version_tuple__

DATA = os.path.join(os.path.dirname(__file__), "data")
BIN_DIR = os.path.join(DATA, "bin")
SYFT_LIB_ENV = os.environ


def _program(name, args):
    return subprocess.call([os.path.join(BIN_DIR, name)] + args, env=SYFT_LIB_ENV)


def syft():
    raise SystemExit(_program("syft", sys.argv[1:]))
