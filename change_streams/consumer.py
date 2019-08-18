#!/usr/bin/env python
# -*- coding: utf-8 -*-
from settings import client
from bson.json_util import dumps


if __name__ == "__main__":

    stream = client.get_database("changestreams").get_collection("profile").watch(full_document='updateLookup')
    while stream:
        document = next(stream)
        print(document)
        # print(dumps(document))
        print('') # for readability only
