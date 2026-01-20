import json
from pathlib import Path

from pymirtoolbox.feature_extractor import get_metadata_path


def test_metadata_file_exists_and_is_valid_json():
    meta_path = Path(get_metadata_path())
    assert meta_path.is_file()
    data = json.loads(meta_path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)


def test_metadata_structure_and_indices_and_params():
    meta_path = Path(get_metadata_path())
    data = json.loads(meta_path.read_text(encoding="utf-8"))
    for feature_name, spec in data.items():
        assert "name" in spec
        assert isinstance(spec["name"], str)

        assert "category" in spec
        assert isinstance(spec["category"], str)

        assert "description" in spec
        assert isinstance(spec["description"], str)

        assert "outputs" in spec
        outputs = spec["outputs"]
        assert isinstance(outputs, dict)
        indices = []
        for out_name, out_spec in outputs.items():
            assert isinstance(out_name, str)
            assert isinstance(out_spec, dict)
            assert "index" in out_spec
            idx = out_spec["index"]
            assert isinstance(idx, int)
            assert idx >= 1
            indices.append(idx)
            assert "description" in out_spec
            assert "type" in out_spec
            assert "shape" in out_spec
            assert "units" in out_spec
        assert len(indices) == len(set(indices))

        assert "params" in spec
        params = spec["params"]
        assert isinstance(params, dict)
        for param_name, p in params.items():
            assert isinstance(param_name, str)
            assert "type" in p
            assert p["type"] in ("bool", "number", "string")
            assert "example" in p
            assert "default" in p
            assert "description" in p
            assert "unit" in p
