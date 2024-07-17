#!/usr/bin/env python3
"""Inserting a document to a collection"""

def insert_school(mongo_collection, **kwargs):
    """
    This function takes in a pymongo collection 'mongo_collection' and
    key-worded args 'kwargs' as its parameters and inserts a document 'kwargs'
    to the collection
    """

    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
