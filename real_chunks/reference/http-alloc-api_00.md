### HTTP-API: alloc_info > Example: > Query

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Web Server](Webserver) → [APIs](WebServerAPIs) → HTTP Alloc API |
|------------------------------------------------------------------|

# HTTP-API: alloc_info

```http://localhost:8888/api/http/alloc_info```

## Purpose

Request a JSON encoded sub-list of allocation descriptors from the Memory Manager’s alloc_info list.

## Query String Parameters
| Parameter|Default|Description                       |
|-------------|----|----------------------------------|
| ```start``` | 0  | starting index of the sub-list.  |
| ```count``` | 20 | number of allocation descriptors.|

### EXAMPLE:

```http://localhost:8888/api/http/alloc_info?start=20&count=2```

## Query Response

Returns a JSON object containing four name-value pairs:

### JSON Response Object

| Name              | Value Description                       |
|-------------------|-----------------------------------------|
| ```alloc_total``` | Total number allocations in the Memory Manager’s alloc_info list. |
| ```chunk_size```  | Number of allocation description objects in ```alloc_list```. |
| ```chunk_start``` | The Memory Manager alloc_info index of the first ```alloc_list``` element below|
| ```alloc_list```  | Array of JSON Allocation Description objects (described below). |


### JSON Allocation Description Object

| Name          | Value Description                                                               |
|---------------|---------------------------------------------------------------------------------|
| ```name```    | Name of the allocation. May be ```Null```                                       |
| ```start```   | Starting address of the allocation.                                             |
| ```end```     | Ending address of the allocation.                                               |
| ```num```
