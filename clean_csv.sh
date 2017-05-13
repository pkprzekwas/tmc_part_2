#!/bin/bash
set -e
a=$(find . -name *.csv | wc -l)
rm $(find . -name *.csv)
echo "Removed $a csv files."
