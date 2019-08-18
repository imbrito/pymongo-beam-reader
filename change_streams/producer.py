#!/usr/bin/env python
# -*- coding: utf-8 -*-
from settings import client
from faker import Faker
from datetime import datetime
import argparse


def check_positive(value):
    arg = int(value)
    if arg < 0: 
        raise argparse.ArgumentTypeError("{} is invalid. Please, a number positive integer bigger than 0.".format(value))
    return arg


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--documents", type=check_positive, default=5, help="number of documents write to mongodb.")
    return parser.parse_args()


if __name__ == "__main__":
    args = read_args()
    agent = Faker()
    collection = client.get_database("changestreams").get_collection("profile")
    for x in range(args.documents):
        try:
            profile = agent.profile()
            profile["current_location"] = [float(profile["current_location"][0]),float(profile["current_location"][1])]
            profile["birthdate"] = profile["birthdate"].strftime("%Y-%m-%d") 
            profile["created"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            collection.insert_one(profile)
            # client.changestreams.profile.insert_one(profile)
            print("{}: {}.".format(
                datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                profile
            ))
        except KeyboardInterrupt:
            print("\n{}: finished by KeyboardInterrupt.".format(
                datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            ))
            break
