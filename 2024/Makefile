# Makefile for Advent of Code 2024 Solutions

# Find all day directories
DAYS := $(sort $(wildcard day*))
LATEST_DAY := $(lastword $(DAYS))
DAY ?= $(LATEST_DAY)

# Binary names
BINARY_GO := gomain
BINARY_RUST := target/release/$(DAY)
BINARY_ZIG := zigmain
BINARY_MOJO := mojomain

# Source file paths
EXISTING_PYTHON := $(wildcard $(DAY)/src/main.py)
EXISTING_GO := $(wildcard $(DAY)/src/main.go)
EXISTING_RUST := $(wildcard $(DAY)/src/main.rs)
EXISTING_ZIG := $(wildcard $(DAY)/src/main.zig)
EXISTING_MOJO := $(wildcard $(DAY)/src/main.mojo)

# Binaries for existing source files
BINARIES := $(if $(EXISTING_GO),$(BINARY_GO))
BINARIES += $(if $(EXISTING_RUST),$(BINARY_RUST))
BINARIES += $(if $(EXISTING_ZIG),$(BINARY_ZIG))
BINARIES += $(if $(EXISTING_MOJO),$(BINARY_MOJO))

# Benchmark commands for existing implementations
BENCH_COMMANDS += $(if $(EXISTING_PYTHON),'python3 src/main.py')
BENCH_COMMANDS := $(if $(EXISTING_GO),'./$(BINARY_GO)')
BENCH_COMMANDS += $(if $(EXISTING_RUST),'../$(BINARY_RUST)')
BENCH_COMMANDS += $(if $(EXISTING_ZIG),'./$(BINARY_ZIG)')
BENCH_COMMANDS += $(if $(EXISTING_MOJO),'./$(BINARY_MOJO)')

# Optimization flags
GO_FLAGS := -ldflags="-s -w" -trimpath
ZIG_FLAGS := -O ReleaseFast -fstrip -fsingle-threaded

.PHONY: benchmark clean build go zig rust mojo which-day init-cargo help list-days run-%

all: benchmark

# Default target
.DEFAULT_GOAL := help

# Display the current day being used
which-day:
	@echo "Using $(DAY) (Latest: $(LATEST_DAY))"

# Initialize Cargo workspace and packages
init-cargo:
	@cd $(CURDIR) && uv run generate_cargo.py

# Benchmark the solutions for the current day
benchmark: which-day build
	@cd $(DAY) && hyperfine -N --warmup 5 $(BENCH_COMMANDS)
	@$(MAKE) -s clean-local

# Build all existing implementations for the current day
build:
	@$(MAKE) init-cargo
	@if [ -n "$(EXISTING_GO)" ]; then \
		cd $(DAY) && go build $(GO_FLAGS) -o $(BINARY_GO) src/main.go; \
	fi
	@if [ -n "$(EXISTING_ZIG)" ]; then \
		cd $(DAY) && zig build-exe $(ZIG_FLAGS) src/main.zig -femit-bin=$(BINARY_ZIG); \
	fi
	@if [ -n "$(EXISTING_RUST)" ]; then \
		cargo build --release --package $(DAY); \
	fi
	@if [ -n "$(EXISTING_MOJO)" ]; then \
		cd $(DAY) && mojo build src/main.mojo -o $(BINARY_MOJO); \
	fi

# Language-specific build targets
go: $(BINARY_GO)
rust: $(BINARY_RUST)
zig: $(BINARY_ZIG)
mojo: $(BINARY_MOJO)

# Go build rule
$(BINARY_GO): $(EXISTING_GO)
	cd $(DAY) && go build $(GO_FLAGS) -o $@ src/main.go

# Rust build rule using Cargo
$(BINARY_RUST): $(EXISTING_RUST)
	cargo build --release --package $(DAY)

# Zig build rule
$(BINARY_ZIG): $(EXISTING_ZIG)
	cd $(DAY) && zig build-exe $(ZIG_FLAGS) src/main.zig -femit-bin=$@

# Clean binaries specific to the current day
clean-local:
	@rm -f $(DAY)/$(BINARY_GO) $(DAY)/$(BINARY_ZIG) $(DAY)/$(BINARY_MOJO)

# Clean all build artifacts
clean: clean-local
	@if [ -f Cargo.toml ]; then \
		if cargo clean 2>/dev/null; then \
			true; \
		else \
			echo "Warning: cargo clean failed, but continuing..."; \
		fi \
	fi

# List all available days
list-days:
	@echo "Available days: $(DAYS)"

# Run benchmark for a specific day (e.g., make run-1)
run-%:
	@$(MAKE) benchmark DAY=day$*

# Display help
help:
	@echo "Available targets:"
	@echo "  make              - Show this help message"
	@echo "  make DAY=dayX      - Run benchmark for specific day (defaults to latest day)"
	@echo "  make run-X         - Run benchmark for day X (e.g., make run-1)"
	@echo "  make which-day     - Show which day is being used"
	@echo "  make list-days     - List all available days"
	@echo "  make init-cargo    - Generate/update Cargo.toml files"
	@echo "  make benchmark     - Build and benchmark the current day"
	@echo "  make build         - Build all existing implementations for the current day"
	@echo "  make clean         - Clean up build artifacts"
	@echo "  make help          - Show this help message"

# ============================
# Zig Targets
# ============================

.PHONY: build-zig run-zig clean-zig zig-action

# Generic target to build, run, and clean Zig solution for specified day
zig-action: build-zig run-zig clean-zig
	@echo "Completed zig-action for Day $(DAY)."

# Build the Zig project for the specified day using zig build-exe
build-zig:
	@echo "Building Zig solution for Day $(DAY)..."
	@cd day$(DAY) && zig build-exe $(ZIG_FLAGS) src/main.zig -femit-bin=$(BINARY_ZIG)

# Run the compiled Zig executable for the specified day
run-zig:
	@echo "Running Zig solution for Day $(DAY)..."
	@./day$(DAY)/$(BINARY_ZIG)

# Clean the Zig build artifacts for the specified day
clean-zig:
	@echo "Cleaning Zig build artifacts for Day $(DAY)..."
	@rm -f day$(DAY)/$(BINARY_ZIG)
