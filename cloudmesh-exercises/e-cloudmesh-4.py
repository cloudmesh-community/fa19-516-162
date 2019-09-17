# fa19-516-162: Cloudmesh Common
# E.Cloudmesh.Common.4
# Develop a program that demonstrates the use of cloudmesh.common.Shell.

from cloudmesh.common.Shell import Shell

# Check python version installed
result = Shell.check_python()
print(result)

# Check if command "ping" exists
result = Shell.command_exists("ping")
print(result)

# Check location of git executable
result = Shell.which("git")
print(result)
