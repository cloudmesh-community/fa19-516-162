# Oracle Compute and Storage Service

Shivani Katukota, [fa19-516-162](https://github.com/cloudmesh-community/fa19-516-162)

Example code at github location: 
<https://github.com/cloudmesh/cloudmesh-oracle/blob/master/examples/examples.py>

Provider.py is updated at location:
<https://github.com/cloudmesh/cloudmesh-oracle/tree/master/cloudmesh/compute/oracle>

Github Insights:
<https://github.com/cloudmesh/cloudmesh-oracle/graphs/contributors>

## Abstract

- Oracle has released a free tier for Oracle cloud.

## Cloudmesh Compute

- cloudmesh-compute project will identify Oracle's python API and develop its 
provider.
- cloudmesh-compute project will identify how to manage credentials in Oracle.
- cloudmesh-compute project will write and run pytests on Oracle cloud. 

## Cloudmesh Storage

- cloudmesh-storage project will add the feature to access storage from Oracle 
services.
- cloudmesh-storage project will provide a REST service based on OpenAPI that 
uses the cloudmesh API.
- cloudmesh-storage project will implement virtual directory from local.

## References

## Progress

### Week 1
1. Setup Oracle cloud config file and installed python api for Oracle
2. Made following functions to work as examples on Oracle cloud using python
    - List images
    - Find image with given name
    - List flavors on cloud
    - Stop server with given name
    - Resume stopped server
    - List all servers
    - Delete/Terminate server
    - Reboot server
    - Rename server

### Week 2
1. Figured out how to use cloudmesh.yaml for credentials
2. Installed mongo db on windows successfully

### Week 3
1. Created python examples for following functions: 
    - create vcn and subnet
    - launch an instance
2. Started integrating examples into Provider.py - In Progress, 
Have not checked-in yet

## Work breakdown
