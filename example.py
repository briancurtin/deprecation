import deprecation
__version__ = "1.5"


@deprecation.deprecated(deprecated_in="1.0", removed_in="2.0",
                        current_version=__version__,
                        details="Use the bar function instead")
def foo():
    """Do some stuff"""
    return 1
