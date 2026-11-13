# trilium_client.AttributesApi

All URIs are relative to *http://localhost:37740/etapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attribute_by_id**](AttributesApi.md#delete_attribute_by_id) | **DELETE** /attributes/{attributeId} | Delete an attribute
[**get_attribute_by_id**](AttributesApi.md#get_attribute_by_id) | **GET** /attributes/{attributeId} | Get an attribute
[**patch_attribute_by_id**](AttributesApi.md#patch_attribute_by_id) | **PATCH** /attributes/{attributeId} | Update an attribute
[**post_attribute**](AttributesApi.md#post_attribute) | **POST** /attributes | Create an attribute


# **delete_attribute_by_id**
> delete_attribute_by_id(attribute_id)

Delete an attribute

deletes an attribute based on the attributeId supplied.

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
    api_instance = trilium_client.AttributesApi(api_client)
    attribute_id = 'attribute_id_example' # str | 

    try:
        # Delete an attribute
        api_instance.delete_attribute_by_id(attribute_id)
    except Exception as e:
        print("Exception when calling AttributesApi->delete_attribute_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**|  | 

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
**204** | attribute deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_by_id**
> Attribute get_attribute_by_id(attribute_id)

Get an attribute

Returns an attribute identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attribute import Attribute
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
    api_instance = trilium_client.AttributesApi(api_client)
    attribute_id = 'attribute_id_example' # str | 

    try:
        # Get an attribute
        api_response = api_instance.get_attribute_by_id(attribute_id)
        print("The response of AttributesApi->get_attribute_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->get_attribute_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attribute response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attribute_by_id**
> Attribute patch_attribute_by_id(attribute_id, attribute)

Update an attribute

patch an attribute identified by the attributeId with changes in the body. For labels, only value and position can be updated. For relations, only position can be updated. If you want to modify other properties, you need to delete the old attribute and create a new one.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attribute import Attribute
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
    api_instance = trilium_client.AttributesApi(api_client)
    attribute_id = 'attribute_id_example' # str | 
    attribute = trilium_client.Attribute() # Attribute | 

    try:
        # Update an attribute
        api_response = api_instance.patch_attribute_by_id(attribute_id, attribute)
        print("The response of AttributesApi->patch_attribute_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->patch_attribute_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**|  | 
 **attribute** | [**Attribute**](Attribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

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

# **post_attribute**
> Attribute post_attribute(attribute)

Create an attribute

create an attribute for a given note

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attribute import Attribute
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
    api_instance = trilium_client.AttributesApi(api_client)
    attribute = trilium_client.Attribute() # Attribute | 

    try:
        # Create an attribute
        api_response = api_instance.post_attribute(attribute)
        print("The response of AttributesApi->post_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->post_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute** | [**Attribute**](Attribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | attribute created |  -  |
**409** | an attribute with the given attributeId already exists (ATTRIBUTE_ALREADY_EXISTS) |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

