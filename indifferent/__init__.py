import os, sys
from flask import Flask

app = Flask(__name__)

# add config
app.config.from_object('config')

if not os.environ.get('REDIS_URL'):
    print "REDIS_URL not set. Using default=[%s]" % app.config['REDIS_URL']

if not os.environ.get('REDIS_NS'):
    print "REDIS_NS not set. Using default=[%s]" % app.config['REDIS_NS']
