# MetricsVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** |  | [optional] 
**db** | **int** |  | [optional] 
**node** | **str** |  | [optional] 
**sync** | **int** |  | [optional] 
**build_date** | **str** |  | [optional] 
**build_revision** | **str** |  | [optional] 

## Example

```python
from trilium_client.models.metrics_version import MetricsVersion

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsVersion from a JSON string
metrics_version_instance = MetricsVersion.from_json(json)
# print the JSON string representation of the object
print(MetricsVersion.to_json())

# convert the object into a dict
metrics_version_dict = metrics_version_instance.to_dict()
# create an instance of MetricsVersion from a dict
metrics_version_from_dict = MetricsVersion.from_dict(metrics_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


