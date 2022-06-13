def read(client, table_dataset, table_name):

    query_string = f"""SELECT * FROM {table_dataset}.{table_name}"""

    dataframe = (
        client.query(query_string)
        .result()
        .to_dataframe()
    )
    data = dataframe.head()

    return data.to_dict(orient="records")
