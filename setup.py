from setuptools import find_packages, setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='netbox-licences',
    version='0.1.4-rc1',
    description='Provides licences for netbox',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/Dzordzu/netbox-licences',
    author='Tomasz Durda',
    license='MIT',
    install_requires=[
        'setuptools-git',
        'inflection'
    ],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
      ],
)
