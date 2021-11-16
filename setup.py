#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()



test_requirements = [ ]

setup(
    author="Ana Sofia Carmo",
    author_email='anascacais@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="EpiBOX is a Raspberry Pi tool for easy signal acquisition.",
    entry_points={
        'console_scripts': [
            'epibox=epibox.cli:main',
        ],
    },
    install_requires=['alabaster==0.7.12', 'appdirs==1.4.4', 'argh==0.26.2', 'arrow==1.1.1', 'Babel==2.9.1', 'binaryornot==0.4.4', 'bitalino==1.2.1', 'bleach==3.3.0', 'certifi==2021.5.30', 'chardet==4.0.0', 'click', 'colorama==0.4.4', 'cookiecutter==1.7.3', 'distlib==0.3.2', 'docutils==0.17.1', 'entrypoints==0.3', 'filelock==3.0.12', 'idna==2.10', 'imagesize==1.2.0', 'install==1.3.4', 'Jinja2==3.0.1', 'jinja2-time==0.2.0', 'MarkupSafe==2.0.1', 'mccabe==0.6.1', 'numpy==1.21.0', 'packaging==21.0', 'paho-mqtt==1.5.1', 'pathtools==0.1.2', 'pexpect==4.8.0', 'pkginfo==1.7.0', 'pluggy', 'poyo==0.5.0', 'primefac==1.1', 'ptyprocess==0.7.0', 'py==1.10.0', 'pybluez2==0.41', 'pycodestyle==2.5.0', 'pyflakes==2.1.1', 'Pygments==2.9.0', 'pyparsing==2.4.7', 'pyserial==3.5', 'python-dateutil==2.8.1', 'python-slugify==5.0.2', 'pytz==2021.1', 'PyYAML==5.4.1', 'readme-renderer==29.0', 'requests==2.25.1', 'requests-toolbelt==0.9.1', 'scipy==1.7.0', 'six==1.16.0', 'snowballstemmer==2.1.0', 'Sphinx==1.8.5', 'sphinxcontrib-serializinghtml==1.1.5', 'sphinxcontrib-websupport==1.2.4', 'text-unidecode==1.3', 'toml==0.10.2', 'tox', 'tqdm==4.61.2', 'twine', 'urllib3==1.26.6', 'virtualenv==20.4.7', 'watchdog==0.9.0', 'webencodings==0.5.1'],
    license="MIT license",
    long_description_content_type='text/markdown',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['epibox', 'signal acquisition', 'Raspberry Pi'],
    name='epibox',
    packages=find_packages(include=['epibox', 'epibox.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/anascacais/epibox',
    version='1.0.0',
    zip_safe=False,
)
