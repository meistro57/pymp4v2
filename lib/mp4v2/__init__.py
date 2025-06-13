"""Cython bindings for libmp4v2.

The extension module is built from ``ext/mp4file.pyx`` and exposes an
``MP4File`` class.  Importing this package will load the compiled
extension if available.
"""

from importlib import import_module

try:
    mp4file = import_module("mp4v2.mp4file")
except Exception as exc:  # pragma: no cover - extension not built
    raise ImportError(
        "The mp4v2 Cython extension is not built or failed to load"
    ) from exc

__all__ = ["mp4file"]
