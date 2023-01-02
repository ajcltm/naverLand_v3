import os
import logging

from naverLand import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('config')

def check_right_parent_dir(dir_naverLand, dir_data):
    if not dir_naverLand == config.dir_main:
        return False
    if not dir_data == config.dir_main.parent:
        return False
    return True

def make_dir(dir):
    dir_project = dir.parent
    dir_naverLand = dir_project.parent
    dir_data = dir_naverLand.parent
    if not check_right_parent_dir(dir_naverLand=dir_naverLand, dir_data=dir_data) :
        raise Exception('It seems not to be the naverLand directory...')
    
    if not os.path.exists(dir_project):
        os.mkdir(dir_project)
        logger.info(f'The project directory is made : {dir}')

    if not os.path.exists(dir):
        os.mkdir(dir)
        logger.info(f'a directory ia made : {dir}')

