### Pre-tasks:
**	 Creating IAM Users (Console)**
- https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console

- 	 Creating keypair
-  Creating group_vars/localhost/vars.yml
		AWS_ACCESS_KEY_ID:
		AWS_SECRET_ACCESS_KEY:
		ansible_ssh_user:
		ansible_ssh_private_key_file: keypair_file.PEM

**Tasks:**
	- Execute: ansible-playbook -i production provision-ec2.yml
	- The playbook that is metioned below should be defined in the crontab.
		ansible/roles/provision-ec2/tasks/check_cpu_instance.yml 
