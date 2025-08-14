from setuptools import find_packages, setup
from typing import List


hypen_e_dot='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requriments which mentioned in requriments.txt
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readline()
        requirments=[req.replace('\n','') for req in requirments]

        if hypen_e_dot in requirments:
            requirments.remove(hypen_e_dot)

    return requirments
        




setup(
    name='mlproject',
    version='0.0.1',
    author='logesh',
    author_email='logeshkumarradhakrishnan94@gmail.com',
    packages=find_packages(),
    install_requriments=get_requirments('requirments.txt')
)