from setuptools import setup, find_packages

setup(
    name='devops-mkdocs-issue-showcaser',
    version='0.0.1',
    description='MkDocs plugin for setting showcasing GitHub Issues on the corresponding pages.',
    keywords='mkdocs github issues',
    url='https://github.com/bayer-int/devops-mkdocs-issue-showcaser',
    author='Tim Jonas Meinerzhagen',
    author_email='tim.meinerzhagen@bayer.com',
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=0.17',
        'jinja2',
        'PyGithub',
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'issue-showcaser = mkdocs_issue_showcaser:IssueShowcaserPlugin'
        ]
    }
)
