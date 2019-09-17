# fa19-516-162: Cloudmesh Common
# E.Cloudmesh.Common.3
# Develop a program that demonstrates the use of FlatDict.

from cloudmesh.common.FlatDict import FlatDict

student = {"Name": { "FirstName": "Shivani", "LastName": "Katukota"},
           "Program": "ISE",
           "University": "IU Bloomington"}

student = FlatDict(student)

print(f"My name is {student.Name__FirstName} and I study at {student.University}.")