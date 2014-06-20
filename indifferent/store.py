from redis import Redis, WatchError
from .kv import KV
from datadiff import diff
import cPickle as pickle
from .util import unixts

class Store(object):

    def __init__(self, config):
        self.redis = Redis.from_url(config['REDIS_URL'])
        self.ns = config['REDIS_NS']

    def __ns(self, k, *kk):
        return ":".join(str(e) for e in [self.ns, k] + list(kk))

    def audit(self, entry):
        """
        Persists the message and code to the audit, and also
        the key/value pair if a value exists.
        """
        ts = unixts()
        self.redis.set(self.__ns(

    def create(self, kv):
        """
        Do a bunch of things in a transaction:
          - bump the version (1 for first version)
          - read the previous version (if it exists)
          - take the diff
          - store the diff
        """
        next_version = -1
        with self.redis.pipeline() as pipe:
            while 1:
                try:
                    # bump the version
                    version_ns = self.__ns('version', kv.key)
                    pipe.watch(version_ns)
                    current_version = pipe.get(version_ns)
                    if current_version:
                        next_version = int(current_version) + 1
                    else:
                        next_version = 1

                    pipe.multi()
                    pipe.set(version_ns, next_version)
                    pipe.set(self.__ns(kv.key, next_version), kv.value)
                    pipe.execute()
                    break
                except WatchError:
                    continue
                finally:
                    pipe.reset()

        # with the new version safely persisted, persist the diff
        previous_value = {}
        if next_version > 1:
            previous_version = next_version - 1
            previous_value = {
                kv.key : self.redis.get(self.__ns(kv.key, previous_version))
            }

        difference = diff(previous_value, kv.as_dict())
        pickled_diff = pickle.dumps(difference)
        self.redis.set(self.__ns('diff', kv.key, next_version), pickled_diff)
        # TODO to save space, old versions can be pruned, and only the diffs kept

    def read(self, key):
        return self.redis.get(self.__ns(key))
