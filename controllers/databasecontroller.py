#! /usr/bin/env python3
# coding: utf-8

from tinydb import TinyDB, Query

db = TinyDB('db.json')

db.insert({"type": "apple", "count": 7})
db.insert({"type": "peach", "count": 3})