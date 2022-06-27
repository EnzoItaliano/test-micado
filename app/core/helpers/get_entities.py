from motor.motor_asyncio import AsyncIOMotorCursor


async def get_entities(cursor: AsyncIOMotorCursor):
    response_entities = []
    for item in await cursor.to_list(None):
        response_entity = {}
        for key in item.keys():
            if key == "_id":
                response_entity["id"] = str(item[key])
            else:
                response_entity[key] = item[key]
        response_entities.append(response_entity)
    return response_entities
