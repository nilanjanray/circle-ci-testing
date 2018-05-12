from setuptools import *
import sys

NAME='deadsnake'
DESCRIPTION='description'
AUTHOR='Nilanjan'
EMAIL='roy.nilanjan@gmail.com'
setup(
    name=NAME,
    version=sys.version,
    description=DESCRIPTION,
    # long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    # python_requires=REQUIRES_PYTHON,
    # url=URL,
    # packages=find_packages('mypackage'),
    # If your package is a single module, use this instead of 'packages':
    py_modules=['memcache_stat'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    #install_requires=REQUIRED,
    #include_package_data=True,
)
