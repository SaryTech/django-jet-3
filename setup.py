import os

from setuptools import find_packages
from setuptools import setup


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        file = open(path, encoding="utf-8")
    except TypeError:
        file = open(path)
    return file.read()


setup(
    name="django-jet",
    version=__import__("jet").VERSION,
    description="Modern template for Django admin interface with improved functionality",
    long_description=read("README.rst"),
    author="Denis Kildishev",
    author_email="support@jet.geex-arts.com",
    url="https://github.com/geex-arts/django-jet",
    packages=find_packages(),
    license="AGPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "License :: Free for non-commercial use",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Environment :: Web Environment",
        "Topic :: Software Development",
        "Topic :: Software Development :: User Interfaces",
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=["Django>=3.2"],
)
