#!/usr/bin/python
# -*- coding: utf-8 -*-
# We have a Data Center with 500 servers and we would like to write system for managing our Data Center.

import os
import Server
import argparse
import csv
import paramiko

class DataCenter:

    def __init__(self):
        try:
            ifile  = open('test.csv', "rU")
            reader = csv.reader(ifile)
            next(reader)
            for row in reader:
                server = Server.Server(row[0], row[1], row[2], row[3])
            ifile.close()
        except Exception as error:
            print(str(error))

    def add_server(self, username, ip, password):
        try:
            server = self.create_server(username, ip, password)
            ofile  = open('test.csv', "a")
            writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\r')
            writer.writerow([server.hostname, server.ip, server.packages, '1'])
            ofile.close()
        except Exception as error:
            print(str(error))

    def remove_server(self, ip):
        try:
            with open("test.csv", "rU") as inp, open("temp_test.csv", "wb") as out:
                writer = csv.writer(out)
                for row in csv.reader(inp):
                    if row[1] != ip:
                        writer.writerow(row)
        except Exception as error:
            print(str(error))
        os.remove("test.csv")
        os.rename("temp_test.csv", "test.csv")

    def update_server(self, username, ip, password):
        self.remove_server(ip)
        self.add_server(username, ip, password)

    def connect_to_server(self, username, ip, password):

        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
        ssh.connect(ip, 22, username, password)

        return ssh

    def install_packages(self, username, ip, password, packages):

        ssh = self.connect_to_server(username, ip, password)

        # Get the install packages on the server
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("apt-get install %s" % packages)

        # Read the packages list
        output = ssh_stdout.read()

        self.update_server(username, ip, password)

    def add_package_group(self, package, group):
        for server in self.servers:
            if (server.group == group):
                server.add_package(package)

    def create_server(self, username, ip, password):

        # Create a Server
        server = Server.Server(username, ip)

        ssh = self.connect_to_server(username, ip, password)

        # Get the install packages on the server
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("dpkg-query -f '${binary:Package}\n' -W")

        # Read the packages list
        output = ssh_stdout.read()

        # Add the packages to the server object
        for package in output.splitlines():
            server.add_package(package)

        return server

