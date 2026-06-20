# Revision

Revision represents a snapshot of note's title and content at some point in the past.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision_id** | **str** |  | [optional] 
**note_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**mime** | **str** |  | [optional] 
**is_protected** | **bool** |  | [optional] [readonly] 
**title** | **str** |  | [optional] 
**blob_id** | **str** | ID of the blob object which effectively serves as a content hash | [optional] 
**date_last_edited** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**utc_date_last_edited** | **str** |  | [optional] 
**utc_date_created** | **str** |  | [optional] 
**utc_date_modified** | **str** |  | [optional] 
**content_length** | **int** |  | [optional] [readonly] 

## Example

```python
from trilium_client.models.revision import Revision

# TODO update the JSON string below
json = "{}"
# create an instance of Revision from a JSON string
revision_instance = Revision.from_json(json)
# print the JSON string representation of the object
print(Revision.to_json())

# convert the object into a dict
revision_dict = revision_instance.to_dict()
# create an instance of Revision from a dict
revision_from_dict = Revision.from_dict(revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


