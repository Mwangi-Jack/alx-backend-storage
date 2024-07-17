#!/usr/bin/env python3
"""Sorting documents"""


def top_students(mongo_collection):
    """This function takes in a mongo collection object 'mongo_collection;
    and returns a list of all studetns sorted by average score"""

    return mongo_collection.aggregate([
		{
			"$project":
				{
					"name": "$name",
					"averageScore": {"$avg": "$topics.score"}
				}
		},
		{
			"$sort": { "averageScore": -1}
		}
	])
