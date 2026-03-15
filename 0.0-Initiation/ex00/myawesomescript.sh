#!/bin/sh

set -eu

if command -v curl >/dev/null 2>&1; then
    curl -sI "$1" | grep -i '^Location' | cut -d ' ' -f2
fi