from setuptools import find_packages, setup

setup(
    name='cliologging',
    packages=find_packages(include=['cliologging']),
    version='1.0.0',
    description='Add-on to the official Python logging library.',
    author='Julien BALDERIOTTI',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)