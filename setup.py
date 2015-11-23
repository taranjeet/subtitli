#!/usr/bin/env python

from setuptools import setup
import sys

setup(
    name='subtitli',
    version='0.0.1',
    description='Downloads the subtitle for a movie',
    long_description=open('README.rst').read(),
    author='Taranjeet Singh',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords="subtitle cli, movie video, subtitle-cli",
    author_email='reachtotj@gmail.com',
    url='https://github.com/staranjeet/subtitli',
    packages=['subtitli'],
    install_requires=[
        'requests==2.7.0',
    ],
    entry_points={
        'console_scripts': [
            'subtitli = subtitli.subtitle:main'
            ],
    }
)
