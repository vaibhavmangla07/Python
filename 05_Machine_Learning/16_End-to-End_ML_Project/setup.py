from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> list:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

setup(
    name='end_to_end_ml_project',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='An end-to-end machine learning project for anomaly detection using Isolation Forest.',
    author='Vaibhav Mangla',
    author_email='vmangla0704@gmail.com'
)