#!/usr/bin/env python3
from setuptools import setup

setup(
    name='pybcra',
    version='0.1.0',
    author='maekos',
    author_email='maekos@gmail.com',
    description='Estadisticas del Banco Central de la Republica Argentina.',
    url='https://github.com/maekos/pybcra',
    package_dir={'':'.'},
    packages=['bcra'],
    install_requires=[
        'requests',
    ],
)
