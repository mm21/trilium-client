# coding: utf-8

# flake8: noqa

"""
    ETAPI

    External Trilium API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zadam.apps@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from trilium_client.api.default_api import DefaultApi

# import ApiClient
from trilium_client.api_client import ApiClient
from trilium_client.configuration import Configuration
from trilium_client.exceptions import OpenApiException
from trilium_client.exceptions import ApiTypeError
from trilium_client.exceptions import ApiValueError
from trilium_client.exceptions import ApiKeyError
from trilium_client.exceptions import ApiAttributeError
from trilium_client.exceptions import ApiException

# import models into sdk package
from trilium_client.models.app_info import AppInfo
from trilium_client.models.attribute import Attribute
from trilium_client.models.branch import Branch
from trilium_client.models.create_note_def import CreateNoteDef
from trilium_client.models.error import Error
from trilium_client.models.login201_response import Login201Response
from trilium_client.models.login_request import LoginRequest
from trilium_client.models.note import Note
from trilium_client.models.note_with_branch import NoteWithBranch
from trilium_client.models.search_response import SearchResponse