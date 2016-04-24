from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-silly-search',
    version='0.1',
    packages=find_packages(),
    requires=['django (>= 1.3)'],
    url='https://github.com/Egregors/django-silly-search',
    download_url='https://github.com/Egregors/django-silly-search/tarball/master',
    license='Apache License',
    keywords='django',
    author='egregors',
    author_email='egregors@yandex.ru',
    description='Really simple django-app for search by Q-expressions',
    long_description=open('README.md').read(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)
