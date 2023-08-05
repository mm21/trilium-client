# coding: utf-8

"""
    ETAPI

    External Trilium API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zadam.apps@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr


class LoginRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    password: Optional[StrictStr] = Field(
        None,
        description="user's password used to e.g. login to Trilium server and/or protect notes",
    )
    __properties = ["password"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LoginRequest:
        """Create an instance of LoginRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoginRequest:
        """Create an instance of LoginRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return LoginRequest.parse_obj(obj)

        _obj = LoginRequest.parse_obj({"password": obj.get("password")})
        return _obj
