#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

URI = "mongodb://root:example@127.0.0.1:27017"

client = MongoClient(URI)