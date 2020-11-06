

from botocore.vendored import requests
import json
import boto3
import logging
import threading
client = boto3.client(service_name='comprehendmedical')

def timeout(event, context):
    raise Exception('Execution is about to time out, exiting...')

def extract_entities_from_message(message):
    return client.detect_phi(Text=message)

def handler(event, context):
    # Add in context for Lambda to exit if needed
    timer = threading.Timer((context.get_remaining_time_in_millis() / 1000.00) - 1, timeout, args=[event, context])
    timer.start()
    print ('Received message payload. Will extract PII')
    try:
        # Extract the message from the event
        message = event['body']['message']
        # Extract all entities from the message
        entities_response = extract_entities_from_message(message)
        entity_list = entities_response['Entities']
        print ('PII entity extraction completed')
        return entity_list
    except Exception as e:
        logging.error('Exception: %s. Unable to extract PII entities from message' % e)
        raise e