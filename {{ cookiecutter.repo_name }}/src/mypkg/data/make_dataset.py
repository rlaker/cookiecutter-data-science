# -*- coding: utf-8 -*-
import argparse
import os
import logging
from pathlib import Path
# from dotenv import find_dotenv, load_dotenv


# THIS IS OLD CODE FROM http://drivendata.github.io/cookiecutter-data-science/
# will be useful if you need to store secret keys 


def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    # Create the parser
    parser = argparse.ArgumentParser(description='Process some folders.')

    # Add the arguments
    parser.add_argument('input_folder',
                        metavar='input_folder',
                        type=str,
                        help='the path to the input folder')

    parser.add_argument('output_folder',
                        metavar='output_folder',
                        type=str,
                        help='the path to the output folder')

    # Execute the parse_args() method
    args = parser.parse_args()


    # Ensure the input folder exists
    if not os.path.isdir(args.input_folder):
        print(f"The specified input folder does not exist: {args.input_folder}")
        exit()

    # Ensure the output folder exists; if not, create it
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
        print(f"Created the output folder: {args.output_folder}")


    main(args.input_folder, args.output_folder)
