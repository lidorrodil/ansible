#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Addional Info:
                The main() executes the image_comparison() which iterating over the file line by line and calling to:
                  - files_exist()
                  - check_demension()

                files_exist() checks if the original and mask image exist otherwise a msg will be written to the logger

                check_demension() checks if the original and mask image have the same demension
'''

import argparse
import logging
import os.path
from PIL import Image

# Create logger
logger = logging.getLogger('logger')


def image_comparison(pair_file, dataset_root):
    '''The script will go over each row in the `pair-file` argument and check:
       1. Both original and mask files exist in the `dataset-root` folder
       2. Original and mask files have the same dimension

       The script should output the list of files that don't meet the above requirements.'''

    # Iterate over the file line by line
    try:
        with open(pair_file) as fp:
            for (cnt, line) in enumerate(fp):
                image_line = line.split()
                try:
                    original_img = image_line[0].replace('/', '\\')
                    mask_img = image_line[1].replace('/', '\\')
                    if files_exist(dataset_root, original_img, mask_img):
                        check_demension(dataset_root, original_img, mask_img)
                except Exception as error:
                    logger.error(str(error) + ' in line %i' % cnt)
    except Exception as error:
        logger.error(str(error))

def check_demension(dataset_root, original_img, mask_img):
    '''Second task is to check that both original and mask files have the same dimension'''

    try:
        original_dem = Image.open(dataset_root + original_img)
        try:
            mask_dem = Image.open(dataset_root + mask_img)
            if original_dem.size != mask_dem.size:
                logger.error("Dimension isn't equal:\n%s - %s , %s - %s" % (original_dem.size, original_img, mask_dem.size, mask_img))
        except Exception as error:
            logger.error('The mask image seems to be corrupted')
    except Exception as error:
        logger.error('The original image seems to be corrupted')

def files_exist(dataset_root, original_img, mask_img):
    '''First task is to check that both original and mask files exist in the `dataset-root` folder'''

    result = True

    if not os.path.isfile(dataset_root + original_img):
        logger.error('Missing original dataset root: %s ' % original_img)
        result = False

    if not os.path.isfile(dataset_root + mask_img):
        logger.error('Missing mask dataset root: %s ' % mask_img)
        result = False

    return result

def main():

    # Define arguments
    parser = \
        argparse.ArgumentParser(description='Helper to the task.')
    parser.add_argument('-p', '--pair-file',
                        help='Path to the pairs file', required=True)
    parser.add_argument('-d', '--dataset-root',
                        help='Path to the root folder', required=True)

    # Parse arguments
    args = parser.parse_args()

    pair_file = args.pair_file
    dataset_root = args.dataset_root

    # Define the logger
    hdlr = logging.FileHandler('logger.log')
    formatter = \
        logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                          datefmt='%m/%d/%Y %I:%M:%S %p')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    # Set console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)

    image_comparison(pair_file, dataset_root)

if __name__ == '__main__':
    main()
