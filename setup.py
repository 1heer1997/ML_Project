## responsible for creating machine learning application as a package and even deploying py.pi
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
     this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() ## read lines from .txt file but it will read with \n so we will do the following
        requirements=[req.replace("\n"," ") for req in requirements if HYPEN_E_DOT not in req] ## replace \n with blank

## it should not read -e . from req.txt, so eliminating that from reading
   ## if HYPEN_E_DOT in requirements:
     ##  requirements.remove(HYPEN_E_DOT)

    return requirements


setup(

name='ML_Project',
version='0.0.1',
author='Heer',
author_email='heerrvankawala@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)
