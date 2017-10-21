"""Setup.py config."""
from setuptools import setup

setup(
    name='code_katas',
    description='A package for Code War kata answers and tests.',
    package_dir={'': 'src'},
    author='Cody Dibble',
    author_email='hcodydibble@gmail.com',
    py_modules=['code_katas'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
)
