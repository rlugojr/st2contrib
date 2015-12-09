# Remedy Integration Pack

This integration allows bi-directional communication between StackStorm and Remedy API

# Overview


# Setup
## Configuration

### Outgoing Integration

* `servername` - Remedy Server Name
* `serverport` - Remedy Server Port
* `username` - Username
* `password` - Password

### Incoming Integration



```
Accept: application/json
Content-Type: application/json
```


## Actions

* `remedy.get` - Get an entry using a dictionary query from a Remedy Table
* `remedy.get_non_structured` - Get an entry using a string query from a Remedy Table
* `remedy.update` - Update an entry in a Remedy Table
* `remedy.insert` - Insert an entry to a Remedy Table
* `remedy.delete` - Delete an entry from a Remedy Table
