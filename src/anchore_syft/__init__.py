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


def _run(name, args, capture_output=True):
    return subprocess.run(
        [os.path.join(BIN_DIR, name)] + args, capture_output=capture_output
    )


# Return value of type subprocess.CompletedProcess
def run(*args):
    return _run("syft", list(args))


def syft():
    raise SystemExit(_program("syft", sys.argv[1:]))
