from __future__ import annotations

import platform

_system = platform.system().lower()

if _system == "darwin":
    from .macos import *
elif _system == "linux":
    from .linux import *
elif _system == "windows":
    from .macos import *
else:
    raise RuntimeError(f"Unsupported OS for pymirtoolbox_runtime: {_system}")
