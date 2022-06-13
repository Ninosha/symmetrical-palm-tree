import logging
from google.cloud import pubsub_v1


def message(data):
    """
    converts bytes to str
    :param data: bytes
    :return: str
    """
    data = str(data).encode('utf-8')
    return data


def create_push(project_id, topic_id, data):
    """
    creates push to pub sub with required data
    :param project_id: str
    :param topic_id: str
    :param data: dict
    :return:
    """
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    published = publisher.publish(topic_path, data=data)
    published.result()
    logging.info("pub/sub push message sent")
