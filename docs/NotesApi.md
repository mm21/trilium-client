# trilium_client.NotesApi

All URIs are relative to *http://localhost:37740/etapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_note**](NotesApi.md#create_note) | **POST** /create-note | Create a note
[**delete_note_by_id**](NotesApi.md#delete_note_by_id) | **DELETE** /notes/{noteId} | Delete a note
[**export_note_subtree**](NotesApi.md#export_note_subtree) | **GET** /notes/{noteId}/export | Export a subtree
[**get_note_by_id**](NotesApi.md#get_note_by_id) | **GET** /notes/{noteId} | Get a note
[**get_note_content**](NotesApi.md#get_note_content) | **GET** /notes/{noteId}/content | Get the content of a note
[**get_note_history**](NotesApi.md#get_note_history) | **GET** /notes/history | List recent changes
[**import_zip**](NotesApi.md#import_zip) | **POST** /notes/{noteId}/import | Import a ZIP archive
[**patch_note_by_id**](NotesApi.md#patch_note_by_id) | **PATCH** /notes/{noteId} | Update a note
[**put_note_content_by_id**](NotesApi.md#put_note_content_by_id) | **PUT** /notes/{noteId}/content | Replace the content of a note
[**search_notes**](NotesApi.md#search_notes) | **GET** /notes | Search notes
[**undelete_note**](NotesApi.md#undelete_note) | **POST** /notes/{noteId}/undelete | Restore a deleted note


# **create_note**
> NoteWithBranch create_note(create_note_def)

Create a note

Create a note and place it into the note tree

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.create_note_def import CreateNoteDef
from trilium_client.models.note_with_branch import NoteWithBranch
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
    api_instance = trilium_client.NotesApi(api_client)
    create_note_def = trilium_client.CreateNoteDef() # CreateNoteDef | 

    try:
        # Create a note
        api_response = api_instance.create_note(create_note_def)
        print("The response of NotesApi->create_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->create_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_note_def** | [**CreateNoteDef**](CreateNoteDef.md)|  | 

### Return type

[**NoteWithBranch**](NoteWithBranch.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | note created |  -  |
**409** | a note with the given noteId already exists (NOTE_ALREADY_EXISTS) |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note_by_id**
> delete_note_by_id(note_id)

Delete a note

deletes a single note based on the noteId supplied

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

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
    api_instance = trilium_client.NotesApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        # Delete a note
        api_instance.delete_note_by_id(note_id)
    except Exception as e:
        print("Exception when calling NotesApi->delete_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | note deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_note_subtree**
> bytes export_note_subtree(note_id, format=format)

Export a subtree

Exports ZIP file export of a given note subtree. To export whole document, use "root" for noteId. Protected notes are exported as "[protected]", without their content or attachments, even while the protected session is open. The "share" format refuses a subtree that contains a protected note with NOTE_IS_PROTECTED.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

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
    api_instance = trilium_client.NotesApi(api_client)
    note_id = 'note_id_example' # str | 
    format = html # str |  (optional) (default to html)

    try:
        # Export a subtree
        api_response = api_instance.export_note_subtree(note_id, format=format)
        print("The response of NotesApi->export_note_subtree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->export_note_subtree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 
 **format** | **str**|  | [optional] [default to html]

### Return type

**bytes**

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | export ZIP file |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_by_id**
> Note get_note_by_id(note_id)

Get a note

Returns a note identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note import Note
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
    api_instance = trilium_client.NotesApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        # Get a note
        api_response = api_instance.get_note_by_id(note_id)
        print("The response of NotesApi->get_note_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->get_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

[**Note**](Note.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | note response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_content**
> bytes get_note_content(note_id)

Get the content of a note

Returns note content identified by its ID. The response carries the note's MIME type as its `Content-Type`.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

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
    api_instance = trilium_client.NotesApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        # Get the content of a note
        api_response = api_instance.get_note_content(note_id)
        print("The response of NotesApi->get_note_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->get_note_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

**bytes**

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | note content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_history**
> List[RecentChange] get_note_history(ancestor_note_id=ancestor_note_id)

List recent changes

Returns recent changes including note creations, modifications, and deletions

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.recent_change import RecentChange
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
    api_instance = trilium_client.NotesApi(api_client)
    ancestor_note_id = 'ancestor_note_id_example' # str | Limit changes to a subtree identified by this note ID. Defaults to \"root\" (all notes). (optional)

    try:
        # List recent changes
        api_response = api_instance.get_note_history(ancestor_note_id=ancestor_note_id)
        print("The response of NotesApi->get_note_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->get_note_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ancestor_note_id** | **str**| Limit changes to a subtree identified by this note ID. Defaults to \&quot;root\&quot; (all notes). | [optional] 

### Return type

[**List[RecentChange]**](RecentChange.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of recent changes |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_zip**
> NoteWithBranch import_zip(note_id, body)

Import a ZIP archive

Imports ZIP file into a given note.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note_with_branch import NoteWithBranch
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
    api_instance = trilium_client.NotesApi(api_client)
    note_id = 'note_id_example' # str | 
    body = None # bytes | The ZIP file, sent as `application/zip` or `application/octet-stream`; other content types are not accepted. 

    try:
        # Import a ZIP archive
        api_response = api_instance.import_zip(note_id, body)
        print("The response of NotesApi->import_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->import_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 
 **body** | **bytes**| The ZIP file, sent as &#x60;application/zip&#x60; or &#x60;application/octet-stream&#x60;; other content types are not accepted.  | 

### Return type

[**NoteWithBranch**](NoteWithBranch.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/zip, application/octet-stream
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | note created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_note_by_id**
> Note patch_note_by_id(note_id, note)

Update a note

patch a note identified by the noteId with changes in the body

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note import Note
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
    api_instance = trilium_client.NotesApi(api_client)
    note_id = 'note_id_example' # str | 
    note = trilium_client.Note() # Note | 

    try:
        # Update a note
        api_response = api_instance.patch_note_by_id(note_id, note)
        print("The response of NotesApi->patch_note_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->patch_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 
 **note** | [**Note**](Note.md)|  | 

### Return type

[**Note**](Note.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | note updated |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_note_content_by_id**
> put_note_content_by_id(note_id, body)

Replace the content of a note

Updates note content identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

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
    api_instance = trilium_client.NotesApi(api_client)
    note_id = 'note_id_example' # str | 
    body = 'body_example' # str | New content of the note. Send text (such as the HTML of a text note) as `text/plain` and binary data (such as the file of an image or file note) as `application/octet-stream`; other content types are not accepted. 

    try:
        # Replace the content of a note
        api_instance.put_note_content_by_id(note_id, body)
    except Exception as e:
        print("Exception when calling NotesApi->put_note_content_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 
 **body** | **str**| New content of the note. Send text (such as the HTML of a text note) as &#x60;text/plain&#x60; and binary data (such as the file of an image or file note) as &#x60;application/octet-stream&#x60;; other content types are not accepted.  | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: text/plain, application/octet-stream
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | note content updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_notes**
> SearchResponse search_notes(search, fast_search=fast_search, include_archived_notes=include_archived_notes, ancestor_note_id=ancestor_note_id, ancestor_depth=ancestor_depth, order_by=order_by, order_direction=order_direction, limit=limit, debug=debug)

Search notes

Search notes

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.search_response import SearchResponse
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
    api_instance = trilium_client.NotesApi(api_client)
    search = 'towers tolkien' # str | search query string as described in https://triliumnext.github.io/Docs/Wiki/search.html
    fast_search = False # bool | enable fast search (fulltext doesn't look into content) (optional) (default to False)
    include_archived_notes = False # bool | search by default ignores archived notes. Set to 'true' to includes archived notes into search results. (optional) (default to False)
    ancestor_note_id = 'ancestor_note_id_example' # str | search only in a subtree identified by the subtree noteId. By default whole tree is searched. (optional)
    ancestor_depth = 'eq1' # str | define how deep in the tree should the notes be searched (optional)
    order_by = '[\"title\",\"#publicationDate\",\"isProtected\",\"isArchived\",\"dateCreated\",\"dateModified\",\"utcDateCreated\",\"utcDateModified\",\"parentCount\",\"childrenCount\",\"attributeCount\",\"labelCount\",\"ownedLabelCount\",\"relationCount\",\"ownedRelationCount\",\"relationCountIncludingLinks\",\"ownedRelationCountIncludingLinks\",\"targetRelationCount\",\"targetRelationCountIncludingLinks\",\"contentSize\",\"contentAndAttachmentsSize\",\"contentAndAttachmentsAndRevisionsSize\",\"revisionCount\"]' # str | name of the property/label to order search results by (optional)
    order_direction = asc # str | order direction, ascending or descending (optional) (default to asc)
    limit = 10 # int | limit the number of results you want to receive (optional)
    debug = False # bool | set to true to get debug information in the response (search query parsing) (optional) (default to False)

    try:
        # Search notes
        api_response = api_instance.search_notes(search, fast_search=fast_search, include_archived_notes=include_archived_notes, ancestor_note_id=ancestor_note_id, ancestor_depth=ancestor_depth, order_by=order_by, order_direction=order_direction, limit=limit, debug=debug)
        print("The response of NotesApi->search_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->search_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search query string as described in https://triliumnext.github.io/Docs/Wiki/search.html | 
 **fast_search** | **bool**| enable fast search (fulltext doesn&#39;t look into content) | [optional] [default to False]
 **include_archived_notes** | **bool**| search by default ignores archived notes. Set to &#39;true&#39; to includes archived notes into search results. | [optional] [default to False]
 **ancestor_note_id** | **str**| search only in a subtree identified by the subtree noteId. By default whole tree is searched. | [optional] 
 **ancestor_depth** | **str**| define how deep in the tree should the notes be searched | [optional] 
 **order_by** | **str**| name of the property/label to order search results by | [optional] 
 **order_direction** | **str**| order direction, ascending or descending | [optional] [default to asc]
 **limit** | **int**| limit the number of results you want to receive | [optional] 
 **debug** | **bool**| set to true to get debug information in the response (search query parsing) | [optional] [default to False]

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_note**
> UndeleteNote200Response undelete_note(note_id)

Restore a deleted note

Restore a deleted note. The note must be deleted and must have at least one undeleted parent.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.undelete_note200_response import UndeleteNote200Response
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
    api_instance = trilium_client.NotesApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        # Restore a deleted note
        api_response = api_instance.undelete_note(note_id)
        print("The response of NotesApi->undelete_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->undelete_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

[**UndeleteNote200Response**](UndeleteNote200Response.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | note restored successfully |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

