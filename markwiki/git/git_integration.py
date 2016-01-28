# Copyright (c) 2016, deadc0de6
'''Versioning of the wiki pages through git'''
from sh import git


class GitIntegration(object):

    GIT_MSG = 'change on page %s'

    def __init__(self, wiki_path):
        self.path = wiki_path
        self.git = git.bake(_cwd=self.path)
        self.git.init()
        self._set_config()
        self.bootstrap()

    def bootstrap(self):
        self._add_untracked()
        self._add_local_change()

    def update_file(self, path):
        '''called on each update of a wiki page'''
        self._commit_file(path)

    def _set_config(self):
        '''handle correctly line ending'''
        self.git.config('--local', 'core.autocrlf', 'input')

    def _add_untracked(self):
        '''add individual commits for each untracked file'''
        for f in self.git('ls-files', '-o').split('\n'):
            if f:
                self._commit_file(f)

    def _add_local_change(self):
        '''commit local changes if any'''
        for f in self.git('ls-files', '-m').split('\n'):
            if f:
                self._commit_file(f)

    def _commit_file(self, path):
        '''commit some change on a wiki page'''
        self.git.add(path)
        msg = self.GIT_MSG % (path)
        self.git.commit('-m', msg)

    def get_changes(self, path):
        '''get list of commits for a specific page'''
        changes = []
        commits = self.git('--no-pager', 'log', '--format=%H,%ai', path)
        for i, commit in enumerate(commits):
            if i == 0:
                continue
            commit = commit.strip('\'').rstrip('\'')
            change = {}
            change['commit'] = commit.split(',')[0]
            change['date'] = commit.split(',')[1]
            changes.append(change)
        return changes

    def view_history(self, path, commit):
        '''view the file as it was at a specific commit'''
        return self.git('--no-pager', 'show', '%s:%s' % (commit, path))

    def revert_file(self, path, commit):
        '''revert a file to a specific commit'''
        self.git.checkout(commit, path)
        self._commit_file(path)
