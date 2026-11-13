# trilium_client.AttachmentsApi

All URIs are relative to *http://localhost:37740/etapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachment_by_id**](AttachmentsApi.md#delete_attachment_by_id) | **DELETE** /attachments/{attachmentId} | Delete an attachment
[**get_attachment_by_id**](AttachmentsApi.md#get_attachment_by_id) | **GET** /attachments/{attachmentId} | Get an attachment
[**get_attachment_content**](AttachmentsApi.md#get_attachment_content) | **GET** /attachments/{attachmentId}/content | Get the content of an attachment
[**get_note_attachments**](AttachmentsApi.md#get_note_attachments) | **GET** /notes/{noteId}/attachments | List the attachments of a note
[**patch_attachment_by_id**](AttachmentsApi.md#patch_attachment_by_id) | **PATCH** /attachments/{attachmentId} | Update an attachment
[**post_attachment**](AttachmentsApi.md#post_attachment) | **POST** /attachments | Create an attachment
[**put_attachment_content_by_id**](AttachmentsApi.md#put_attachment_content_by_id) | **PUT** /attachments/{attachmentId}/content | Replace the content of an attachment


# **delete_attachment_by_id**
> delete_attachment_by_id(attachment_id)

Delete an attachment

deletes an attachment based on the attachmentId supplied.

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
    api_instance = trilium_client.AttachmentsApi(api_client)
    attachment_id = 'attachment_id_example' # str | 

    try:
        # Delete an attachment
        api_instance.delete_attachment_by_id(attachment_id)
    except Exception as e:
        print("Exception when calling AttachmentsApi->delete_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 

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
**204** | attachment deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_by_id**
> Attachment get_attachment_by_id(attachment_id)

Get an attachment

Returns an attachment identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attachment import Attachment
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
    api_instance = trilium_client.AttachmentsApi(api_client)
    attachment_id = 'attachment_id_example' # str | 

    try:
        # Get an attachment
        api_response = api_instance.get_attachment_by_id(attachment_id)
        print("The response of AttachmentsApi->get_attachment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->get_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attachment response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_content**
> bytes get_attachment_content(attachment_id)

Get the content of an attachment

Returns attachment content identified by its ID. The response carries the attachment's MIME type as its `Content-Type`.

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
    api_instance = trilium_client.AttachmentsApi(api_client)
    attachment_id = 'attachment_id_example' # str | 

    try:
        # Get the content of an attachment
        api_response = api_instance.get_attachment_content(attachment_id)
        print("The response of AttachmentsApi->get_attachment_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->get_attachment_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 

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
**200** | attachment content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_attachments**
> List[Attachment] get_note_attachments(note_id)

List the attachments of a note

Returns all attachments for a note identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attachment import Attachment
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
    api_instance = trilium_client.AttachmentsApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        # List the attachments of a note
        api_response = api_instance.get_note_attachments(note_id)
        print("The response of AttachmentsApi->get_note_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->get_note_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

[**List[Attachment]**](Attachment.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of attachments |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attachment_by_id**
> Attachment patch_attachment_by_id(attachment_id, attachment)

Update an attachment

patch an attachment identified by the attachmentId with changes in the body. Only role, mime, title, and position are patchable.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attachment import Attachment
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
    api_instance = trilium_client.AttachmentsApi(api_client)
    attachment_id = 'attachment_id_example' # str | 
    attachment = trilium_client.Attachment() # Attachment | 

    try:
        # Update an attachment
        api_response = api_instance.patch_attachment_by_id(attachment_id, attachment)
        print("The response of AttachmentsApi->patch_attachment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->patch_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 
 **attachment** | [**Attachment**](Attachment.md)|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attribute updated |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attachment**
> Attachment post_attachment(create_attachment)

Create an attachment

create an attachment

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attachment import Attachment
from trilium_client.models.create_attachment import CreateAttachment
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
    api_instance = trilium_client.AttachmentsApi(api_client)
    create_attachment = trilium_client.CreateAttachment() # CreateAttachment | 

    try:
        # Create an attachment
        api_response = api_instance.post_attachment(create_attachment)
        print("The response of AttachmentsApi->post_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->post_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_attachment** | [**CreateAttachment**](CreateAttachment.md)|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | attachment created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_attachment_content_by_id**
> put_attachment_content_by_id(attachment_id, body)

Replace the content of an attachment

Updates attachment content identified by its ID

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
    api_instance = trilium_client.AttachmentsApi(api_client)
    attachment_id = 'attachment_id_example' # str | 
    body = 'body_example' # str | New content of the attachment. Send text as `text/plain` and binary data (such as an image or a PDF) as `application/octet-stream`; other content types are not accepted. 

    try:
        # Replace the content of an attachment
        api_instance.put_attachment_content_by_id(attachment_id, body)
    except Exception as e:
        print("Exception when calling AttachmentsApi->put_attachment_content_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 
 **body** | **str**| New content of the attachment. Send text as &#x60;text/plain&#x60; and binary data (such as an image or a PDF) as &#x60;application/octet-stream&#x60;; other content types are not accepted.  | 

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
**204** | attachment content updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

