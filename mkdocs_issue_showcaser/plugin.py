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
    issues = dict()

    def __init__(self):
        self.enabled = True

    def on_startup(self, command, dirty):
        self.github_token = environ.get(self.config['env_github_token'])
        self.repo = self.config['repo']
            
        if not self.github_token:
            raise Exception("No GitHub token found in environment variable '{}'".format(self.config['env_github_token']))
        
        g = Github(self.github_token)
        for issue in g.get_repo(self.repo).get_issues():
            title = re.findall('`([^`]*)`', issue.title)
            body = []
            if issue.body:
                body = re.findall('`([^`]*)`', issue.body)

            for file in title + body:
                if file not in self.issues:
                    self.issues[file] = []
                self.issues[file].append(issue)

    def on_page_markdown(self, markdown, page, config, files):
        if page.file.src_uri in self.issues:
            issue_header = "<ul>"
            for issue in self.issues[page.file.src_uri]:
                issue_header =  issue_header + '<li><a href="' + issue.url.replace('api.github.com/repos', 'github.com') + '">#' + str(issue.number) + " " + issue.title + "</a></li>"
            issue_header = issue_header + "</ul>"

            header = '<div class="admonition bug"><p class="admonition-title">Open Issues for this page</p><p>These are currently open issues that affect this document: \n' + issue_header + '</p></div>'

            markdown = header + "\n\n" + markdown
        return markdown
