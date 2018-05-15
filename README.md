**First install Ansible version 2.5.2:**

- $ sudo apt-get update

- $ sudo apt-get install software-properties-common

- $ sudo apt-add-repository ppa:ansible/ansible

- $ sudo apt-get update

- $ sudo apt-get install ansible

------------



**Then install git:**

$ sudo apt-get update

$ sudo apt-get install git


------------



**Create a file:**
/home/${USER}/.vault_pass.txt
with the password: adminadmin


------------


**Clone the Ansible repository:**


https://github.com/lidorrodil/ansible.git


**Checkout the branch:** jenkins-docker-implementation

**Execute:** ansible-playbook ci-server.yml -i production -vv


------------


*The playbook ci-server.yml will install Jenkins on your localhost.


An extra playbook cwt_configuration.yml will create a docker_cwt job. (It's a part of the ci-server.yml)


------------



## **Jenkins will be available in the following web: localhost:8080**



------------



Run the job docker_cwt from Jenkins in order to create your container on your localhost.
**Remember to type a unique container name.*

The container contain a nginx service.
Try in your browser to type: localhost:80

------------



### Note:

**PROBLEM:**

-  Docker build can't download packages
	
**SOLUTION:**

- This problem occurs in an environment that has a private DNS server, or the network blocks the Google's DNS servers. Even if the docker container can ping 8.8.8.8, the build still needs to have access to the same private DNS server behind your firewall or Data Center.
	
Steps to take:

1. $ sudo cat /etc/resolv.conf 

2. nameserver 127.0.1.1

3. nameserver 8.8.8.8


#### The host_vars include a directory 127.0.0.1 with vars. Remember to adjust the username and password based on your system authentication.
