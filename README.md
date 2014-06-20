# indifferent

An opinionated means to store changes to Python data (lists, tuples, dicts, etc), see diffs or audit logs, and to roll back.

# Dependencies

datadiff
redis
flask
cPickle

# Model

    { key : value }

# API

    /audit
    /diff

# Notes

See from "In [20]" onwards on http://nbviewer.ipython.org/github/bigsnarfdude/bsides_vancouver_2013/blob/master/PickleRedis.ipynb
