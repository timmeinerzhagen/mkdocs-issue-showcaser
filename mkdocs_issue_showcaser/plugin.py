import re
from os import environ
from datetime import datetime

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

from github import Github


class IssueShowcaserPlugin(BasePlugin):
    config_scheme = (
        ('env_github_token', config_options.Type(str, default="GITHUB_TOKEN")),
        ('repo', config_options.Type(str)),
    )

    def __init__(self):
        self.enabled = True

    def on_startup(self, config):
        self.github_token = environ.get(self.config['env_github_token'])
        self.repo = self.config['repo']
            
        if not self.github_token:
            raise Exception("No GitHub token found in environment variable '{}'".format(self.config['env_github_token']))
        
        g = Github(self.github_token)
        for issue in g.get_repo(self.repo).get_issues():
            print(issue)
            print(re.findall('`([^"]*)`', issue.title))
            print(re.findall('`([^"]*)`', issue.body))

    def on_page_markdown(self, markdown, page, config, files):

        return markdown
