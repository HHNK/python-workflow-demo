#!/bin/bash
set -e  # Exit on any error

# Clone the repo if it doesn't exist
if [ ! -d "../hhnk-threedi-tools" ]; then
    git clone https://github.com/threedi/hhnk-threedi-tools/ ../hhnk-threedi-tools
fi

# Install with the same pip flags as in the Windows script
pip install --no-build-isolation --no-deps --disable-pip-version-check -e ../hhnk-threedi-tools
