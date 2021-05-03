#!/usr/bin/python3 -OO
"""bastipy is just a module with some helpers for me """


def ic(*a):  # pylint: disable=invalid-name
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


try:
    import psutil  # type: ignore[import]
except ImportError:
    pass
else:

    def bastitiming(func):
        """bastitiming is a decorator to time calls by process timings"""
        save = func.__name__

        def wrapped(*args, **kwargs):
            before = psutil.Process().cpu_times()
            retval = func(*args, **kwargs)
            after = psutil.Process().cpu_times()
            print(
                f"{save} took ",
                before.__class__(
                    *(after[i] - before[i] for i in range(len(before)))
                ),
            )
            return retval

        return wrapped


if __name__ == "__main__":
    print("DANKE Basti")
