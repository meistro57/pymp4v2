# pymp4v2

This repository contains a historical Cython wrapper around the
[libmp4v2](https://github.com/sergiomb2/libmp4v2) library.  It was
initially built for Python 2 and last touched over a decade ago.

The code exposes an `MP4File` object implemented in Cython
(`ext/mp4file.pyx`).  Building the extension requires development
headers for `libmp4v2` which are not currently installed in this
environment.

## Current status

* The build uses `setuptools`/Cython.  You must have Cython installed.
* The library targets Python 2 semantics and has not been updated for
  Python 3.
* Tests expect `nose` and Pillow and rely on sample media files which
  are missing from this repository.

Given the missing dependencies and the age of the code, significant
work would be required to bring it up to date.  Consider using modern
alternatives such as [`pymp4`](https://pypi.org/project/pymp4/) or
[`mutagen`](https://mutagen.readthedocs.io/) for manipulating MP4
metadata.
