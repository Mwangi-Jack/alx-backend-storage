#!/usr/bin/env python3
"""Filtering a collection"""

def schools_by_topic(mongo_collection, topic):
    """This function takes in a pymongo collection 'mongo_collection'
     and a string to search 'topic' and returns a list of collections that
     match the search
     """

    return mongo_collection.find({"topics":  {"$in": [topic]}})
