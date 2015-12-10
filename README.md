# mongo_cache
A simple python cache library backed by mongodb. 

#Installation
Not yet on Pypi, can be installed by dragging the `mongo_cache.py` file into your project.

#Usage
At this point the best documentation is the code or the test for advanced uses.

## Initialization
`cache = MongoCache(mongo_db = MongoClient().cache_database, size=0, cache_collection="cache_collection")`

`size` isnt implemented as of now.

## Get/Set
```
cache.get("test") # => None
cache.set("test", 42) 
cache.get("test") # => 42

cache.get("test2", lambda: 42) # => 42
```
Both `get` and `set` methods accept `expires_in` and `expires_at` keyword arguements. These apply only if the value is being set, and are both in seconds, `expires_in` being the seconds from the current moment, while `expires_at` is a unix time in the future.
