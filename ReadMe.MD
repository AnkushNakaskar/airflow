#Airflow Project
* Install airflow on local using following cmd:
    ```
        * Create a new workspace folder and execute below commands
        * for example we have created below folder 
        * cd /Users/ankush.nakaskar/Office/PersonalProjects/airflow_workspace
        * brew install pip
        * sudo pip3 install virtualenv
        * virtualenv airflow_env
        * source airflow_env/bin/activate
        * pip3 install apache-airflow[gcp,sentry,statsd]
        * pip3 install pyspark
        * pip3 install sklearn
        - Now the airflow is install on path : cd /User/ankush.nakaskar/airflow
        * to check the all the DB creation for DAG store and meta data , run below cmds
            * airflow db init
            * Create user :
            ```
                airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@some.com

            ```
            * dag folder inside :   /User/ankush.nakaskar/airflow
            * if not , create for you, since you need to check the config in this folder.
            Folder look like this :
                ``` 
                    -rw-r--r--  1 ankush.nakaskar  1312973762   49455 Jul 18 11:56 airflow.cfg
                    -rw-r--r--  1 ankush.nakaskar  1312973762    4707 Jul 18 11:56 webserver_config.py
                    -rw-r--r--  1 ankush.nakaskar  1312973762       6 Jul 18 12:06 airflow-webserver.pid
                     drwxr-xr-x  4 ankush.nakaskar  1312973762     128 Jul 18 12:14 dags
                     drwxr-xr-x  5 ankush.nakaskar  1312973762     160 Jul 18 12:14 logs
                    -rw-r--r--  1 ankush.nakaskar  1312973762  761856 Jul 18 12:22 airflow.db
 
                ```    
            * Create the DAG's and inside the dag folder or move the hello_world.py into this .
            * Restart the schedular
            * to start schedular & webserver :
                * airflow scheduler
                * airflow webserver 
            * You can check logs here : /Users/ankush.nakaskar/airflow/logs/
                * If you find any exception or error in Dag file, all the logs will be printed here.
  
            * You can check the UI on : 
                http://localhost:8080/home
  ```
  
  * For reference Follow : https://insaid.medium.com/setting-up-apache-airflow-in-macos-2b5e86eeaf1