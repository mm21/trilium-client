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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from trilium_client.models.note import Note


class SearchResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    results: List[Note] = ...
    debug_info: Optional[Dict[str, Any]] = Field(
        None,
        alias="debugInfo",
        description="debugging info on parsing the search query enabled with &debug=true parameter",
    )
    __properties = ["results", "debugInfo"]

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
    def from_json(cls, json_str: str) -> SearchResponse:
        """Create an instance of SearchResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict["results"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchResponse:
        """Create an instance of SearchResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SearchResponse.parse_obj(obj)

        _obj = SearchResponse.parse_obj(
            {
                "results": [
                    Note.from_dict(_item) for _item in obj.get("results")
                ]
                if obj.get("results") is not None
                else None,
                "debug_info": obj.get("debugInfo"),
            }
        )
        return _obj
