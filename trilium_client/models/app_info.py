# coding: utf-8

"""
    ETAPI

    External Trilium API

    The version of the OpenAPI document: 1.0.0
    Contact: zadam.apps@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class AppInfo(BaseModel):
    """
    AppInfo
    """  # noqa: E501

    app_version: Optional[StrictStr] = Field(
        default=None, description="Trilium version", alias="appVersion"
    )
    db_version: Optional[StrictInt] = Field(
        default=None, description="DB version", alias="dbVersion"
    )
    sync_version: Optional[StrictInt] = Field(
        default=None, description="Sync protocol version", alias="syncVersion"
    )
    build_date: Optional[datetime] = Field(
        default=None, description="build date", alias="buildDate"
    )
    build_revision: Optional[StrictStr] = Field(
        default=None, description="git build revision", alias="buildRevision"
    )
    data_directory: Optional[StrictStr] = Field(
        default=None,
        description="data directory where Trilium stores files",
        alias="dataDirectory",
    )
    clipper_protocol_version: Optional[StrictStr] = Field(
        default=None,
        description="version of the supported Trilium Web Clipper protocol",
        alias="clipperProtocolVersion",
    )
    utc_date_time: Optional[StrictStr] = Field(
        default=None, description="current UTC date time", alias="utcDateTime"
    )
    __properties: ClassVar[List[str]] = [
        "appVersion",
        "dbVersion",
        "syncVersion",
        "buildDate",
        "buildRevision",
        "dataDirectory",
        "clipperProtocolVersion",
        "utcDateTime",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AppInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "appVersion": obj.get("appVersion"),
                "dbVersion": obj.get("dbVersion"),
                "syncVersion": obj.get("syncVersion"),
                "buildDate": obj.get("buildDate"),
                "buildRevision": obj.get("buildRevision"),
                "dataDirectory": obj.get("dataDirectory"),
                "clipperProtocolVersion": obj.get("clipperProtocolVersion"),
                "utcDateTime": obj.get("utcDateTime"),
            }
        )
        return _obj
