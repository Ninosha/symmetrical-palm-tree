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


# def create_pull(project_id, topic_id):
#     publisher = pubsub_v1.PublisherClient()
#     topic_path = publisher.topic_path(project_id, topic_id)
#     published = publisher.publish(topic_path, data=pub_sub_message)
#     published.result()
#     logging.info("pub/sub push message sent")

def pull_pubsub(project_id, topic_id):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id,
                                                     topic_id)

    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        print(f"Received {message}.")
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path,
                                                 callback=callback)
    return streaming_pull_future.result()

