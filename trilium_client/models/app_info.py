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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr


class AppInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    app_version: Optional[StrictStr] = Field(
        None, alias="appVersion", description="Trilium version"
    )
    db_version: Optional[StrictInt] = Field(
        None, alias="dbVersion", description="DB version"
    )
    sync_version: Optional[StrictInt] = Field(
        None, alias="syncVersion", description="Sync protocol version"
    )
    build_date: Optional[datetime] = Field(
        None, alias="buildDate", description="build date"
    )
    build_revision: Optional[StrictStr] = Field(
        None, alias="buildRevision", description="git build revision"
    )
    data_directory: Optional[StrictStr] = Field(
        None,
        alias="dataDirectory",
        description="data directory where Trilium stores files",
    )
    clipper_protocol_version: Optional[StrictStr] = Field(
        None,
        alias="clipperProtocolVersion",
        description="version of the supported Trilium Web Clipper protocol",
    )
    utc_date_time: Optional[StrictStr] = Field(
        None, alias="utcDateTime", description="current UTC date time"
    )
    __properties = [
        "appVersion",
        "dbVersion",
        "syncVersion",
        "buildDate",
        "buildRevision",
        "dataDirectory",
        "clipperProtocolVersion",
        "utcDateTime",
    ]

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
    def from_json(cls, json_str: str) -> AppInfo:
        """Create an instance of AppInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AppInfo:
        """Create an instance of AppInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AppInfo.parse_obj(obj)

        _obj = AppInfo.parse_obj(
            {
                "app_version": obj.get("appVersion"),
                "db_version": obj.get("dbVersion"),
                "sync_version": obj.get("syncVersion"),
                "build_date": obj.get("buildDate"),
                "build_revision": obj.get("buildRevision"),
                "data_directory": obj.get("dataDirectory"),
                "clipper_protocol_version": obj.get("clipperProtocolVersion"),
                "utc_date_time": obj.get("utcDateTime"),
            }
        )
        return _obj
