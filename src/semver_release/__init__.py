try:
    from ._version import version as __version__
except ImportError:  # the project is not packaged or installed
    __version__ = '0.0.0+unknown'
