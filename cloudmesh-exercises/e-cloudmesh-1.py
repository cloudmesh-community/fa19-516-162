# fa19-516-162: Cloudmesh Common
# E.Cloudmesh.Common.1
# Develop a program that demonstrates the use of BANNER, HEADING, and VERBOSE.

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.variables import Variables
from cloudmesh.common.debug import VERBOSE

# BANNER Example
banner("Cloud Mesh Banner", label='Cloud Mesh Assignment 1')

# HEADING Example
HEADING("This exercise is saved in file")

# VERBOSE Example
variables = Variables()
variables['verbose'] = 10
sample = {"one": 1, "two": 2, "three": 3}
VERBOSE(sample)