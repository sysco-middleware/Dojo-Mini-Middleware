#!/bin/bash

JAVA_HOME={{ JAVA_HOME }}
export JAVA_HOME

'{{ ORACLE_HOME }}/oracle_common/bin/rcu -silent -createRepository -databaseType ORACLE -connectString {{ DB_CONN_STRING }} -dbUser sys -dbRole SYSDBA -schemaPrefix {{ SCHEMA_PREFIX }} -useSamePasswordForAllSchemaUsers true -component IAU -component IAU_APPEND -component IAU_VIEWER -component OPSS -component STB -component MDS -f < {{ MW_INSTALLER_DIR }}/passwords.txt'
