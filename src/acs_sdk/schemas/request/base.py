from pydantic import BaseModel, ConfigDict


class APIRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
