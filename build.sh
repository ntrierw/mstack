#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Run the static site generator
python3 generator.py

# Move the generated files to the root of output directory
# Cloudflare Pages will serve from the configured output directory
mv output/content/* output/ 2>/dev/null || true
