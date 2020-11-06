from botocore.vendored import requests
import json
import boto3
import hashlib
import base64
import logging
import threading
import uuid
import os

ddb = boto3.client('dynamodb')

def timeout(event, context):
    raise Exception('Execution is about to time out, exiting...')
    
def store_deidentified_message(message, entity_map, ddb_table):
    hashed_message = hashlib.sha3_256(message.encode()).hexdigest()
    for entity_hash in entity_map:
        ddb.put_item(
            TableName=ddb_table,
            Item={
                'MessageHash': {
                    'S': hashed_message
                },
                'EntityHash': {
                    'S': entity_hash
                },
                'Entity': {
                    'S': entity_map[entity_hash]
                }
            }
        )
    return hashed_message
    
def deidentify_entities_in_message(message, entity_list):
    entity_map = dict()
    for entity in entity_list:
      salted_entity = entity['Text'] + str(uuid.uuid4())
      hashkey = hashlib.sha3_256(salted_entity.encode()).hexdigest()
      entity_map[hashkey] = entity['Text']
      message = message.replace(entity['Text'], hashkey)
    return message, entity_map
    
def handler(event, context):
    # Add in context for Lambda to exit if needed
    timer = threading.Timer((context.get_remaining_time_in_millis() / 1000.00) - 1, timeout, args=[event, context])
    timer.start()
    print ('Received message payload')
    try:
        # Extract the entities and message from the event
        message = event['body']['message']
        entity_list = event['body']['entities']
        # Mask entities
        deidentified_message, entity_map = deidentify_entities_in_message(message, entity_list)
        hashed_message = store_deidentified_message(deidentified_message, entity_map, os.environ['EntityMap'])
        return {
            "deid_message": deidentified_message, 
            "hashed_message": hashed_message
        }
    except Exception as e:
      logging.error('Exception: %s. Unable to extract entities from message' % e)
      raise e