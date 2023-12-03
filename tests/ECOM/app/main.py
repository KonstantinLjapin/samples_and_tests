import uvicorn
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Query, status
from pymongo import MongoClient
from up_load_mongo import get_db


def db_worker(client: MongoClient = get_db()):
    try:
        dbname = client['task_dict']
        collection_name = dbname["users_form"]
        item_details = collection_name.find()
        item = item_details[0]
        return item
    except TypeError as err:
        return False


app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def hello():
    ret = '''<html><body><h2>Hello World!</h2></body></html>'''

    return HTMLResponse(content=ret)


@app.post("/get_form")
async def read_items(f_name1: str = Query(None), f_name2: str = Query(None)):
    if db_worker():
        row: dict = db_worker().get("data")
        get_db().close()
        for form in row:
            if f_name1 in [*form.values()] and f_name2 in [*form.values()]:
                return form
        return {f_name1: "FIELD_TYPE", f_name2: "FIELD_TYPE"}
    return {f_name1: "FIELD_TYPE", f_name2: "FIELD_TYPE"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
