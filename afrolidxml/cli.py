#!/usr/bin/env python3
import logging
import os
import sys
from pathlib import Path

import click
import predictions
from afrolid.main import classifier


@click.command()
@click.argument("input_file")
@click.argument("output_file")
@click.option("--model_path", "-m", required=True, help="Model path", type=str)
def main(input_file, output_file, model_path):
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=os.environ.get("LOGLEVEL", "INFO").upper(),
        force=True,  # Resets any previous configuration
    )
    logger = logging.getLogger("afrolid")

    # Check input and output filepaths
    if not Path(input_file).exists():
        print("Bad input file path")
        sys.exit(1)

    if Path(output_file).exists():
        print("Output file already exists")
        sys.exit(1)

    # Check model path
    if not Path(model_path).exists():
        print("Bad model path")
        sys.exit(1)

    # Analyze file contents using AfroLID's classifier and write XML file
    with open(input_file, encoding="utf-8") as file:
        text = file.read()

    cl = classifier(logger, model_path)
    predicted_languages = cl.classify(text, 3)
    predictions.write_predicted_languages_xml(predicted_languages, output_file)


if __name__ == "__main__":
    sys.exit(main())
