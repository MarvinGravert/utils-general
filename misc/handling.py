from typing import Callable
from typing import List

# From plum https://github.com/beartype/plum

def is_in_class(f: Callable) -> bool:
    """Check if a function is part of a class.

    Args:
        f (function): Function to check.

    Returns:
        bool: Whether `f` is part of a class.
    """
    parts = f.__qualname__.split(".")
    return len(parts) >= 2 and parts[-2] != "<locals>"

def _split_parts(f: Callable) -> List[str]:
    qualified_name = f.__module__ + "." + f.__qualname__
    return qualified_name.split(".")


def get_class(f: Callable) -> str:
    """Assuming that `f` is part of a class, get the fully qualified name of the
    class.

    Args:
        f (function): Method to get class name for.

    Returns:
        str: Fully qualified name of class.
    """
    parts = _split_parts(f)
    return ".".join(parts[:-1])

def get_context(f) -> str:
    """Get the fully qualified name of the context for `f`.

    If `f` is part of a class, then the context corresponds to the scope of the class.
    If `f` is not part of a class, then the context corresponds to the scope of the
    function.

    Args:
        f (function): Method to get context for.

    Returns:
        str: The context of `f`.
    """
    parts = _split_parts(f)
    if is_in_class(f):
        # Split off function name and class.
        return ".".join(parts[:-2])
    else:
        # Split off function name only.
        return ".".join(parts[:-1])