### Pre-tasks:
**Creating IAM Users (Console)**
- https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console

- 	 Creating keypair
-  Creating group_vars/localhost/vars.yml
	1. AWS_ACCESS_KEY_ID:
	2. AWS_SECRET_ACCESS_KEY:
	3. ansible_ssh_user:
	4. ansible_ssh_private_key_file: keypair_file.PEM

**Tasks:**
- Execute: ansible-playbook -i production provision-ec2.yml
- 	The playbook that is metioned below should be defined in the crontab.

*ansible/roles/provision-ec2/tasks/check_cpu_instance.yml* 



[![ELB & Security Group](http://aws.typepad.com/.a/6a00d8341c534853ef01a5119a8c70970c-pi "ELB & Security Group")](http://aws.typepad.com/.a/6a00d8341c534853ef01a5119a8c70970c-pi "ELB & Security Group")
