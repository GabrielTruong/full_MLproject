from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(path:str)->List[str]:
    '''
    This function will return a list from the requirements.txt file
    '''
    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
name="full_ML_project",
version="0.1",
author="Gabriel TRUONG",
author_email="gabriel.truong@epfedu.fr",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)