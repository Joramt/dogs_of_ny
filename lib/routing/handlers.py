import json
import os

import tornado.web
import pandas as pd

from tornado.options import options
from lib.tool.pandas_helper import PandaHelper
from lib.tool.query_helper import QueryHelper


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Everything is up and running ! " +
                   "Now go to the <code>/count</code> endpoint")


class CountHandler(tornado.web.RequestHandler):
    def get(self):

        self.set_header('Content-Type', 'application/json')
        self.content_type = 'application/json'

        # loading CSV and normalizing it to lowercase
        csv_data = pd.read_csv(os.path.join(
                os.path.dirname(__file__), "../../static/dogs_of_ny.csv"
            )).apply(lambda x: x.astype(str).str.lower())

        # CSV columns names are going to be our whitelisted_parameters
        whitelisted_parameters = list(csv_data.columns.values)
        query_parameters_dict = QueryHelper.queryStringToDict(
            self.request.full_url()
            )
        
        unknown_fields = []
        for key, value in query_parameters_dict:
            if key.lower() not in whitelisted_parameters:
                unknown_fields.append(key)

        if unknown_fields:
            self.set_status(400)
            response = {"unknown fields": sorted(unknown_fields)}

        elif not query_parameters_dict:
            self.set_status(200)
            response = {"count": 0}

        else:
            self.set_status(200)
            # transform the query string into a panda-readable condition
            # ie "foo='bar' and baz='foz'" and ...
            conditions = PandaHelper.generateConditionsFromDict(
                query_parameters_dict)
            filtered_data = csv_data.query(conditions)
            count = filtered_data.shape[0]
            response = {"count": count}

        self.write(json.dumps(response))
        self.finish()
