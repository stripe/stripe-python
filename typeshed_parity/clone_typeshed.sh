# This script is intended to be run manually from time-to-time to update the
# checked-in copy of typeshed. It is not run as part of the build process.
#
# Expected to be run from REPO_ROOT/typeshed_parity
#!/usr/bin/env bash

set -ueo pipefail

DIR=typeshed
rm -rf $DIR
mkdir -p $DIR
git clone --filter=blob:none --no-checkout https://github.com/python/typeshed.git "$DIR"
cd $DIR
git sparse-checkout init --cone
git sparse-checkout set stubs/stripe/stripe
git checkout HEAD
git rev-parse HEAD > GIT_SHA
rm -rf .git
find . -type f -depth 1 | xargs rm
