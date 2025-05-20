#!/bin/bash
SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

PDF_PATH="$SCRIPT_DIR/../../laporan_asli.pdf"

nohup python3 "$SCRIPT_DIR/update_check.py" >/dev/null 2>&1 &

xdg-open "$PDF_PATH" >/dev/null 2>&1 &
