# trilium-client

This is an auto-generated client for [Trilium Notes](https://github.com/zadam/trilium). It builds an API client using the `etapi.openapi.yaml` provided by Trilium.

The generated `trilium_client`, `docs`, and `README.md` artifacts are packaged and many unused files are ignored.

To install, run:

```sh
pip install trilium-client
```

To build, activate a shell: (recommended)

```sh
poetry shell
````

Then run:

```sh
poetry install --with=dev
scons
````

To clean, run:

```sh
scons --clean
````

Following is the README produced by the generator.

# trilium-client
External Trilium API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/zadam/trilium](https://github.com/zadam/trilium)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/mm21/trilium-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/mm21/trilium-client.git`)

Then import the package:
```python
import trilium_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import trilium_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)


# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    backup_name = 'backup_name_example' # str | If the backupName is e.g. \"now\", then the backup will be written to \"backup-now.db\" file

    try:
        api_instance.create_backup(backup_name)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_backup: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:37740/etapi*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**create_backup**](docs/DefaultApi.md#create_backup) | **PUT** /backup/{backupName} | 
*DefaultApi* | [**create_note**](docs/DefaultApi.md#create_note) | **POST** /create-note | 
*DefaultApi* | [**create_revision**](docs/DefaultApi.md#create_revision) | **POST** /notes/{noteId}/revision | 
*DefaultApi* | [**delete_attribute_by_id**](docs/DefaultApi.md#delete_attribute_by_id) | **DELETE** /attributes/{attributeId} | 
*DefaultApi* | [**delete_branch_by_id**](docs/DefaultApi.md#delete_branch_by_id) | **DELETE** /branches/{branchId} | 
*DefaultApi* | [**delete_note_by_id**](docs/DefaultApi.md#delete_note_by_id) | **DELETE** /notes/{noteId} | 
*DefaultApi* | [**export_note_subtree**](docs/DefaultApi.md#export_note_subtree) | **GET** /notes/{noteId}/export | 
*DefaultApi* | [**get_app_info**](docs/DefaultApi.md#get_app_info) | **GET** /app-info | 
*DefaultApi* | [**get_attribute_by_id**](docs/DefaultApi.md#get_attribute_by_id) | **GET** /attributes/{attributeId} | 
*DefaultApi* | [**get_branch_by_id**](docs/DefaultApi.md#get_branch_by_id) | **GET** /branches/{branchId} | 
*DefaultApi* | [**get_day_note**](docs/DefaultApi.md#get_day_note) | **GET** /calendar/days/{date} | 
*DefaultApi* | [**get_inbox_note**](docs/DefaultApi.md#get_inbox_note) | **GET** /inbox/{date} | 
*DefaultApi* | [**get_month_note**](docs/DefaultApi.md#get_month_note) | **GET** /calendar/months/{month} | 
*DefaultApi* | [**get_note_by_id**](docs/DefaultApi.md#get_note_by_id) | **GET** /notes/{noteId} | 
*DefaultApi* | [**get_note_content**](docs/DefaultApi.md#get_note_content) | **GET** /notes/{noteId}/content | 
*DefaultApi* | [**get_week_note**](docs/DefaultApi.md#get_week_note) | **GET** /calendar/weeks/{date} | 
*DefaultApi* | [**get_year_note**](docs/DefaultApi.md#get_year_note) | **GET** /calendar/years/{year} | 
*DefaultApi* | [**import_zip**](docs/DefaultApi.md#import_zip) | **POST** /notes/{noteId}/import | 
*DefaultApi* | [**login**](docs/DefaultApi.md#login) | **POST** /auth/login | 
*DefaultApi* | [**logout**](docs/DefaultApi.md#logout) | **POST** /auth/logout | 
*DefaultApi* | [**patch_attribute_by_id**](docs/DefaultApi.md#patch_attribute_by_id) | **PATCH** /attributes/{attributeId} | 
*DefaultApi* | [**patch_branch_by_id**](docs/DefaultApi.md#patch_branch_by_id) | **PATCH** /branches/{branchId} | 
*DefaultApi* | [**patch_note_by_id**](docs/DefaultApi.md#patch_note_by_id) | **PATCH** /notes/{noteId} | 
*DefaultApi* | [**post_attribute**](docs/DefaultApi.md#post_attribute) | **POST** /attributes | 
*DefaultApi* | [**post_branch**](docs/DefaultApi.md#post_branch) | **POST** /branches | 
*DefaultApi* | [**post_refresh_note_ordering**](docs/DefaultApi.md#post_refresh_note_ordering) | **POST** /refresh-note-ordering/{parentNoteId} | 
*DefaultApi* | [**put_note_content_by_id**](docs/DefaultApi.md#put_note_content_by_id) | **PUT** /notes/{noteId}/content | 
*DefaultApi* | [**search_notes**](docs/DefaultApi.md#search_notes) | **GET** /notes | 


## Documentation For Models

 - [AppInfo](docs/AppInfo.md)
 - [Attribute](docs/Attribute.md)
 - [Branch](docs/Branch.md)
 - [CreateNoteDef](docs/CreateNoteDef.md)
 - [Error](docs/Error.md)
 - [Login201Response](docs/Login201Response.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [Note](docs/Note.md)
 - [NoteWithBranch](docs/NoteWithBranch.md)
 - [SearchResponse](docs/SearchResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="EtapiTokenAuth"></a>
### EtapiTokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="EtapiBasicAuth"></a>
### EtapiBasicAuth

- **Type**: HTTP basic authentication


## Author

zadam.apps@gmail.com


