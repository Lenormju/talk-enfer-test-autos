#!/bin/bash
set -euo pipefail

mkdir -p public
uv tool run mkslides \
    build \
    --config-file 'mkslides_config.yml' \
    --site-dir 'public' \
    --strict \
    'src/slides.md'

#xdg-open "file://$(pwd)/public/index.html"
