from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_metadata(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def py_type(t: str) -> str:
    if t == "bool":
        return "bool"
    if t == "number":
        return "float"
    if t == "string":
        return "str"
    return "object"


def format_default(val) -> str:
    if val is None:
        return "..."
    if isinstance(val, bool):
        return "True" if val else "False"
    if isinstance(val, (int, float)):
        return repr(val)
    if isinstance(val, str):
        return repr(val)
    return "..."


def render_feature_method(name: str, spec: dict) -> str:
    params = spec.get("params", {})
    audio_param = params.get("audio_input")
    if audio_param is None:
        raise ValueError(f"Feature {name} is missing required 'audio_input' param")
    lines: list[str] = []
    sig_parts: list[str] = ["self", "*"]
    sig_parts.append("audio_input: str")
    for pname, pspec in params.items():
        if pname == "audio_input":
            continue
        ptype = py_type(pspec.get("type", "object"))
        default = pspec.get("default", None)
        default_str = format_default(default)
        sig_parts.append(f"{pname}: {ptype} = {default_str}")
    sig = ", ".join(sig_parts)
    lines.append(f"    def {name}({sig}) -> Dict[str, np.ndarray]: ...")
    return "\n".join(lines)


def render_pyi(meta: dict) -> str:
    lines: list[str] = []
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from typing import Any, Callable, Dict")
    lines.append("import numpy as np")
    lines.append("")
    lines.append("")
    lines.append("class FeatureExtractor:")
    lines.append("    def __getattr__(self, name: str) -> Callable[..., Dict[str, np.ndarray]]: ...")
    lines.append("")
    for feature_name in sorted(meta.keys()):
        spec = meta[feature_name]
        lines.append(render_feature_method(feature_name, spec))
        lines.append("")
    lines.append("")
    lines.append("feature_extractor: FeatureExtractor")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate .pyi stubs for FeatureExtractor from feature metadata.")
    parser.add_argument(
        "--metadata",
        default="feature_metadata.json",
        help="Path to feature metadata JSON file.",
    )
    parser.add_argument(
        "--output",
        default="feature_extractor.pyi",
        help="Output .pyi file path.",
    )
    args = parser.parse_args()

    meta_path = Path(args.metadata)
    meta = load_metadata(meta_path)
    pyi_text = render_pyi(meta)

    out_path = Path(args.output)
    out_path.write_text(pyi_text, encoding="utf-8")


if __name__ == "__main__":
    main()
