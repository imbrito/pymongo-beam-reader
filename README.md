# PyMongo BEAM Reader

A simple example of how to use the Apache Beam MongoDB reader.

## Setup

- docker >= 19.03.1
- docker-compose >= 1.21.0
- virtualenv >= 16.4.3
- python >= 3.7.1
- pip >= 19.0.3

## Deploy

If you like, you can test it out with these commands:

```bash
    $ docker-compose up
    $ make install
    $ python change_streams/producer.py -d 5000
    $ python beam_example.py
```

## MonogoDB Document

```JSON
{   
    "job": "Loss adjuster, chartered",
    "company": "Miller, Green and White", 
    "ssn": "874-24-2926", 
    "residence": "7580 Morris Flat Apt. 158\nNorth George, WI 42409", 
    "current_location": [-59.7897495, -0.973508], 
    "blood_group": "B+", 
    "website": ["https://snyder-lopez.com/", "http://bright-green.com/", "https://bray-espinoza.com/"], 
    "username": "glassjoshua", 
    "name": "Donald Campbell", 
    "sex": "M", 
    "address": "158 Green Manors\nNorth Patricialand, AZ 28429", 
    "mail": "james54@hotmail.com", 
    "birthdate": "1928-05-09",
    "created": "2019-08-18T16:35:01.693389Z", 
    "_id": ObjectId("5d597e358c48dfe74e9db7e4")
}
```

## Change Streams: consumer

- TODO
- required ReplicaSet

## Referências:

- https://www.mongodb.com/blog/post/mongodb-change-streams-with-python
- https://docs.mongodb.com/manual/changeStreams/
- https://docs.docker.com/samples/library/mongo/
- https://www.youtube.com/watch?v=eBGC6z1fPs0
