# Dojo-Mini-Middleware Install & Configure

## How-to
Clone the repo

Update the playbook - **fmw_infrastructure.yml**

    - update the hosts field
    - comment / uncomment the roles required \
        dojo-jdk-installer : to copy jdk tarball & install jdk \
        dojo-fmw-installer : to copy binary & install FMW Infra
    

Copy the FMW jar and JDK file under the  **files** directory

    example:
    - fmw_12.2.1.4.0_infrastructure.jar
    - jdk-8u311-linux-x64.tar.gz

Update the vaiables in  **variables.yml** file 

    TIP : Refer the directory structure and modify the variables based on customization required

## Directory structure created

```
$(ORACLE_BASE)
 - $(MW_INSTALLER_DIR)
 - java
	- $(JAVA_HOME) # java_latest which will be a symlink
	- $(JDK_DIR
 - product
	- $(ORACLE_HOME)
 - config
	- $(DOMAIN_HOME)
		- DOMAIN_NAME
	- applications
```
**NOTE :** All variables are enclosed with **$( )** and they can be modified using the `variables.yml`

## Run the playbook
```
    ansible-playbook fmw_instance_maker.yml -b -vv
```


### Domain creation using WDT 
Use this collection [zeusbaba.wdt](https://galaxy.ansible.com/zeusbaba/wdt) from Ansible Galaxy  
NB! first and foremost; make sure that collection is installed!  
it is better to install from GitHub repo so that you have the latest & greatest updates  
```
ansible-galaxy collection install git+https://github.com/zeusbaba/ansible-collection-wdt    
```
now go ahead with more  
```
# prepare `inventory_dojo` file, e.g.  
dojoserver ansible_host=FIXME_IP ansible_ssh_user=FIXME_USER ansible_ssh_private_key_file=~/.ssh/FIXME_ssh.key

# now you can run the playbook for domain creation
 ansible-playbook -i inventory_dojo  fmw_wls_domain_maker.yml -vvv
```

### FMW LifeCycle using Ansible 

Use playbook fmw_wls_lifecycle.yml to automate the lifecycle of WLS.
Life cycle currently suppport below operations:
* Start Admin server & start nodemanager combinedly 
` ansible-playbook fmw_wls_lifecycle.yml --tags=start`
* Start Admin server individually
` ansible-playbook fmw_wls_lifecycle.yml --tags=startAdmin`
* Start NodeManager server individually
` ansible-playbook fmw_wls_lifecycle.yml --tags=startNodeManager`
* Stop Admin server & start nodemanager combinedly 
` ansible-playbook fmw_wls_lifecycle.yml --tags=stop`
* Stop Admin server individually
` ansible-playbook fmw_wls_lifecycle.yml --tags=stopAdmin`
* Stop NodeManager server individually
` ansible-playbook fmw_wls_lifecycle.yml --tags=stopNodeManager`


### Tips & Tricks  
How to create ssh tunnel so that you access Weblogic console?   
```
ssh -L 7001:127.0.0.1:7001 firstname.surname@DOJO_IP -i ~/.ssh/your_ssh_key
```
now you can access the console simply via `http://localhost:7001/console`  
