#!/usr/bin/env python3
"""
Module documented
"""


def update_topics(mongo_collection, name, topics):
    """
    Function documented
    """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    return mongo_collection.update_many(query, update)
