from flask import Flask, request, jsonify
from flask.ext.restful import Resource, Api, reqparse
import gensim
from gensim import utils, matutils
from numpy import exp, dot, zeros, outer, random, dtype, get_include, float32 as REAL,\
     uint32, seterr, array, uint8, vstack, argsort, fromstring, sqrt, newaxis, ndarray, empty, sum as np_sum
import cPickle
import argparse
import base64
import sys

parser = reqparse.RequestParser()


def filter_words(words):
    if words is None:
        return
    return [word for word in words if word in model.vocab]


class show_topics(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('number', type=int, required=True, help="Number of results.")
        args = parser.parse_args()
        return model.show_topic(args['number'])


class print_topics(Resource):
    def get(self):
        parser = reqparse.RequestParser()
		parser.add_argument('number', type=int, required=True, help="Number of results.")
        args = parser.parse_args()
        return model.print_topics(args['number'])


class topic(Resource):
    def get(self):
        parser = reqparse.RequestParser()
		parser.add_argument('sentence', type=str, required=True, help="", action='append')
		query = args['sentence'].split()
        bow = model.id2word.doc2bow(query)
        topic_analysis = model[bow]
        args = parser.parse_args()
        return topic_analysis
        



app = Flask(__name__)
api = Api(app)

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

@app.errorhandler(500)
def raiseError(error):
    return error

if __name__ == '__main__':
    global model

    #----------- Parsing Arguments ---------------
    p = argparse.ArgumentParser()
    p.add_argument("--model", help="Path to the trained model")
   
    p.add_argument("--host", help="Host name (default: localhost)")
    p.add_argument("--port", help="Port (default: 5000)")
    p.add_argument("--path", help="Path (default: /lda)")
    args = p.parse_args()

    model_path = args.model if args.model else "./model.bin.gz"
    
    host = args.host if args.host else "localhost"
    path = args.path if args.path else "/lda"
    port = int(args.port) if args.port else 5000
    if not args.model:
        print "Usage: lda-apy.py --model path/to/the/model [--host host --port 1234]"
    model = gensim.models.LdaModel.load(model_path)
    api.add_resource(show_topics, path+'/show_topics')
    api.add_resource(print_topics, path+'/print_topics')
    api.add_resource(topic, path+'/topic')
    
    app.run(host=host, port=port)
