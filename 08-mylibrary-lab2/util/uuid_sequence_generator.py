import uuid

def uuid_sequence_genrator():
    while True:
        yield str(uuid.uuid1())
