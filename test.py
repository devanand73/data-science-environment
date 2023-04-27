import platform
import os
import pkg_resources

# Print Python version
print("Python version: ", platform.python_version())

# Print current directory
print("Current directory: ", os.getcwd())

# Get list of installed modules
modules = [i.key for i in pkg_resources.working_set]

# Sort modules in ascending order
modules.sort()

# Print sorted list of installed modules
print("List of installed modules (sorted): ")
for module in modules:
    print(module)
