#!/usr/bin/env bash

set -ueo pipefail

# This script is meant as a temporary measure to check the diff between
# the stubs that the `stubgen` tool produces based on the current typing
# annotations in this repo and the ones that are presently committed to
# the typeshed repo.
#
# Once we are satisfied with the stubs that `stubgen` produces, we can
# remove this script and the `stubdiff` directory from the repo.

# Take in path to python executable as first argument
# If no argument is provided, use the default python
PYTHON=${1:-python}

TYPESHED_DIR="typeshed"
${PYTHON} -c "import mypy.stubgen; mypy.stubgen.main(['-p', 'stripe'])"

# Make sure `find` produces relative paths
pushd out/stripe > /dev/null
FILES=$(find . -name '*.pyi')
popd > /dev/null

pushd $TYPESHED_DIR/stubs/stripe/stripe > /dev/null
for FILE in $FILES; do
    mkdir -p $(dirname $FILE)
    touch $FILE
done
popd > /dev/null

mkdir -p stubdiff

function filter_diff {
    # Remove lines that start with +++, ---, @@, or index or "diff --git"
    sed -e '/^+++/d' -e '/^---/d' -e '/^@@/d' -e '/^index/d' -e '/^diff --git/d'
}

process_file() {
  FILE="$1"
  OUTPUT_FILE="$FILE.diff"
  OUTPATH="stubdiff/$OUTPUT_FILE"
  mkdir -p $(dirname $OUTPATH)

  TYPESHED_SORTED=$(mktemp)
  STUBGEN_SORTED=$(mktemp)
  cat $TYPESHED_DIR/stubs/stripe/stripe/$FILE | ${PYTHON} pyi_sort.py > $TYPESHED_SORTED
  cat out/stripe/$FILE | ${PYTHON} pyi_sort.py > $STUBGEN_SORTED
  git diff --no-index $TYPESHED_SORTED $STUBGEN_SORTED | filter_diff > $OUTPATH
}

export -f process_file
export -f filter_diff
export TYPESHED_DIR
export PYTHON
echo "$FILES" | xargs -I {} -P "$(nproc)" bash -c 'process_file "{}"'
