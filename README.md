# Conan2 Structure Prototype

A minimal example to prototype Conan 2 usage and amenability to our developer workflow.

## Usage

./build_all.sh

## Fail cases:

* Case_01 (build_01_fail.sh):
  * fails on `Case_01/test_packages`:
    It requires `Case_01/mid_a`, which requires `Up/up_a`,
    but transitive headers are turned off:
    * Thus, example.cpp indirect attempt to include `up_a.h` via `mid.h` fails.
