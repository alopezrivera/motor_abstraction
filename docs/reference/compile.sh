#!/bin/bash

# Remove any previous documentation
find . -name 'project*rst'
find . -name 'project*rst' -delete
# Clean
make clean

# Generate site
make html
find . -name 'project*rst'
find . -name 'project*rst' -delete

# Remove LaTeX artifacts
make latex
find . -name 'project*rst'
find . -name 'project*rst' -delete

# Build
cd build
cd latex
make LATEXMKOPTS="-lualatex"
