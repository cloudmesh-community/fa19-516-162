# Oracle Compute and Storage Service

Shivani Katukota, [fa19-516-162](https://github.com/cloudmesh-community/fa19-516-162)

Insights: 

* <https://github.com/cloudmesh-community/fa19-516-162/graphs/contributors>
* <https://github.com/cloudmesh/cloudmesh-oracle/graphs/contributors>

Example code at github location: 

* <https://github.com/cloudmesh/cloudmesh-oracle/blob/master/examples/examples.py>

Code Directory:

* <https://github.com/cloudmesh/cloudmesh-oracle>

## Abstract

Oracle has released a free tier for Oracle cloud.

### Cloudmesh Compute

* cloudmesh-compute project will identify Oracle's python API and develop its 
provider.
* cloudmesh-compute project will identify how to manage credentials in Oracle.
* cloudmesh-compute project will write and run pytests on Oracle cloud. 

### Cloudmesh Storage

* cloudmesh-storage project will add the feature to access storage from Oracle 
services.
* cloudmesh-storage project will provide a REST service based on OpenAPI that 
uses the cloudmesh API.
* cloudmesh-storage project will implement virtual directory from local.

## References

:o2:

## Progress

### Week 1 (30th September)

1. Setup Oracle cloud config file and installed python api for Oracle
2. Made following functions to work as examples on Oracle cloud using python
    * List images
    * Find image with given name
    * List flavors on cloud
    * Stop server with given name
    * Resume stopped server
    * List all servers
    * Delete/Terminate server
    * Reboot server
    * Rename server

### Week 2 (7th October)

1. Figured out how to use cloudmesh.yaml for credentials
2. Installed mongo db on windows successfully

### Week 3 (14th October)

1. Created python examples for following functions: 
    * create vcn and subnet
    * launch an instance
2. Started integrating examples into Provider.py - In Progress, 
Have not checked-in yet

### Week 4 (21st October)

1. Integrated the examples into Provider.py
2. Fixed issues with integrated examples to make them run via cmd
3. Fixed issues with saving data in mongo db via commands 

### Week 5 (28th October)

1. Integrating examples related to instance start and stop

### Week 6 (4th November)

1. boot command worked but with minor defects

### Week 7 (11th November)

1. ssh command

### Week 8 (18th November)

1. boot and ssh work with default key
2. Issues running compute test cases
3. Started with oracle storage project

