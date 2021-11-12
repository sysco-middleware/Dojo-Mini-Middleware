# Dojo-Mini-Middleware Install & Configure

## How-to
Clone the repo

Update the playbook - **fmw_install.yml**

    - update the hosts field
    - comment / uncomment the roles required \
        jdk_install : to copy jdk tarball & install jdk \
        FMW_Infra_Install : to copy binary & install FMW Infra
    

Copy the FMW jar and JDK file under the  **files** directory

    example:
    - fmw_12.2.1.4.0_infrastructure.jar
    - jdk-8u202-linux-x64.tar.gz

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
**NOTE :** All variables are enclosed with **$( )** and they can be modified using the varibales.yml

## Run the playbook
```
    ansible-playbook fmw_install.yml -b -vv
```

