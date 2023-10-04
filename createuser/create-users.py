#!/usr/bin/python3

import os
import re
import sys

def main():
    for line in sys.stdin:

        match = re.match("^#", line)  # Match if line starts with '#'
        fields = line.strip().split(':')

        if match or len(fields) != 5:  # Check if the number of columns in line is different than 5. Basically cheking that
            continue                   # the user creation information for this user is complete
                                       # Also check if there was a match in the comment checking regex

        username = fields[0]
        password = fields[1]
        gecos = f"{fields[3]} {fields[2]},,,"
        groups = fields[4].split(',')  # Split group information into a list containing the groups names

        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        os.system(cmd)  # The os.system() method executes a command in the operating system (bash)

        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        os.system(cmd)

        for group in groups:  # This line add users to the corresponding groups as defined in the input file
                              # The for loop is required because some users need to be assigned to more than one group
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                os.system(cmd)


if __name__ == '__main__':
    main()
