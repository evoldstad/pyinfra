# pyinfra
# File: pyinfra/facts/git.py
# Desc: local git repo facts

from pyinfra.api.facts import FactBase


class GitBranch(FactBase):
    @classmethod
    def command(cls, name):
        return 'cd {0} && git rev-parse --abbrev-ref HEAD'.format(name)
