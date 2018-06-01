#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Server
import DataCenter
import argparse
import csv
import paramiko

def main():

    # Define arguments
    parser = \
        argparse.ArgumentParser(description='Helper to DataCenter.')
    parser.add_argument('-i', '--ip',
                        help='Server to be connected', required=True)
    parser.add_argument('-u', '--username',
                        help='Username for the server', required=True)
    parser.add_argument('-p', '--password',
                        help='Password for the server', required=True)
    parser.add_argument('-c', '--command',
                        help='Command such as add, remove, update, install', required=True)
    parser.add_argument('-pck', '--packages',
                        help='Packages to install', required=False)

    # Parse arguments
    args = parser.parse_args()

    ip = args.ip
    username = args.username
    password = args.password
    command = args.command
    packages= args.packages

    # Create a DataCenter
    DC = DataCenter.DataCenter()

    if (command == "add"):
        # Add the server to the DataCenter
        DC.add_server(username, ip, password)

    if (command == "remove"):
        DC.remove_server(ip)

    if (command == "update"):
        DC.update_server(username, ip, password)

    if (command == "install"):
        DC.install_packages(username, ip, password, packages)

if __name__ == '__main__':
    main()
