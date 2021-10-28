## HOW TO RUN

**NOTE**: Make sure to have the filenames / version no as provided in the example

- Copy the FMW jar and JDK file to the directory files
    fmw_12.2.1.4.0_infrastructure.jar
    jdk-8u202-linux-x64.tar.gz

- For now the variables can be updated only under the role ***FMW-Infra/vars*** directory
    You can set the be varilables for installation:
     - WLS & JDK VERSION
     - USER/GROUP
     - Installation Location - APP_HOME

    All the directories including JAVA_HOME and ORACLE_HOME will be created under APP_HOME


- Run the playbook as below 
```
    ansible-playbook fmw_install.yml -b -vv
```