#!/usr/bin/env python3
"""
Module documented
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function documented
    """
    return mongo_collection.insert_one(kwargs).inserted_id
