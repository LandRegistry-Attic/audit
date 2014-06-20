# indifferent

An opinionated means to store changes to Python data (lists, tuples, dicts, etc), see diffs or audit logs, and to roll back.

# Dependencies

datadiff
redis
flask
cPickle

# Model

The model is a basic envelope that contains these items:

    {
      'key' : <str>, 
      'message' : <str>,
      'http_status' : <int>,
      'value' : <str|int|obj|etc> /* OPTIONAL */ 
    }

....where
 - ```key``` is the unique key this audit entry pertains to
 - ```message``` is a custom log message
 - ```http_status``` is an HTTP status code
 - ```value``` (OPTIONAL) is a string, array, object, etc.


# API

    /log  POST  'create a new log entry
    /log/<someKey>  GET 'get the entire audit log for someKey'

# Notes

See from "In [20]" onwards on http://nbviewer.ipython.org/github/bigsnarfdude/bsides_vancouver_2013/blob/master/PickleRedis.ipynb

