BINARY_GO := gomain
BINARY_ZIG := zigmain
BINARY_RUST := rustmain

# Find existing source files
EXISTING_GO := $(wildcard main.go)
EXISTING_ZIG := $(wildcard main.zig)
EXISTING_RUST := $(wildcard main.rs)
EXISTING_PYTHON := $(wildcard main.py)

# Only include binaries for existing source files
BINARIES := $(if $(EXISTING_GO),$(BINARY_GO))
BINARIES += $(if $(EXISTING_ZIG),$(BINARY_ZIG))
BINARIES += $(if $(EXISTING_RUST),$(BINARY_RUST))

# Create benchmark commands only for existing implementations
BENCH_COMMANDS := $(if $(EXISTING_GO),'./$(BINARY_GO)')
BENCH_COMMANDS += $(if $(EXISTING_ZIG),'./$(BINARY_ZIG)')
BENCH_COMMANDS += $(if $(EXISTING_RUST),'./$(BINARY_RUST)')
BENCH_COMMANDS += $(if $(EXISTING_PYTHON),'python3 -OO main.py')

# Maximum optimization flags for each compiler
GO_FLAGS := -ldflags="-s -w" -trimpath
ZIG_FLAGS := -O ReleaseFast -fstrip -fsingle-threaded
RUST_FLAGS := -C opt-level=3 -C target-cpu=native -C lto=true -C codegen-units=1 -C panic=abort

.PHONY: benchmark clean build $(LANGUAGES)

benchmark: build
	hyperfine -N --warmup 5 $(BENCH_COMMANDS)
	@$(MAKE) -s clean

build: $(BINARIES)

# Language-specific builds
go: $(BINARY_GO)
zig: $(BINARY_ZIG)
rust: $(BINARY_RUST)

$(BINARY_GO): $(EXISTING_GO)
	go build $(GO_FLAGS) -o $@ main.go

$(BINARY_ZIG): $(EXISTING_ZIG)
	zig build-exe $(ZIG_FLAGS) main.zig -femit-bin=$@

$(BINARY_RUST): $(EXISTING_RUST)
	rustc $(RUST_FLAGS) main.rs -o $@

clean:
	@rm -f $(BINARIES) zigmain.o
