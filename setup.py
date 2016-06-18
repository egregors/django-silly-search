from distutils.core import setup

from setuptools import find_packages
from silly_search import __version__

setup(
    name='django-silly-search',
    version='.'.join(str(x) for x in __version__),
    packages=find_packages(),
    install_requires=[
        "django>=1.8",
    ],
    url='https://github.com/Egregors/django-silly-search',
    download_url='https://github.com/Egregors/django-silly-search/tarball/master',
    license="BSD",
    keywords='django',
    author='Vadim Iskuchekov',
    author_email='egregors@yandex.ru',
    description='Really simple django-app for search by Q-expressions',
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Framework :: Django",
    ],
)
