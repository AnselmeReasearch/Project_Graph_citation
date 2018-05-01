
#!/usr/bin/python3
# coding:UTF8
#---------Library-------------------------#
from setuptools import setup
#-----------------------------------------#

with open ("README.md", "r") as fileR :
    description_library  = fileR.read()


setup (
    name = "Project_Graph_Citation",
    version = "1.0",
    description = "graph citation Pubmed tools",
    license='MIT',
    long_description = description_library,
    url = "https://github.com/HansCeril/Project_Graph_citation",
    author_email = "hans-ceril@hotmail.fr",
    keywords='PubMed Graph Citation',
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
     ],
    install_requires = ["setuptools","pickle", "time", "sys", "os", "networkx", "xml"],
    package_data = {
        '': ['*.vcf', '*.gz', '*.tbi'],
        },



)


