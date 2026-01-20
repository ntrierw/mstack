# Cloudflare Pages Configuration

This repository is configured to build on Cloudflare Pages with the following settings:

## Build Configuration

When setting up your Cloudflare Pages project, use these settings:

- **Framework preset**: None
- **Build command**: `./build.sh`
- **Build output directory**: `output`
- **Root directory**: `/` (leave empty or default)

## Build Process

The build script (`build.sh`) will:
1. Install Python dependencies from `requirements.txt`
2. Run the static site generator (`generator.py`)
3. Move generated files to the output directory

## Python Runtime

The project uses Python 3.11 as specified in `runtime.txt`.

## Files Added for Cloudflare Pages

- `requirements.txt` - Python dependencies (markdown library)
- `build.sh` - Build script executed by Cloudflare Pages
- `runtime.txt` - Python version specification
- `CLOUDFLARE_PAGES.md` - This configuration guide

No existing source code was modified to make this Cloudflare Pages compatible.
