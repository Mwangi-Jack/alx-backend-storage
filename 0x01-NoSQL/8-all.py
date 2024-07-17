#!/usr/bin/env python3
"""listing all documents in a collection"""


def list_all(mongo_collection):
    """
    This function takes in a pymongo collection object
    'mongo_collection' as a parameter and returns a list of all
    the dcuments in the collection or empty list if not documents found
    """

    if not mongo_collection:
        return []

    documents = mongo_collection.find()

    return [entry for entry in documents]
