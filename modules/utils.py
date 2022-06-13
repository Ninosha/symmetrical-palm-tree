import os
from google.cloud import pubsub_v1


def message(data):
    data = str(data).encode('utf-8')
    return data


def create_push(project_id, topic_id, data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    published = publisher.publish(topic_path, data=data)
    published.result()

#
# project_id = "bitcoindata-352508"
# topic_id = "crimes"
#
# create_push(project_id, topic_id, 234)
