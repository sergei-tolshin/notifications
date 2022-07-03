import orjson
from pydantic import BaseModel as PydanticModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class OrjsonMixin(PydanticModel):

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
