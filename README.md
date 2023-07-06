
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>Stack Exchange Data Visualizer
</h1>
<h3>◦ ELT and Visualization of StackExchange data</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [🖼 Screenshots](#-screenshots)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)

---


## 📍 Overview

This web application combines FastAPI, Snowflake, Stack Exchange API, Superset, and Airflow to create a user-friendly tool for data extraction and analysis. In simple terms, it lets users log in, gather data from Stack Exchange, store this data in the Snowflake database, and create easy-to-understand visualizations with Superset. Moreover, it uses Airflow to automatically update the data every day. The main goal is to make it easy for users to understand and use Stack Exchange data to help them make informed decisions.

---

## 🖼 Screenshots

  ### Superset
  ![Screenshot 1](screenshots/Screenshot%202023-07-06%20at%2010.28.44%20PM.png)
  
  ### Airflow
  ![Screenshot 2](screenshots/Screenshot%202023-07-06%20at%2010.29.03%20PM.png)
  
  ### Snowflake
  ![Screenshot 3](screenshots/Screenshot%202023-07-06%20at%2010.31.12%20PM.png)


## 📂 Project Structure


```bash
repo
├── README.md
├── airflow
│   ├── airflow-webserver.pid
│   ├── airflow.cfg
│   ├── airflow.cfg.bak
│   ├── airflow.db
│   ├── dags
│   │   └── load_data_dag.py
│   └── webserver_config.py
├── app
│   ├── api
│   │   └── api_v1
│   │       ├── api.py
│   │       └── endpoints
│   │           ├── callback.py
│   │           ├── display_token.py
│   │           ├── get_data.py
│   │           ├── home.py
│   │           ├── load_data.py
│   │           └── set_token.py
│   ├── core
│   │   ├── auth.py
│   │   └── config.py.changeme
│   ├── database.py
│   ├── services
│   │   ├── snowflake_service.py
│   │   └── stackexchange_service.py
│   ├── tasks
│   │   └── load_data_task.py
│   └── templates
│       ├── callback.html
│       ├── display_token.html
│       └── index.html
├── dbt_se
│   ├── README.md
│   ├── analyses
│   ├── dbt_project.yml
│   ├── macros
│   ├── models
│   │   ├── calculation
│   │   │   ├── calculation_daily_tags.sql
│   │   │   ├── calculation_daily_tags.yml
│   │   │   └── calculation_weekly_tags_change.sql
│   │   ├── consumption
│   │   │   ├── consumption_daily_tags.sql
│   │   │   └── consumption_weekly_tags_change.sql
│   │   ├── curation
│   │   │   └── curation_tags.sql
│   │   └── ingestion
│   │       └── sources.yml
│   ├── seeds
│   ├── snapshots
│   └── tests
├── main.py
└── superset_se
    ├── superset.db
    └── superset_config.py

23 directories, 35 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                            | Summary                                                                                                                             |
| ---                                                                                             | ---                                                                                                                                 |
| [main.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/main.py) | The code snippet creates a FastAPI application and includes a router for version 1 of the API, accessible via the "/api/v1" prefix. |

</details>

<details closed><summary>App</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                  |
| ---                                                                                                         | ---                                                                                                                                                                                                                      |
| [database.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/database.py) | This code snippet connects to a Snowflake database using SQLAlchemy and creates a session to interact with the database. It provides a function get_db() to obtain a database session, ensuring proper session handling. |

</details>

<details closed><summary>Tasks</summary>

| File                                                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [load_data_task.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/tasks/load_data_task.py) | The code snippet performs the following:1. It imports the necessary modules for the StackExchange and Snowflake services.2. It defines a DataLoader class with a static method, load_data.3. Within the load_data method, it calls the StackExchangeService to scrape data asynchronously.4. It calls the SnowflakeService to insert data from a CSV file.5. It checks if the CSV file exists and deletes it if it does.6. Finally, it runs the load_data method using asyncio.Overall, the code loads data from StackExchange, inserts it into Snowflake, and deletes the CSV file if it exists. |

</details>

<details closed><summary>Core</summary>

| File                                                                                                                           | Summary                                                                                                                                                                                                         |
| ---                                                                                                                            | ---                                                                                                                                                                                                             |
| [auth.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/core/auth.py)                       | The code snippet defines an async function authenticate(). It constructs an authorization URL using authorization_base_url, client_id, redirect_uri, and scope parameters, then returns the URL.                |
| [config.py.changeme](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/core/config.py.changeme) | The code snippet provides variables for configuration settings such as client details, OAuth endpoints, redirect URIs, and Snowflake database credentials. It also enables client-side and desktop OAuth flows. |

</details>

<details closed><summary>Api_v1</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                              |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                                                  |
| [api.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/api.py) | The provided code snippet creates an API router using FastAPI. It includes several routers for different endpoints such as home, callback, set_token, display_token, load_data, and get_data. Each router is associated with specific tags for easy categorization and organization. |

</details>

<details closed><summary>Endpoints</summary>

| File                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                        | ---                                                                                                                                                                                                                                                                                         |
| [callback.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/callback.py)           | The provided code snippet is using the FastAPI framework to create an API endpoint ("/auth-callback") that returns a Jinja2 template response ("callback.html") with the HTTP request object as context.                                                                                    |
| [home.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/home.py)                   | This code snippet creates an API router using FastAPI. It provides a home route that renders an HTML template, passing the request object and an authentication URL.                                                                                                                        |
| [set_token.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/set_token.py)         | This code snippet defines an API route using FastAPI framework. It accepts a POST request to set a token value, which is received as input in the request body. The token value is then written to a file called "token.txt". Finally, a JSON response is returned with a success message.  |
| [get_data.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/get_data.py)           | The code snippet defines an API router for a FastAPI application. It reads an encrypted access token from a file, checks its availability, and makes a GET request to an external API using the access token as authorization. The response from the external API is returned as JSON data. |
| [load_data.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/load_data.py)         | This code snippet defines an API endpoint ("/load-data") that triggers the loading of data using a DataLoader class. It returns a JSON response indicating that the data loading process is in progress.                                                                                    |
| [display_token.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/display_token.py) | This code snippet defines an API endpoint "/display-token" that takes a "token" parameter. It returns an HTML template "display_token.html" with the token value displayed. The Jinja2Templates library is used for rendering the template.                                                 |

</details>

<details closed><summary>Templates</summary>

| File                                                                                                                                | Summary                                                                                                                                                                                                                   |
| ---                                                                                                                                 | ---                                                                                                                                                                                                                       |
| [index.html](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/templates/index.html)                 | The code snippet is a basic web page that allows users to authenticate, load data, and display tags. It uses JavaScript to make HTTP requests and update the page dynamically.                                            |
| [callback.html](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/templates/callback.html)           | This code snippet parses the access token from the URL fragment, sends it to a server endpoint using a POST request, and redirects the user to a new page to display the token if the request is successful.              |
| [display_token.html](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/templates/display_token.html) | This code snippet is an HTML template that displays an access token if it exists. If the token exists, it is printed in a paragraph. If the token doesn't exist, a message stating "Access Token not found" is displayed. |

</details>

<details closed><summary>Services</summary>

| File                                                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                            | ---                                                                                                                                                                                                                                                                                                                            |
| [stackexchange_service.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/services/stackexchange_service.py) | This code snippet is a part of a web scraping service for Stack Exchange. It uses HTTPX for making requests, AIOMeter for concurrent scraping, and CSV for storing scraped data. It retrieves tag information from the Stack Exchange API, writes it to a CSV file, and continues scraping until there are no more pages left. |
| [snowflake_service.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/services/snowflake_service.py)         | The code snippet connects to a Snowflake database using provided credentials and inserts CSV data into a table called "tags" in chunks of 10,000 rows at a time. The data is mapped to columns "name", "count", and "ingestion_timestamp".                                                                                     |

</details>

<details closed><summary>Airflow</summary>

| File                                                                                                                                | Summary                                                                                                                                                                                                                                                |
| ---                                                                                                                                 | ---                                                                                                                                                                                                                                                    |
| [airflow-webserver.pid](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/airflow/airflow-webserver.pid) | The provided code snippet performs an operation to multiply two given numbers together and returns the result.                                                                                                                                         |
| [webserver_config.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/airflow/webserver_config.py)     | This code snippet contains the default configuration settings for the Airflow webserver. It includes options for authentication, such as database, LDAP, OAuth, and OpenID. It also provides settings for theme customization using predefined themes. |

</details>

<details closed><summary>Dags</summary>

| File                                                                                                                           | Summary                                                                                                                                                                                             |
| ---                                                                                                                            | ---                                                                                                                                                                                                 |
| [load_data_dag.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/airflow/dags/load_data_dag.py) | This code snippet sets up an Airflow DAG for an ELT pipeline. It includes tasks for API extraction, DBT transformations, and consumption. The tasks are connected in sequence to form the pipeline. |

</details>

<details closed><summary>Curation</summary>

| File                                                                                                                                       | Summary                                                                                                                                                                                                    |
| ---                                                                                                                                        | ---                                                                                                                                                                                                        |
| [curation_tags.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/curation/curation_tags.sql) | The code snippet retrieves data from a source table called'tags' and converts some columns to specific data types. It then selects the tag name, count, and ingestion timestamp from the transformed data. |

</details>

<details closed><summary>Consumption</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                   |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                       |
| [consumption_weekly_tags_change.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/consumption/consumption_weekly_tags_change.sql) | This code snippet selects all data from the "calculation_weekly_tags_change" view in the "consumption" schema and aliases it as "weekly_tags_change". It is configured as a materialized view with the tag "consumption". |
| [consumption_daily_tags.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/consumption/consumption_daily_tags.sql)                 | This code snippet creates a view with the alias "daily_tags" in the "consumption" schema. The view selects all columns from the "calculation_daily_tags" table.                                                           |

</details>

<details closed><summary>Calculation</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                      |
| [calculation_weekly_tags_change.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/calculation/calculation_weekly_tags_change.sql) | The provided code snippet retrieves the weekly change in tag counts by subtracting the minimum daily count from the maximum daily count for each tag. It calculates the daily tag count by summing the daily counts for each tag. The query filters the data based on the load date within the past 7 days. The result is then grouped by tag name and ordered by the weekly change in descending order. |
| [calculation_daily_tags.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/calculation/calculation_daily_tags.sql)                 | The code snippet defines a table configuration and then performs a query on a base table. The base table is derived from another table called'curation_tags'. The query groups the data by load date and tag name, calculates the maximum tag count per day, and sorts the results.                                                                                                                      |

</details>

<details closed><summary>Superset_se</summary>

| File                                                                                                                              | Summary                                                                                                                                                                                                            |
| ---                                                                                                                               | ---                                                                                                                                                                                                                |
| [superset_config.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/superset_se/superset_config.py) | This code snippet sets the specific configurations for Superset, a data visualization and exploration platform. It includes settings for row limit, secret key, database URI, CSRF protection, and Mapbox API key. |

</details>

---

## 🚀 Getting Started

### 📦 Installation

1. Clone the StackExchange_API_PKT_V2 repository:
```sh
git clone https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git
```

2. Change to the project directory:
```sh
cd StackExchange_API_PKT_V2
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using StackExchange_API_PKT_V2

1. In app/core folder, change the python name from config.py.ignore to config.py
2. Add the specified required credentials
3. Run the Flask API webserver using 
```sh  
uvicorn main:app
```
4. In your browser goto localhost:8000/api/v1 and click on Authenticate. if you have set the Stack exchange API credentials right in the config.py file, this would generated a token.txt in the root folder.
5. To test the ingestion of data to snowflake go back to localhost/api/v1 and press  load data button to load the data in snowflake. (Note: you need to have the schema specified in config.py in snowflake along with the access privilege)
6. Install dbt on your system and use dbt run to run the transformation models.
7. Ensure that you have data in dbt_consumption schema in snowflake.
8. Now, cd into airflow and create a new venv for isolation. Install airflow using pip and follow the process to get the dag working, the dag is scheduled to run once daily.
9. Now, create another virtualenv in superset_se folder for apache superset and install it your virtual environment. 
10. Create your desired dashboards with charts.


---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---
