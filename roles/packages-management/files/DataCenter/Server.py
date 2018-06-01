#!/usr/bin/python
# -*- coding: utf-8 -*-
class Server:
    """A server contains:
        1. which packages are installed
        2. IP
        3. Hostname
        4. IPtables configurations

    Attributes:
        hostname: A hostname representing the server's name.
        ip: A ip address of the server.
        packages: Server packages list
        iptables: Manage servers iptables rules (support for blocking input and output traffic by IP or port)
    """

    def __init__(self, hostname, ip, packages=[], group=0):
        self.hostname = hostname
        self.ip = ip
        self.group = group
        self.packages = packages
        self.iptables = []

    def add_package(self, package):
        for exist_package in self.packages:
            if (exist_package == package):
                return False
        self.packages.append(package)

    def add_iptable(self, iptable):
        self.iptables.append(iptable)


