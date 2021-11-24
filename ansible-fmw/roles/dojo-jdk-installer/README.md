Role Name
=========

Ansible role to install JDK  

Requirements
------------

Copy the JDK file under the  **files** directory

Role Variables
--------------

Below are the variables used by the role and they should be defined in the **variables.yml** file. Only the **JDK_DIR** variable need to be updated. *JAVA_DIR* & *JAVA_HOME* will be based on what will be defined by *JDK_DIR*

    JDK_DIR: '{{ JAVA_DIR }}/jdkx.x.x_xxx'
    JAVA_DIR: '{{ ORACLE_BASE }}/java'
    JAVA_HOME: '{{ JAVA_DIR }}/java_latest'


Dependencies
------------

No dependency

Example Playbook
----------------

Update the variables in **variables.yml** on the playbook directory path with playbook as below

    hosts: <server_group>
    vars_files:
      - '{{ playbook_dir }}/variables.yml'
    roles:
      - dojo-jdk-installer

License
-------

MIT

Author Information
------------------

This repo is crafted by a team of doers who practice continuously as DOJO team.  
We learn by doing, we craft working software, and we share.  
