import os
import uvicorn
import logging
from fastapi import FastAPI
from modules.read import read
from google.cloud import bigquery
from modules.utils import message, create_push


TOPIC_ID = os.getenv("TOPIC_ID")
TABLE_DATASET = os.getenv("TABLE_DATASET")
VIEWS_DATASET = os.getenv("VIEWS_DATASET")

app = FastAPI()

client = bigquery.Client()
project_id = client.project


@app.get("/data")
def read_data(table_name: str):
    data = read(client, TABLE_DATASET, table_name)
    logging.info(f"table {table_name} is read")
    return {"data": data}


@app.post("/data")
def insert_rows(table_name: str, rows: dict or list):
    req_type = "post"
    data = message({"request_type": req_type, "table_name": table_name,
                    "rows": rows})
    create_push(project_id, TOPIC_ID, data)
    logging.info(f"insert rows request send on table {table_name}")
    return {"client_host": [table_name, rows]}


@app.put("/data")
def update_row(table_name: str, column_name: str, value: str or int):
    req_type = "put"
    data = message({"request_type": req_type, "table_name": table_name,
                    "column_name": column_name,
                    "value": value})
    create_push(project_id, TOPIC_ID, data)
    logging.info(f"update rows request send on table {table_name}")
    return "success"


@app.delete("/data")
def delete_row(table_name: str, column_name: str, value: str or int):
    req_type = "delete"
    data = message({"request_type": req_type, "table_name": table_name,
                    "column_name": column_name,
                    "value": value})
    create_push(project_id, TOPIC_ID, data)
    logging.info(f"delete rows request send on table {table_name}")
    return "item"


@app.get("/views")
def read_views(table_name: str):
    data = read(client, VIEWS_DATASET, table_name)
    logging.info(f"view table {table_name} is read")
    return {"data": data}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)



# TOPIC_ID
#
# crimes
#
# TABLE_DATASET
#
# bitcoindata-352508.crimes_dataset
#
# VIEWS_DATASET
#
# bitcoindata-352508.views
#
