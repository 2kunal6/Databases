####Introduction
- It is an memory-first key-value Datastore.
- It stores data directly in memory, so it is faster than any disk based DBs.  
- But Redis can also sync the data into disk using append-only files, snapshots and more.
- It is a no-sql DB. So, no joins.
- To access data, we just need the key and the type of data stored.
- Beyond caching it can act as primary DB, session management, do vector searches, streams, probailistic queries, geospatial data, bitmaps, time series, and many other things.
- USP: verstility and speed
- Redis Insight is a visualization tool that helps us look at the DB using GUI, look at key-values, and hopefully to debug when queries are running slow.
- Redis has 2 types of keys:
  - persistent: default, keys stay around until deleted
  - volatile: lives till TTL

####Setup with Docker
- In local machine: docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest

####TODO
- use redis as DB and cache
- use strings, lists, audio files as keys and values
- use incrementing, decrementing numbers, substrings, bitwise ops for keys and values
- hyperloglog, bloom filter
- find my name, color, price range etc.
- use for vector search to find similar products -> create chatbot

####More
- K-V
  - Redis is a giant map of keys and values
  - A value is a piece of data we want to store.  It can be textx, numbers, raw bytes, complex data structures (like hashmaps, lists)
  - Namespaces are used to avoid conflicting names for keys.  Ex: product:1234:color, product:1234:price and they can be viewed hierarchically
- Probabilistic data structure helps us count practically unlimited number of items with great accuracy (not 100% accurate)
- Redis streams are an ordered data structure recording a series of chronological events.