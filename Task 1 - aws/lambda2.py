from botocore.vendored import requests
import json
import boto3
import logging
import threading
import sys

def timeout(event, context):
  raise Exception('Execution is about to time out, exiting...')

def mask_entities_in_message(message, entity_list):
  for entity in entity_list:
      message = message.replace(entity['Text'], '#' * len(entity['Text']))
  return message

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
      masked_message = mask_entities_in_message(message, entity_list)
      print (masked_message)
      return masked_message
  except Exception as e:
      logging.error('Exception: %s. Unable to extract entities from message' % e)
      raise e