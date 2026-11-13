# MetricsDatabase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_notes** | **int** |  | [optional] 
**deleted_notes** | **int** |  | [optional] 
**active_notes** | **int** |  | [optional] 
**protected_notes** | **int** |  | [optional] 
**total_attachments** | **int** |  | [optional] 
**deleted_attachments** | **int** |  | [optional] 
**active_attachments** | **int** |  | [optional] 
**total_revisions** | **int** |  | [optional] 
**total_branches** | **int** |  | [optional] 
**total_attributes** | **int** |  | [optional] 
**total_blobs** | **int** |  | [optional] 
**total_etapi_tokens** | **int** |  | [optional] 
**total_recent_notes** | **int** |  | [optional] 

## Example

```python
from trilium_client.models.metrics_database import MetricsDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsDatabase from a JSON string
metrics_database_instance = MetricsDatabase.from_json(json)
# print the JSON string representation of the object
print(MetricsDatabase.to_json())

# convert the object into a dict
metrics_database_dict = metrics_database_instance.to_dict()
# create an instance of MetricsDatabase from a dict
metrics_database_from_dict = MetricsDatabase.from_dict(metrics_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


