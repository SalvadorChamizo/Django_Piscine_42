#!/usr/bin/bash

set -euo pipefail

if ! command -v pip >/dev/null 2>&1; then
    echo "Error: pip not found"
    exit 1
fi

pip --version

rm -rf local_lib

git clone https://github.com/jaraco/path.py.git local_lib > install.log 2>&1

python3 my_program.py