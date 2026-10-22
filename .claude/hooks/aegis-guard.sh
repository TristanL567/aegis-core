#!/bin/sh
# Runs aegis_guard.py with the first Python that really starts (on Windows,
# python3 may be a store stub). Without Python the rules stay written only.
dir=$(dirname "$0")
for py in python3 python py; do
    if command -v "$py" >/dev/null 2>&1 && "$py" -c "import sys" >/dev/null 2>&1; then
        exec "$py" "$dir/aegis_guard.py" "$@"
    fi
done
echo "AEGIS guard warning: no Python found; rules are not enforced" >&2
exit 0
