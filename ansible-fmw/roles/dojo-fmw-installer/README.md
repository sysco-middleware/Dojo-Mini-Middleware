Role Name
=========

Ansible role to Install and Configure Fusion Middleware (FMW)  

Requirements
------------

Copy the FMW binary file under the  **files** directory

Role Variables
--------------
Below are the variables used by the role, and they should be defined in the **variables.yml** file.

    ORACLE_BASE: "/home/dojowls"
    ORACLE_HOME: '{{ ORACLE_BASE }}/product/{{ WLS_VERSION }}'
    MW_INSTALLER_DIR: '{{ ORACLE_BASE }}/installers'

    INSTALL_TYPE: Fusion Middleware Infrastructure # OPTIONS: Fusion Middleware Infrastructure, Fusion Middleware Infrastructure With Examples.
    DECLINE_AUTO_UPDATES: True  # OPTIONS: True / False

Dependencies
------------

JDK installation must be completed before using this role. Define the *JDK_HOME* variable on *variables.yml* file as it will be used by *dojo-fmw-installer* role 

**dojo-jdk-installer** role can be used to install the jdk

Example Playbook
----------------

Update the variables in **variables.yml** on the playbook directory path with playbook as below

    hosts: <server_group>
    vars_files:
      - '{{ playbook_dir }}/variables.yml'
    roles:
      - dojo-jdk-installer
      - dojo-fmw-installer

License
-------

MIT

Author Information
------------------

This repo is crafted by a team of doers who practice continuously as DOJO team.  
We learn by doing, we craft working software, and we share.  
