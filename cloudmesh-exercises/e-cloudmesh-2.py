# fa19-516-162: Cloudmesh Common
# E.Cloudmesh.Common.2
# Develop a program that demonstrates the use of dotdict.

from cloudmesh.common.dotdict import dotdict

student = {"Name": "Shivani",
           "Program": "ISE",
           "University": "IU Bloomington"}

student = dotdict(student)

print(f"My name is {student.Name} and I study at {student.University}.")
