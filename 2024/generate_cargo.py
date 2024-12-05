#!/usr/bin/env python3
"""Generate Cargo.toml workspace and package files for Advent of Code solutions."""

import sys
from pathlib import Path

import toml

WORKSPACE_TEMPLATE = """\
[workspace]
members = [
{}
]
resolver = "2"
"""

PACKAGE_TEMPLATE = """\
[package]
name = "{}"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "{}"
path = "src/main.rs"

[dependencies]
{}
"""


def has_valid_rust_setup(day_dir: Path) -> bool:
    """Check if directory has a src/main.rs file."""
    return (day_dir / "src" / "main.rs").exists()


def find_rust_days(directory: Path) -> list[str]:
    """Find all day directories containing Rust files."""
    # Convert to absolute path to ensure consistent directory scanning
    directory = directory.resolve()
    return sorted(
        d.name
        for d in directory.iterdir()
        if d.is_dir() and d.name.startswith("day") and has_valid_rust_setup(d)
    )


def extract_dependencies(cargo_toml_path: Path) -> dict:
    """Extract dependencies from an existing Cargo.toml file."""
    try:
        with cargo_toml_path.open("r") as f:
            cargo_data = toml.load(f)
            return cargo_data.get("dependencies", {})
    except Exception as e:
        print(
            f"Warning: Failed to read dependencies from {cargo_toml_path}: {e}",
            file=sys.stderr,
        )
        return {}


def format_dependencies(deps: dict) -> str:
    """Format the dependencies dictionary into TOML format."""
    if not deps:
        return ""
    lines = []
    for dep, version in deps.items():
        if isinstance(version, dict):
            # Handle complex dependency specifications
            lines.append(
                f'{dep} = {{ {", ".join(f"{k} = {v}" for k, v in version.items())} }}'
            )
        else:
            lines.append(f'{dep} = "{version}"')
    return "\n".join(lines)


def create_package_toml(day_dir: Path) -> None:
    """Create or update Cargo.toml for a day with its dependencies."""
    cargo_toml = day_dir / "Cargo.toml"

    existing_deps = {}
    if cargo_toml.exists():
        existing_deps = extract_dependencies(cargo_toml)
        print(f"Found existing dependencies in {cargo_toml}: {existing_deps}")

    new_deps = (
        existing_deps  # You can modify this if you have standard dependencies to add
    )

    formatted_deps = format_dependencies(new_deps)

    content = PACKAGE_TEMPLATE.format(day_dir.name, day_dir.name, formatted_deps)

    cargo_toml.write_text(content)
    if cargo_toml.exists():
        action = "Updated" if existing_deps else "Created"
        print(f"{action} {cargo_toml}")


def generate_cargo_toml(directory: Path = Path(".")) -> None:
    """Main function to generate all necessary Cargo.toml files."""
    try:
        # Ensure we're working with absolute paths
        directory = directory.resolve()

        # Find day directories with Rust files
        days = find_rust_days(directory)
        if not days:
            print("No day directories with Rust files found!")
            return

        # Create or update package Cargo.toml files
        for day in days:
            create_package_toml(directory / day)

        # Write workspace Cargo.toml
        members = "\n".join(f'    "{day}",' for day in days)
        content = WORKSPACE_TEMPLATE.format(members)

        workspace_toml = directory / "Cargo.toml"
        workspace_toml.write_text(content)
        print(f"Generated workspace Cargo.toml with {len(days)} Rust solutions.")
        # print(content)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    generate_cargo_toml()
