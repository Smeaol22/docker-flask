# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    my_license = f.read()

setup(
    name='docker_flask',
    version='0.0.1',
    description='put your description',
    long_description=readme,
    author='Dauloudet Olivier',
    url='https://github.com/Smeaol22/docker_flask',
    license=my_license,
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
