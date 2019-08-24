# PyMongo BEAM Reader

A simple example of how to use the MongoDB Change Streams and Apache Beam MongoDB reader.

## Setup

- docker >= 19.03.1
- docker-compose >= 1.21.0
- virtualenv >= 16.4.3
- python >= 3.7.1
- pip >= 19.0.3
- curl >= 7.47.0

## Deploy

If you like, you can test it out with these commands:

### Create docker images

After you clone this repository and access to folder repository, run:

```bash
    $ docker-compose up
```

### Edit /etc/hosts

Add hostnames `mongo-one`, `mongo-two` and `mongo-three`, run:

```bash
    $ sudo vi /etc/hosts
    > 127.0.0.1     mongo-one
    > 127.0.0.1     mongo-two
    > 127.0.0.1     mongo-three
```

Check if resolves hostnames `mongo-one`, `mongo-two` and `mongo-three`, run:

```bash
    $ curl -X GET localhost:27017
    $ curl -X GET mongo-one:27017
    $ curl -X GET mongo-two:27017
    $ curl -X GET mongo-three:27017
```

All responses, expected: `It looks like you are trying to access MongoDB over HTTP on the native driver port.`

### Initiate MongoDB Replica Set

Access MongoDB shell, run:

```bash
    $ docker exec -it mongo-one mongo
    > rs.initiate({_id: 'beam', members: [
        {_id: 0, host: "mongo-one:27017" },
        {_id: 1, host: "mongo-two:27017" },
        {_id: 2, host: "mongo-three:27017"}]})
    > exit
```

### Python Environment

Create `venv` and install `requirements.txt`, run:

```bash
    $ make install
```

## MongoDB Change Streams

Open terminal, activate venv `$ source venv/bin/activate`, run:

- listen change streams by database `changestreams` on collection `profile`.

```bash
    $ python change_streams/consumer.py
```

Open other terminal, activate venv `$ source venv/bin/activate`, run:

- insert document

```bash
    $ python change_streams/producer.py --insert --number 1
```

- update document

```bash
    $ python change_streams/producer.py --update --number 1
```

- delete document

```bash
    $ python change_streams/producer.py --delete --number 1
```

all options: `$ python change_streams/producer.py --help`.
    
```
usage: producer.py [-h] [-n NUMBER] [-i] [-u] [-d]
```

|    argument   | type | default |   choices   | description                          |
|---------------|------|---------|-------------|--------------------------------------|
| -h, --help    | bool |  False  |     n/a     | show this help message and exit      |
| -i, --insert  | bool |  False  |     n/a     | insert documents on mongodb          |
| -u, --update  | bool |  False  |     n/a     | insert documents on mongodb          |
| -d, --delete  | bool |  False  |     n/a     | insert documents on mongodb          |
| -n, --number  | int  |    5    |   int > 0   | number of documents write to mongodb |

- Also for testing, you can use Mongo Express in browser: `localhost:8081`.

## MongoDB Apache Beam

Open terminal, activate venv `$ source venv/bin/activate`, run:

- read MongoDB with Apache Beam.

```bash
    $ python change_streams/producer.py --insert --number 5000 # write documents before read
    $ python beam_example.py
```

## MonogoDB Document

```JSON
{
    "_id": ObjectID("5d6167818d7bb7a8d3e2757d"),
    "job": "Editor, film/video",
    "company": "Bowman, Haynes and Williams",
    "ssn": "291-81-4054",
    "residence": "861 Sweeney Harbors Apt. 719\nButlerfurt, NY 84300",
    "current_location": [
        77.3373835,
        53.068343
    ],
    "blood_group": "O-",
    "website": [
        "https://fritz.info/",
        "https://austin.biz/",
        "https://smith.org/",
        "https://brooks.com/"
    ],
    "username": "devin39",
    "name": "David Patel",
    "sex": "M",
    "address": "5497 Heather Bypass\nSouth Jenniferland, NH 09256",
    "mail": "janet11@gmail.com",
    "birthdate": "2015-06-04",
    "created": "2019-08-24T16:36:17.969783Z"
}
```

## References:

- https://www.mongodb.com/blog/post/mongodb-change-streams-with-python
- https://docs.mongodb.com/manual/changeStreams/
- https://docs.docker.com/samples/library/mongo/
- https://www.youtube.com/watch?v=eBGC6z1fPs0
- https://gist.github.com/harveyconnor/518e088bad23a273cae6ba7fc4643549
