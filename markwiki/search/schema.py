# Copyright (c) 2013, Matt Layman and contributors

from whoosh import fields


class WikiSchema(fields.SchemaClass):
    '''This describes the content that will be stored in the search index.'''

    # The field boost helps wiki page paths show more prevalently in results
    # since they will also be used as links in the conten of other pages.
    path = fields.TEXT(field_boost=2.0, stored=True)
    content = fields.TEXT
