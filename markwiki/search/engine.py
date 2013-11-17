# Copyright (c) 2013, Matt Layman and contributors

import os

from whoosh import index

from markwiki.search.schema import WikiSchema


class SearchEngine(object):
    '''The engine is the interface to the search related functionality.'''

    def __init__(self, markwiki_home):
        self.index_dir = os.path.join(markwiki_home, 'search')
        # Whoosh convention prefers 'ix' for index.
        self._ix = None

    def create_index(self, wiki_path):
        '''Create the search index and populate with initial wiki content.'''
        if not os.path.exists(self.index_dir):
            os.mkdir(self.index_dir)

        print(' * Creating the search index ...')
        self._ix = index.create_in(self.index_dir, WikiSchema)
        self._populate_index(wiki_path)

    def open_index(self):
        '''Open the search index.'''
        # The index may already be open from a create_index call.
        if self._ix is None:
            self._ix = index.open_dir(self.index_dir)

    def add_wiki(self, path, content):
        '''Add and index a wiki page.'''
        with self._ix.writer() as writer:
            writer.add_document(path=unicode(path), content=unicode(content))

    def update_wiki(self, path, content):
        '''Update an existing wiki in the index.'''
        # TODO: implement

    def delete_wiki(self, path, content):
        '''Delete a wiki from the index.'''
        # TODO: implement

    def _populate_index(self, wiki_path):
        '''Populate the search index with the initial content of the wiki.'''
        # A wiki page path is relative to the primary wiki path so a certain
        # number of parts should be ignored when creating the page path.
        segments = len(wiki_path.split(os.sep))

        for root, _, files in os.walk(wiki_path):
            for file_ in files:
                # Be sure to only work with Markdown files.
                if not file_.endswith('.md'):
                    continue

                abs_path = os.path.join(root, file_)
                # Trim off the wiki_path from the abs_path to get page_path.
                page_path = os.sep.join(abs_path.split(os.sep)[segments:])
                # Now trim the extension.
                page_path = page_path[:-3]
                content = self._get_markdown_content(abs_path)
                self.add_wiki(page_path, content)

    def _get_markdown_content(self, markdown_path):
        '''Read all the content out of a Markdown file.'''
        with open(markdown_path, 'r') as f:
            content = f.read()

        return content
