#!/bin/sh
python3 -m src.make_archive
python3 -m src.main --vfs minimal.zip --script scripts/vfs_test.txt