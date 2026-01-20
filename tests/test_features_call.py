import json
import os
from pathlib import Path

import numpy as np
import pytest

from pymirtoolbox import feature_extractor
from pymirtoolbox.feature_extractor import get_metadata_path

_meta_path = Path(get_metadata_path())
_meta = json.loads(_meta_path.read_text(encoding="utf-8"))
_feature_names = list(_meta.keys())


def _audio_input_for_feature(feature_name: str) -> str:
    params = _meta[feature_name]["params"]
    p = params["audio_input"]
    value = p["example"]
    return str(Path(__file__).parents[1] / value)


def _build_kwargs_for_feature(feature_name: str):
    spec = _meta[feature_name]
    params = spec.get("params", {})
    kwargs = {}
    for param_name, p in params.items():
        value = p["example"]
        if param_name == "audio_input":
            value = str(Path(__file__).parents[1] / value)
        kwargs[param_name] = value
    return kwargs


@pytest.mark.parametrize("feature_name", _feature_names)
def test_feature_plain_call_returns_named_outputs(feature_name):
    func = getattr(feature_extractor, feature_name)
    audio_input = _audio_input_for_feature(feature_name)
    result = func(audio_input=audio_input)
    assert isinstance(result, dict)

    expected_outputs = set(_meta[feature_name]["outputs"].keys())
    result_outputs = set(result.keys())
    assert expected_outputs == result_outputs

    for key in expected_outputs:
        value = result[key]
        assert isinstance(value, np.ndarray)
        assert value.size > 0


@pytest.mark.parametrize("feature_name", _feature_names)
def test_feature_call_with_kwargs_from_metadata(feature_name):
    func = getattr(feature_extractor, feature_name)
    kwargs = _build_kwargs_for_feature(feature_name)
    result = func(**kwargs)
    assert isinstance(result, dict)

    expected_outputs = set(_meta[feature_name]["outputs"].keys())
    result_outputs = set(result.keys())
    assert expected_outputs == result_outputs

    for key in expected_outputs:
        value = result[key]
        assert isinstance(value, np.ndarray)
        assert value.size > 0
