# trilium_client.CalendarApi

All URIs are relative to *http://localhost:37740/etapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_day_note**](CalendarApi.md#get_day_note) | **GET** /calendar/days/{date} | Get a day note
[**get_inbox_note**](CalendarApi.md#get_inbox_note) | **GET** /inbox/{date} | Get the inbox note
[**get_month_note**](CalendarApi.md#get_month_note) | **GET** /calendar/months/{month} | Get a month note
[**get_week_first_day_note**](CalendarApi.md#get_week_first_day_note) | **GET** /calendar/week-first-day/{date} | Get the day note starting the week
[**get_week_note**](CalendarApi.md#get_week_note) | **GET** /calendar/weeks/{week} | Get a week note
[**get_year_note**](CalendarApi.md#get_year_note) | **GET** /calendar/years/{year} | Get a year note


# **get_day_note**
> Note get_day_note(var_date)

Get a day note

returns a day note for a given date. Gets created if doesn't exist.

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
    api_instance = trilium_client.CalendarApi(api_client)
    var_date = '2022-02-22' # date | 

    try:
        # Get a day note
        api_response = api_instance.get_day_note(var_date)
        print("The response of CalendarApi->get_day_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_day_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**|  | 

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
**200** | day note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox_note**
> Note get_inbox_note(var_date)

Get the inbox note

returns an "inbox" note, into which note can be created. Date will be used depending on whether the inbox is a fixed note (identified with #inbox label) or a day note in a journal. A database with neither returns the root note, and ignores the date, rather than creating a journal to hold a day note.


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
    api_instance = trilium_client.CalendarApi(api_client)
    var_date = '2022-02-22' # date | 

    try:
        # Get the inbox note
        api_response = api_instance.get_inbox_note(var_date)
        print("The response of CalendarApi->get_inbox_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_inbox_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**|  | 

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
**200** | inbox note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_month_note**
> Note get_month_note(month)

Get a month note

Returns a month note for a given month (format YYYY-MM, e.g., 2022-02). The note is created if it doesn't exist.

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
    api_instance = trilium_client.CalendarApi(api_client)
    month = '2022-02' # str | 

    try:
        # Get a month note
        api_response = api_instance.get_month_note(month)
        print("The response of CalendarApi->get_month_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_month_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**|  | 

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
**200** | month note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_week_first_day_note**
> Note get_week_first_day_note(var_date)

Get the day note starting the week

Returns the day note for the first day of the week containing the given date, honouring
the configured first day of week. The note is created if it doesn't exist. This returns a
day note, not a week note, so unlike /calendar/weeks/{week} it does not require the
enableWeekNote label on the calendar root.


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
    api_instance = trilium_client.CalendarApi(api_client)
    var_date = '2022-02-22' # date | Any date within the week, in the format YYYY-MM-DD.

    try:
        # Get the day note starting the week
        api_response = api_instance.get_week_first_day_note(var_date)
        print("The response of CalendarApi->get_week_first_day_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_week_first_day_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| Any date within the week, in the format YYYY-MM-DD. | 

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
**200** | day note starting the week |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_week_note**
> Note get_week_note(week)

Get a week note

Returns a week note for a given ISO week (format YYYY-Www, e.g., 2025-W01). The note is created if it doesn't exist.

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
    api_instance = trilium_client.CalendarApi(api_client)
    week = '2025-W01' # str | The ISO 8601 week identifier (YYYY-Www).

    try:
        # Get a week note
        api_response = api_instance.get_week_note(week)
        print("The response of CalendarApi->get_week_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_week_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **week** | **str**| The ISO 8601 week identifier (YYYY-Www). | 

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
**200** | week note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_year_note**
> Note get_year_note(year)

Get a year note

Returns a year note for a given year (format YYYY, e.g., 2022). The note is created if it doesn't exist.

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
    api_instance = trilium_client.CalendarApi(api_client)
    year = '2022' # str | 

    try:
        # Get a year note
        api_response = api_instance.get_year_note(year)
        print("The response of CalendarApi->get_year_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_year_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  | 

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
**200** | year note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

