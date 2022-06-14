import logging

def read(client, table_dataset, table_name):
    """
    function reads table fetched from api request
    :param client: client object
    :param table_dataset: str
    :param table_name: str
    :return: dict
    """
    try:
        query_string = f"""SELECT * FROM {table_dataset}.{table_name}"""

        dataframe = (
            client.query(query_string)
            .result()
            .to_dataframe()
        )
        data = dataframe.head()
        return data.to_dict(orient="records")
    except Exception as e:
        message = {"message": f"error while reading table {e}"}
        logging.info(message)
        return message
