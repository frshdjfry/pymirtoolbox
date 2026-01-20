from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_metadata(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def group_by_category(meta: dict) -> dict:
    categories: dict = {}
    for feature_name, spec in meta.items():
        category = spec.get("category", "uncategorized")
        categories.setdefault(category, []).append((feature_name, spec))
    for cat in categories:
        categories[cat].sort(key=lambda pair: pair[0])
    return categories


def render_feature_md(name: str, spec: dict) -> str:
    lines: list[str] = []
    lines.append(f"### `{name}`")
    lines.append("")
    desc = str(spec.get("description", "")).strip()
    if desc:
        lines.append(desc)
        lines.append("")
    outputs = spec.get("outputs", {})
    if outputs:
        lines.append("**Outputs**")
        lines.append("")
        lines.append("| Name | Type | Shape | Units | Description |")
        lines.append("| ---- | ---- | ----- | ----- | ----------- |")
        for out_name, out_spec in outputs.items():
            otype = out_spec.get("type", "")
            shape = out_spec.get("shape", "")
            units = out_spec.get("units", "")
            odesc = out_spec.get("description", "")
            lines.append(
                f"| `{out_name}` | {otype} | {shape} | {units} | {odesc} |"
            )
        lines.append("")
    params = spec.get("params", {})
    if params:
        lines.append("**Parameters**")
        lines.append("")
        lines.append("| Name | Type | Default | Example | Unit | Description |")
        lines.append("| ---- | ---- | ------- | ------- | ---- | ----------- |")
        for pname, pspec in params.items():
            ptype = pspec.get("type", "")
            default = pspec.get("default", None)
            example = pspec.get("example", "")
            unit = pspec.get("unit", "")
            pdesc = pspec.get("description", "")
            if default is None:
                default_disp = "null"
            else:
                default_disp = str(default)
            example_disp = str(example)
            lines.append(
                f"| `{pname}` | {ptype} | {default_disp} | {example_disp} | {unit} | {pdesc} |"
            )
        lines.append("")
    return "\n".join(lines)


def render_md(meta: dict, title: str) -> str:
    grouped = group_by_category(meta)
    parts: list[str] = [f"# {title}", ""]
    for category in sorted(grouped.keys()):
        parts.append(f"## {category.capitalize()}")
        parts.append("")
        for feature_name, spec in grouped[category]:
            parts.append(render_feature_md(feature_name, spec))
    parts.append("")
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Markdown docs for MIR features.")
    parser.add_argument(
        "--metadata",
        default="feature_metadata.json",
        help="Path to feature metadata JSON file.",
    )
    parser.add_argument(
        "--output",
        default="-",
        help="Output Markdown file path, or '-' for stdout.",
    )
    parser.add_argument(
        "--title",
        default="pymirtoolbox.feature_extractor",
        help="Top-level title for the document.",
    )
    args = parser.parse_args()

    meta_path = Path(args.metadata)
    meta = load_metadata(meta_path)
    md = render_md(meta, title=args.title)

    if args.output == "-" or not args.output:
        sys.stdout.write(md)
    else:
        out_path = Path(args.output)
        out_path.write_text(md, encoding="utf-8")


if __name__ == "__main__":
    main()
