#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

URI = "mongodb://mongo-one:27017,mongo-two:27017,mongo-three:27017/?replicaSet=beam"

client = MongoClient(URI)