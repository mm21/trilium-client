# trilium_client.RevisionsApi

All URIs are relative to *http://localhost:37740/etapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_revision**](RevisionsApi.md#create_revision) | **POST** /notes/{noteId}/revision | Create a revision
[**get_note_revisions**](RevisionsApi.md#get_note_revisions) | **GET** /notes/{noteId}/revisions | List the revisions of a note
[**get_revision_by_id**](RevisionsApi.md#get_revision_by_id) | **GET** /revisions/{revisionId} | Get a revision
[**get_revision_content**](RevisionsApi.md#get_revision_content) | **GET** /revisions/{revisionId}/content | Get the content of a revision


# **create_revision**
> create_revision(note_id, format=format)

Create a revision

Create a note revision for the given note

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
    api_instance = trilium_client.RevisionsApi(api_client)
    note_id = 'note_id_example' # str | 
    format = html # str |  (optional) (default to html)

    try:
        # Create a revision
        api_instance.create_revision(note_id, format=format)
    except Exception as e:
        print("Exception when calling RevisionsApi->create_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 
 **format** | **str**|  | [optional] [default to html]

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
**204** | revision has been created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_revisions**
> List[Revision] get_note_revisions(note_id)

List the revisions of a note

Returns the revisions of a note identified by its ID. Protected revisions are
omitted, since they cannot be read through ETAPI individually either.


### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.revision import Revision
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
    api_instance = trilium_client.RevisionsApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        # List the revisions of a note
        api_response = api_instance.get_note_revisions(note_id)
        print("The response of RevisionsApi->get_note_revisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RevisionsApi->get_note_revisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

[**List[Revision]**](Revision.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of revisions |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_revision_by_id**
> Revision get_revision_by_id(revision_id)

Get a revision

Returns a revision identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.revision import Revision
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
    api_instance = trilium_client.RevisionsApi(api_client)
    revision_id = 'revision_id_example' # str | 

    try:
        # Get a revision
        api_response = api_instance.get_revision_by_id(revision_id)
        print("The response of RevisionsApi->get_revision_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RevisionsApi->get_revision_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revision_id** | **str**|  | 

### Return type

[**Revision**](Revision.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | revision response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_revision_content**
> str get_revision_content(revision_id)

Get the content of a revision

Returns revision content identified by its ID

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
    api_instance = trilium_client.RevisionsApi(api_client)
    revision_id = 'revision_id_example' # str | 

    try:
        # Get the content of a revision
        api_response = api_instance.get_revision_content(revision_id)
        print("The response of RevisionsApi->get_revision_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RevisionsApi->get_revision_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revision_id** | **str**|  | 

### Return type

**str**

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | revision content response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

