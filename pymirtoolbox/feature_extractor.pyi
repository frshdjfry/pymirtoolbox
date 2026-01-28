from __future__ import annotations

from typing import Any, Callable, Dict
import numpy as np


class FeatureExtractor:
    def __getattr__(self, name: str) -> Callable[..., Dict[str, np.ndarray]]: ...

    def mirkeystrength(self, *, audio_input: str, Frame: bool = False, Weight: float = ..., Triangle: bool = ...) -> Dict[str, np.ndarray]: ...


feature_extractor: FeatureExtractor
