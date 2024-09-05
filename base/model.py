from pydantic import BaseModel, field_validator


class ModelCard(BaseModel):
    number: str
    balance: int

    @field_validator("number")
    def prov_numb(cls, value):
        if value == "" or value is None:
           raise Exception("error")
        else:
            return value

