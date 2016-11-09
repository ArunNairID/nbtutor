#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copied and modified from
# https://github.com/Anaconda-Platform/nbpresent/tree/master/nbpresent/tasks
import os
import shutil
import sys

from . import _env


def main(**opts):
    shutil.copyfile(
        os.path.join(_env.SRC, "js", "index.js"),
        os.path.join(_env.DIST, "js", "nbtutor.min.js")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
