# Metrics

Instance and database metrics, as served by GET /etapi/metrics?format=json

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**MetricsVersion**](MetricsVersion.md) |  | [optional] 
**database** | [**MetricsDatabase**](MetricsDatabase.md) |  | [optional] 
**note_types** | **Dict[str, int]** | Number of active notes per note type | [optional] 
**attachment_types** | **Dict[str, int]** | Number of active attachments per MIME type | [optional] 
**statistics** | [**MetricsStatistics**](MetricsStatistics.md) |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from trilium_client.models.metrics import Metrics

# TODO update the JSON string below
json = "{}"
# create an instance of Metrics from a JSON string
metrics_instance = Metrics.from_json(json)
# print the JSON string representation of the object
print(Metrics.to_json())

# convert the object into a dict
metrics_dict = metrics_instance.to_dict()
# create an instance of Metrics from a dict
metrics_from_dict = Metrics.from_dict(metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


