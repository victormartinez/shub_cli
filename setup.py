from codecs import open
from os.path import abspath, dirname, join
from setuptools import find_packages, setup
from shub_cli import __version__ as VERSION
from pip.req import parse_requirements

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


def _to_list(requires):
    return [str(ir.req) for ir in requires]


install_requires = _to_list(parse_requirements('requirements.txt', session=False))
tests_require = _to_list(parse_requirements('requirements-test.txt', session=False))

setup(
    name='shub-cli',
    version=VERSION,
    description='A CLI at your hands to deal with the features of ScrapingHub.',
    long_description=long_description,
    url='https://github.com/victormartinez/shub_cli',
    author='Victor Martinez',
    author_email='vcrmartinez@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    tests_require=tests_require,
    install_requires=install_requires,
    setup_requires=['pytest-runner==2.8'],
    entry_points={
        'console_scripts': [
            'shub-cli=shub_cli.cli:main',
        ],
    }
)
