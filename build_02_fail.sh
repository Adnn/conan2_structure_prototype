set -e # Exit immediately if a command exits with non-zero

pushd Up
conan install .
conan build .
conan export-pkg .
popd

pushd Case_02
conan install .
conan build .
conan export-pkg .
popd

