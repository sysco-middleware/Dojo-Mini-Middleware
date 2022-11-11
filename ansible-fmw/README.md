# Dojo-Mini-Middleware Install & Configure

## How-to

### 1. Clone the repo

### 2. Prepare **inventory_dojo** file in ansible-fmw

dojoserver ansible_host=FIXME_IP ansible_ssh_user=FIXME_USER ansible_ssh_private_key_file=~/.ssh/FIXME_ssh.key

### 3. Setup the infrastructure

We can setup the infrastructure by using either of the two playbooks fmw_infrastructure_maker.yml or fmw_wls_instance_maker.yml

Update the playbook - **fmw_infrastructure_maker.yml**

```yaml
    # update the hosts field
    # comment / uncomment the roles required
    dojo-jdk-installer : # to copy jdk tarball & install jdk 
    dojo-fmw-installer : # to copy binary & install FMW Infra
```

Copy the FMW jar and JDK file under the  **files** directory

```$
├── files
│   ├── fmw_12.2.1.4.0_wls_lite_generic.jar
│   └── jdk-8u311-linux-x64.tar.gz
```

Update the variables in  **variables.yml** file.

* TIP : Refer the directory structure and modify the variables based on customization required

Setup the infrastructure by running the below command

```bash
ansible-playbook -i inventory_dojo fmw_infrastructure_maker.yml -vvv 
```

or

```bash
ansible-playbook -i inventory_dojo fmw_wls_instance_maker.yml -b -vvv
```

### 4. Domain creation using WDT 

Use this collection [zeusbaba.wdt](https://galaxy.ansible.com/zeusbaba/wdt) from Ansible Galaxy  
NB! first and foremost; make sure that collection is installed!

1. Install the collection

```bash
ansible-galaxy collection install zeusbaba.wdt    
```

2. Start the WDT setup and domain creation

```bash
# now you can run the playbook for domain creation
 ansible-playbook -i inventory_dojo  fmw_wls_domain_maker.yml -vvv
```

### Directory structure Reference

```
$(ORACLE_BASE)
 - $(MW_INSTALLER_DIR)
 - java
	- $(JAVA_HOME) # java_latest which will be a symlink
	- $(JDK_DIR)
 - product
	- $(ORACLE_HOME)
 - config
	- $(DOMAIN_HOME)
		- DOMAIN_NAME
	- applications
```

### 5. FMW LifeCycle using Ansible 

Use playbook fmw_wls_lifecycle.yml to automate the lifecycle of WLS.
Life cycle currently support below operations:

* Start Admin server & start nodemanager combinedly.  
`ansible-playbook -i inventory_dojo fmw_wls_lifecycle.yml --tags=start`
* Start Admin server individually.  
`ansible-playbook -i inventory_dojo fmw_wls_lifecycle.yml --tags=startAdmin`
* Start NodeManager server individually.  
`ansible-playbook -i inventory_dojo fmw_wls_lifecycle.yml --tags=startNodeManager`
* Stop Admin server & start nodemanager combinedly.  
`ansible-playbook -i inventory_dojo fmw_wls_lifecycle.yml --tags=stop`
* Stop Admin server individually.  
`ansible-playbook -i inventory_dojo fmw_wls_lifecycle.yml --tags=stopAdmin`
* Stop NodeManager server individually.  
`ansible-playbook -i inventory_dojo fmw_wls_lifecycle.yml --tags=stopNodeManager`


### 6. Domain update using WDT

We will use the same collection [zeusbaba.wdt](https://galaxy.ansible.com/zeusbaba/wdt) for updating the domain.

Run the playbook:

```bash
ansible-playbook -i inventory_dojo fmw_wls_domain_update.yml -vvv 
```

This will update the domain. But we need to restart the server to see the changes.  
Reason: The update domain is performed in offline mode.  
