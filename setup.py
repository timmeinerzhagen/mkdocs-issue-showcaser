from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mkdocs-issue-showcaser',
    version='0.1.1',
    description='MkDocs plugin for setting showcasing GitHub Issues on the corresponding pages.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='mkdocs github issues',
    url='https://github.com/timmeinerzhagen/mkdocs-issue-showcaser',
    author='Tim Jonas Meinerzhagen',
    author_email='tim@meinerzhagen.me',
    license='MIT',
    license_files = ('LICENSE'),
    classifiers=[
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        "License :: OSI Approved :: MIT License",
        'Topic :: Documentation',
        'Topic :: Text Processing',
    ],
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=0.17',
        'jinja2',
        'PyGithub',
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'issue-showcaser = mkdocs_issue_showcaser.plugin:IssueShowcaserPlugin'
        ]
    }
)
