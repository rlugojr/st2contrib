# Remedy Integration Pack

This integration allows bi-directional communication between StackStorm and Remedy API

Initial work based on PR by Renan Caldeira, updated by Lindsay Hill

## Configuration

Copy the example configuration in [remedy.yaml.example](./remedy.yaml.example)
to `/opt/stackstorm/configs/remedy.yaml` and edit as required.

It must contain:

* `servername` - Remedy Server Name
* `serverport` - Remedy Server Port
* `username` - Username
* `password` - Password

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.


## Actions

* `remedy.get` - Get an entry using a dictionary query from a Remedy Table
* `remedy.get_non_structured` - Get an entry using a string query from a Remedy Table
* `remedy.update` - Update an entry in a Remedy Table
* `remedy.insert` - Insert an entry to a Remedy Table
* `remedy.delete` - Delete an entry from a Remedy Table
