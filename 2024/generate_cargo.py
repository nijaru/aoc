#!/usr/bin/env python3
"""Generate Cargo.toml workspace and package files for Advent of Code solutions."""

import sys
from pathlib import Path

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


def create_package_toml(day_dir: Path) -> None:
    """Create Cargo.toml for a day if it doesn't exist and has Rust files."""
    if not has_valid_rust_setup(day_dir):
        return

    cargo_toml = day_dir / "Cargo.toml"
    if not cargo_toml.exists():
        content = PACKAGE_TEMPLATE.format(day_dir.name, day_dir.name)
        cargo_toml.write_text(content)
        print(f"Created {cargo_toml}")


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

        # Create package Cargo.toml files if needed
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
