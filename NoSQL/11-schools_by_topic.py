#!/usr/bin/env python3
"""
Module documented
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function documented
    """
    if mongo_collection is None:
        raise ValueError("mongo_collection cannot be None")
    if not isinstance(topic, str):
        raise ValueError("topic must be a string")
    query = {"topics": topic}
    return list(mongo_collection.find(query))
