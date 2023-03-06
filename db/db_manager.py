import json

class MongoManage:

    posts = []
    topics = []
    num_topics = 0
    def __init__(self):
        print('init')

    # async def get_data(self, collection, filter_query, filter_fields):
    #     current_filter_fields = {"_id": 0}
    #     current_filter_fields |= filter_fields
    #     cursor = collection.find(filter_query, current_filter_fields)
    #     return (doc async for doc in cursor)

    # async def write_data(self, collection, data):
    #     if isinstance(data, list):
    #         collection.insert_many(data)
    #     else:
    #         collection.insert_one(data)

    # async def get_topics(self, *args):
    #     return await self.get_data(self.topic_collection, *args)

    async def write_topics(self, *args):
        self.num_topics += 1
        self.topics.append(*args)
        # await self.write_data(self.topic_collection, *args)

    # async def get_posts(self, *args):
    #     return await self.get_data(self.posts_collection, *args)

    async def write_posts(self, *args):
        self.posts += args
        # await self.write_data(self.posts_collection, *args)

    async def close(self):
        print("closing")
        # self.client.close()

    def writefiles(self):
        print('writing', self.num_topics, "topics")
        
        with open('topics.json', 'w') as f:
            json.dump(self.topics, f)
        with open('posts.json', 'w') as f:
            json.dump(self.posts, f)