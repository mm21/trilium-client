# MetricsStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oldest_note** | **str** |  | [optional] 
**newest_note** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**database_size_bytes** | **int** |  | [optional] 

## Example

```python
from trilium_client.models.metrics_statistics import MetricsStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsStatistics from a JSON string
metrics_statistics_instance = MetricsStatistics.from_json(json)
# print the JSON string representation of the object
print(MetricsStatistics.to_json())

# convert the object into a dict
metrics_statistics_dict = metrics_statistics_instance.to_dict()
# create an instance of MetricsStatistics from a dict
metrics_statistics_from_dict = MetricsStatistics.from_dict(metrics_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


