import asyncio
import warnings

from deprecation import UnsupportedWarning


async def async_test(value, warn=False):
    await asyncio.sleep(0)
    if warn:
        warnings.warn(UnsupportedWarning("old", "1", "2"))
    return value


async def run_together(*coroutines):
    return await asyncio.gather(*coroutines, return_exceptions=True)


async def capture_in_test():
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        await asyncio.sleep(0)
        warnings.warn(UnsupportedWarning("old", "1", "2"))
        return len(caught)
