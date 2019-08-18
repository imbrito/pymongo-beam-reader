#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple example of how to use the Apache Beam MongoDB reader.
If you like, you can test it out with these commands:
    $ docker-compose up
    $ make install
    $ python change_streams/producer.py -d 5000
    $ python beam_example.py
"""
import logging

import apache_beam as beam
from bson.json_util import dumps


def transform(document):
    return dumps(document)


def run():
    logging.basicConfig(level=logging.DEBUG)
    connection_string = 'mongodb://root:example@127.0.0.1:27017'

    with beam.Pipeline(runner='DirectRunner') as pipeline:
        (pipeline
         | 'read' >> beam.io.mongodbio.ReadFromMongoDB(connection_string, 'changestreams', 'profile')
         | 'transform' >> beam.Map(transform)
         | 'FixedWindow to 5m' >> beam.WindowInto(beam.window.FixedWindows(5))
         | 'save' >> beam.io.WriteToText(file_path_prefix="documents/output",file_name_suffix=".json",num_shards=1))


if __name__ == '__main__':
    run()