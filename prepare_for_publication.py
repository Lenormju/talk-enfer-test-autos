# /// script
# dependencies = [
#   "pyyaml",
# ]
# ///

import argparse
import sys
from pathlib import Path

import yaml


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config_filepath", type=Path, required=True)
    parser.add_argument("-s", "--slides_filepath", type=Path, required=True)
    args = parser.parse_args()
    config_filepath: Path = args.config_filepath
    slides_filepath: Path = args.slides_filepath

    with config_filepath.open("rt") as config_file:
        document = yaml.safe_load(config_file)
    document["slides"]["theme"] = "dracula"
    document["revealjs"]["navigationMode"] = "linear"
    with args.config_filepath.open("wt") as config_file:
        yaml.safe_dump(document, config_file)

    slides = slides_filepath.read_text()
    slides_without_fragments = slides.replace("<!-- .element: class=\"fragment\" -->", "")
    slides_filepath.write_text(slides_without_fragments)

    return 0


if __name__ == "__main__":
    sys.exit(main())
