#!/usr/bin/env python
# -*- coding: utf-8 -*-
from settings import client
from faker import Faker
from datetime import datetime
from time import sleep
import argparse

agent = Faker()


def check_positive(value):
    arg = int(value)
    if arg < 0: 
        raise argparse.ArgumentTypeError("{} is invalid. Please, a number positive integer bigger than 0.".format(value))
    return arg


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=check_positive, default=5, help="number of documents write to mongodb.")
    parser.add_argument("-i", "--insert", help="insert documents on mongodb.", action="store_true")
    parser.add_argument("-u", "--update", help="update documents on mongodb.", action="store_true")
    parser.add_argument("-d", "--delete", help="delete documents on mongodb.", action="store_true")
    return parser.parse_args()


def logger(action, _id):
    return print("{time} - {action} {id}.".format(
            time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            action=action,
            id=_id
        ))


def insert_document(collection, number):
    for x in range(number):
        document = agent.profile()
        document["current_location"] = [float(document["current_location"][0]),float(document["current_location"][1])]
        document["birthdate"] = document["birthdate"].strftime("%Y-%m-%d") 
        document["created"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        collection.insert_one(document)
        logger("inserted", document["_id"])


def update_document(collection, number):
    documents = collection.find(limit=number)
    for document in documents:
        collection.update_one({"_id": document["_id"]}, {"$set": {"job": agent.job()}})
        logger("updated", document["_id"])


def delete_document(collection, number):
    documents = collection.find(limit=number)
    for document in documents:
        collection.delete_one({"_id": document["_id"]})
        logger("deleted", document["_id"])


if __name__ == "__main__":
    
    args = read_args()
    
    try:
        collection = client.get_database("changestreams").get_collection("profile")
        # collection = client.changestreams.profile

        if args.insert:
            insert_document(collection=collection, number=args.number)

        if args.update:
            update_document(collection=collection, number=args.number)
            sleep(0.5)
        
        if args.delete:
            delete_document(collection=collection, number=args.number)

    except KeyboardInterrupt:
        print("\n{} - finished by KeyboardInterrupt.".format(
            datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        ))
    except Exception as excpetion:
        print("\n{} - finished by Exception: {}.".format(
            datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            excpetion
        ))
