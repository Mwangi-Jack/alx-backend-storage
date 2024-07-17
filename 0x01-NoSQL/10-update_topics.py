#!/usr/bin/env python3
"""Updating matching documents"""


def update_topics(mongo_collection, name, topics):
    """This function takes in  a mongo collection object 'mongo_collectioin'
    a string 'name' and a list of strings 'topics' as parameters and
    updates all documents  with 'name' """

    return mongo_collection.update_many({"name": name}, {
        "$set": {
			"topics": topics
		}
        })
