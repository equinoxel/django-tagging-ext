from setuptools import setup, find_packages

version = '0.3.1'

setup(
    name='django_tagging_ext',
    version=version,
    description="Adds in new features to supplement django-tagging",
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    keywords='django,pinax',
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/django-tagging-ext/tree/master',
    license='MIT',
    packages=find_packages(),
)
