#!/usr/bin/env -S python3.10 -OO
"""bastipy is just a module with some helpers for me """
from os import times_result
from typing import Any, Callable, TypeVar


def ic(*a) -> Any | tuple[Any, ...] | None:  # pylint: disable=invalid-name
    """Just in case package icecream is not available: For logging purpuses."""
    if not a:
        return None
    return a[0] if len(a) == 1 else a


if __debug__:
    try:
        from icecream import ic  # type: ignore[import,no-redef]  # noqa: F811,W0404
    except ImportError:
        pass  # Fallback to default
    else:
        ic.configureOutput(includeContext=True)  # type: ignore[attr-defined]
try:
    from cpu_load_generator import load_single_core  # type: ignore[import]
except ImportError:
    pass
else:

    def loadonecore(
        loadduration: int = 10, loadedcore: int = 0, theload: float = 0.5
    ) -> None:
        """just a helper function to generate load on one given core"""
        load_single_core(
            core_num=loadedcore,
            duration_s=loadduration,
            target_load=theload,
        )


try:
    from cpu_load_generator import load_all_cores  # type: ignore[import]
except ImportError:
    pass
else:

    def loadallcores(loadduration: int = 10, theload: float = 0.5) -> None:
        """just a helper function to generate load on all cores"""
        load_all_cores(duration_s=loadduration, target_load=theload)


InnerFunctionReturnType = TypeVar("InnerFunctionReturnType")
try:
    import psutil  # type: ignore[import]
except ImportError:
    import os

    ic("Timing of function with the help of module os")

    def bastitiming(
        func: Callable[..., InnerFunctionReturnType]
    ) -> Callable[..., InnerFunctionReturnType]:
        """bastitiming is a decorator to time calls"""
        savename: str = func.__name__

        def wrapped(*args, **kwargs) -> InnerFunctionReturnType:
            beforesys: times_result = os.times()
            retval: InnerFunctionReturnType = func(*args, **kwargs)
            aftersys: times_result = os.times()
            thediffsys: times_result = beforesys.__class__(
                aftersys[i] - beforesys[i] for i in range(len(beforesys))
            )
            print(f"processing of {savename} took {thediffsys}")
            return retval

        return wrapped

else:
    ic("Timing of function with the help of module psutil")

    def bastitiming(
        func: Callable[..., InnerFunctionReturnType]
    ) -> Callable[..., InnerFunctionReturnType]:
        """bastitiming is a decorator to time calls"""
        savename = func.__name__

        def wrapped(*args, **kwargs) -> InnerFunctionReturnType:
            beforesys = psutil.cpu_times()
            before = psutil.Process().cpu_times()
            retval: InnerFunctionReturnType = func(*args, **kwargs)
            after = psutil.Process().cpu_times()
            aftersys = psutil.cpu_times()
            thediff = before.__class__(
                *(after[i] - before[i] for i in range(len(before)))
            )
            thediffsys = beforesys.__class__(
                *(aftersys[i] - beforesys[i] for i in range(len(beforesys)))
            )
            print(f"processing of {savename} took")
            print(f"{thediff} in total {sum(thediff)}")
            print(f"{thediffsys} in total {sum(thediffsys)}")
            return retval

        return wrapped


if __name__ == "__main__":
    print("DANKE Basti")
    bastitiming(loadallcores)(15, 0.9)
    print("Basti fertig")
