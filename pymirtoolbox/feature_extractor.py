from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict
from pathlib import Path

import numpy as np
import pymirtoolbox


@dataclass
class MirComponent:
    comp: Any

    def feature_dispatcher(self, *args: Any) -> Any:
        return self.comp.feature_dispatcher(*args)

    def terminate(self) -> None:
        self.comp.terminate()


_component: MirComponent | None = None


def _get_component() -> MirComponent:
    global _component
    if _component is None:
        comp = pymirtoolbox.initialize()
        _component = MirComponent(comp)
    return _component


def get_metadata_path() -> str:
    return str(Path(__file__).with_name("feature_metadata.json"))


def _to_numpy_dict(result: Any) -> Dict[str, np.ndarray]:
    if hasattr(result, "_fieldnames"):
        out: Dict[str, np.ndarray] = {}
        for name in result._fieldnames():
            value = getattr(result, name)
            out[str(name)] = np.asarray(value)
        return out
    if hasattr(result, "keys"):
        return {str(k): np.asarray(v) for k, v in result.items()}
    return {"value": np.asarray(result)}


def _kwargs_to_matlab_args(kwargs: Dict[str, Any]) -> list[Any]:
    args: list[Any] = []
    for k, v in kwargs.items():
        if isinstance(v, bool):
            if v:
                args.append(k)
        else:
            args.append(k)
            if isinstance(v, int):
                v = float(v)
            args.append(v)
    return args


class FeatureExtractor:
    def __getattr__(self, name: str) -> Callable[..., Dict[str, np.ndarray]]:
        def _call(**kwargs: Any) -> Dict[str, np.ndarray]:
            if "audio_input" not in kwargs:
                raise TypeError("audio_input keyword argument is required")
            audio_input = kwargs.pop("audio_input")
            metadata_path = get_metadata_path()
            matlab_kwargs = _kwargs_to_matlab_args(kwargs)
            comp = _get_component()
            raw = comp.feature_dispatcher(name, audio_input, metadata_path, *matlab_kwargs)
            return _to_numpy_dict(raw)

        return _call


feature_extractor = FeatureExtractor()
