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