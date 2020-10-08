from setuptools import setup

setup(
    name="pytest-suite-execution",
    version= '0.1.1',
    description="A Pytest plugin to excute test suite's in a specified order using a json file",
    author='Sivaram SV',
    author_email='sivaramshibu@live.com',
    license='MIT',
    py_modules=['pytest_suite_execution'],
    url='https://github.com/SivaRamSV/Pytest_Test_suite_sequence',
    install_requires=['pytest'],
    entry_points = {'pytest11': ['suite = pytest_suite_execution']
    },
)