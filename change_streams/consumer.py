#!/usr/bin/env python
# -*- coding: utf-8 -*-
from settings import client
from datetime import datetime


if __name__ == "__main__":

    stream = client.get_database("changestreams").get_collection("profile").watch(full_document='updateLookup')
    try:
        while stream:
            document = stream.next()
            print("{}\n".format(document))

    except KeyboardInterrupt:
            print("\n{} - finished by KeyboardInterrupt.".format(
                datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            ))
    except Exception as excpetion:
        print("\n{} - finished by Exception: {}.".format(
            datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            excpetion
        ))