#Code for project management

from setuptools import setup, find_packages

#read the contents of requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='hotel_reservation_prediction_MLOps_GCP',
    version='0.1',
    author='Swapnil Rokade',
    packages=find_packages(),
    install_requires=requirements,
)