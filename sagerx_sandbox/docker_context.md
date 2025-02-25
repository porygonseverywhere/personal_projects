### The Installation Guide suggests running two 'docker-compose' commands back to back. Is that normal?

`docker-compose up airflow-init`

followed by,

`docker-compose up`


##### Yep!

The *airflow-init* service is typically responsible for initializing the Airflow database and creating the necessary tables.
This initialization step needs to be completed before the other Airflow services (such as the webserver, scheduler, and worker) can start and function correctly. 
Running` docker compose up airflow-init` specifically executes this initialization task.
After the initialization is complete, running docker compose up starts all the Airflow services, including those that depend on the initialized database.
This ensures that Airflow is fully functional and ready to use.
Therefore, this two-step process is a standard practice for setting up Airflow with Docker Compose.

