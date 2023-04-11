"""Stubs file for `deprecation.py`.

Created using mypy's `stubgen`, types manually corrected.
"""

import datetime
from packaging import version
from typing import Callable, Optional, Union

message_location: str

class DeprecatedWarning(DeprecationWarning):
    function: str
    deprecated_in: Union[datetime.date, version.Version, None]
    removed_in: Union[datetime.date, version.Version, None]
    details: Union[datetime.date, version.Version, None]
    def __init__(
        self,
        function: str,
        deprecated_in: Union[datetime.date, version.Version, None],
        removed_in: Union[datetime.date, version.Version, None],
        details: str = ...,
    ) -> None: ...

class UnsupportedWarning(DeprecatedWarning): ...

def deprecated(
    deprecated_in: Union[str, datetime.date, version.Version, None] = ...,
    removed_in: Union[str, datetime.date, version.Version, None] = ...,
    current_version: Union[str, datetime.date, version.Version, None] = ...,
    details: str = ...,
) -> Callable: ...
def fail_if_not_removed(method: Callable) -> Callable: ...
