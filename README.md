# INET 4031 Add User Script (Python)

**Python Script for Adding Users/Groups to a System**

## Description

This Python3 Script reads user/group data from an input file, processes the file line-by-line and adds each user to the system.

This script requires the `os` , `sys`  and `re` built-in Python modules in order to read the input file via `stdin` , process it and then issue commands to the operating system to actually create the users.

The input file contains user/group information separated by `:` . Users described in the input file that should not be created can be commented out by starting the line with a `#` .

## Operation

### Input File Specification

The input file should have the following format:

- ** username:default_password:last_name:first_name:comma_separated_list_of_groups

For example:

jdoe11:mypass:Doe:John:admins, reviewers

The name of the input file is up to the user.  Convention is create-users.input

### Running the Script

This Python script can be run as a normal Python3 script as in:

```bash
sudo python3 create-users.py < create-users.input
```

Or you can take advantage of the Shebang line pointing to Python3. i.e. `#!/usr/bin/python3` and run the script directly:
```bash
chmod a+x create-users.py  # Give execution permissions to file
sudo ./create-users.py < create-users.input
```
