# RecentChange

Represents a recent change event (creation, modification, or deletion).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_id** | **str** |  | [optional] 
**title** | **str** | Title at the time of the change (may be \&quot;[protected]\&quot; for protected notes) | [optional] 
**current_title** | **str** | Current title of the note (may be \&quot;[protected]\&quot; for protected notes) | [optional] 
**current_is_deleted** | **bool** | Whether the note is currently deleted | [optional] 
**current_delete_id** | **str** | Delete ID if the note is deleted | [optional] 
**current_is_protected** | **bool** | Whether the note is protected | [optional] 
**utc_date** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**can_be_undeleted** | **bool** | Whether the note can be undeleted (only present for deleted notes) | [optional] 

## Example

```python
from trilium_client.models.recent_change import RecentChange

# TODO update the JSON string below
json = "{}"
# create an instance of RecentChange from a JSON string
recent_change_instance = RecentChange.from_json(json)
# print the JSON string representation of the object
print(RecentChange.to_json())

# convert the object into a dict
recent_change_dict = recent_change_instance.to_dict()
# create an instance of RecentChange from a dict
recent_change_from_dict = RecentChange.from_dict(recent_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


