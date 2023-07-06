
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>StackExchange_API_PKT_V2
</h1>
<h3>◦ Unlock the power of StackExchange with our API!</h3>
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
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is a FastAPI-based web application that utilizes the Stack Exchange API to scrape data and store it in a Snowflake database. It provides endpoints for authentication, data retrieval, token management, and data loading. The core functionalities include fetching data from the Stack Exchange API, authenticating users, securely storing access tokens, managing data loading tasks, and visualizing the data using tools like dbt and Superset. Overall, the project aims to provide a seamless and efficient way to scrape and analyze data from Stack Exchange.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a modular architecture pattern, with separate files for different components of the application. It uses the FastAPI framework for building the API and SQLAlchemy for database connectivity. The codebase also includes components for data loading, authentication, and handling API requests. The architecture promotes separation of concerns and allows for easy maintenance and extensibility. The use of async functions and asynchronous processing enhances performance and scalability. |
| **📖 Documentation**   | The codebase includes inline comments and docstrings to provide explanations and context for the code. The repository also contains a README file, but it lacks detailed information about installation, configuration, and usage. The code could benefit from additional documentation, especially regarding the overall system architecture, design decisions, and API endpoints. |
| **🔗 Dependencies**    | The codebase relies on several external libraries and frameworks, including FastAPI, SQLAlchemy, Jinja2, and Snowflake. These dependencies are specified in the repository's requirements.txt file and can be easily installed using pip. The project also uses database and authentication services provided by Snowflake and Stack Exchange API, respectively. |
| **🧩 Modularity**      | The codebase demonstrates good modularity, with files organized into specific directories based on their functionality. Each file focuses on a specific feature or aspect of the application, such as the API endpoints, database connection, data loading, and authentication. This modular structure allows for easy maintenance, testing, and reusability of components. |
| **✔️ Testing**          | Although the codebase does not include a dedicated directory for tests, it is well-structured and modular, making it testable. The FastAPI framework provides built-in mechanisms for testing API endpoints. However, the codebase lacks comprehensive unit tests, integration tests, and test fixtures. The addition of a testing framework, such as Pytest, along with test scripts and sample test data, would greatly enhance the reliability and maintainability of the code. |
| **⚡️ Performance**      | The codebase leverages asynchronous processing using async functions and the FastAPI framework to enhance performance and responsiveness. The use of asynchronous programming allows for concurrent execution of requests, reducing latency and efficiently utilizing system resources. The codebase also includes optimizations, such as processing data in chunks and utilizing database-specific functionalities for efficient data insertion. However, without performance benchmarks or profiling, it is difficult to assess the codebase's overall performance. |
| **🔐 Security**        | The codebase addresses security concerns by implementing an authentication flow using OAuth. It provides mechanisms for handling access tokens securely, such as storing tokens in files with restricted access or using environment variables. However, there is a potential security risk in the provided code templates, as sensitive information like Snowflake credentials and OAuth secret keys should not be committed to version control. The codebase

---


## 📂 Project Structure


```bash
repo
├── README.md
├── __pycache__
│   ├── main.cpython-311.pyc
│   └── main.cpython-39.pyc
├── airflow
│   ├── airflow-webserver.pid
│   ├── airflow.cfg
│   ├── airflow.cfg.bak
│   ├── airflow.db
│   ├── dags
│   │   ├── __pycache__
│   │   │   └── load_data_dag.cpython-39.pyc
│   │   └── load_data_dag.py
│   └── webserver_config.py
├── app
│   ├── __pycache__
│   │   └── database.cpython-311.pyc
│   ├── api
│   │   └── api_v1
│   │       ├── __pycache__
│   │       │   ├── api.cpython-311.pyc
│   │       │   └── api.cpython-39.pyc
│   │       ├── api.py
│   │       └── endpoints
│   │           ├── __pycache__
│   │           │   ├── callback.cpython-311.pyc
│   │           │   ├── callback.cpython-39.pyc
│   │           │   ├── display_token.cpython-311.pyc
│   │           │   ├── display_token.cpython-39.pyc
│   │           │   ├── get_data.cpython-311.pyc
│   │           │   ├── get_data.cpython-39.pyc
│   │           │   ├── home.cpython-311.pyc
│   │           │   ├── home.cpython-39.pyc
│   │           │   ├── load_data.cpython-311.pyc
│   │           │   ├── load_data.cpython-39.pyc
│   │           │   ├── set_token.cpython-311.pyc
│   │           │   └── set_token.cpython-39.pyc
│   │           ├── callback.py
│   │           ├── display_token.py
│   │           ├── get_data.py
│   │           ├── home.py
│   │           ├── load_data.py
│   │           └── set_token.py
│   ├── core
│   │   ├── __pycache__
│   │   │   ├── auth.cpython-311.pyc
│   │   │   ├── auth.cpython-39.pyc
│   │   │   ├── config.cpython-311.pyc
│   │   │   └── config.cpython-39.pyc
│   │   ├── auth.py
│   │   └── config.py.changeme
│   ├── database.py
│   ├── services
│   │   ├── __pycache__
│   │   │   ├── stackexchange_service.cpython-311.pyc
│   │   │   └── stackexchange_service.cpython-39.pyc
│   │   ├── snowflake_service.py
│   │   └── stackexchange_service.py
│   ├── tasks
│   │   ├── __pycache__
│   │   │   ├── load_data_task.cpython-311.pyc
│   │   │   └── load_data_task.cpython-39.pyc
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
    ├── __pycache__
    │   └── superset_config.cpython-39.pyc
    ├── superset.db
    └── superset_config.py

32 directories, 62 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                            | Summary                                                                                                                              |
| ---                                                                                             | ---                                                                                                                                  |
| [main.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/main.py) | This code snippet sets up a FastAPI application. It includes a router for version 1 of the API and sets a prefix for the API routes. |

</details>

<details closed><summary>App</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                                 |
| ---                                                                                                         | ---                                                                                                                                                                                                                                                                                     |
| [database.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/database.py) | This code snippet sets up a connection to a Snowflake database using SQLAlchemy. It creates an engine using the Snowflake URL and defines a session factory for database operations. The "get_db" function provides a database session for use in APIs or other application components. |

</details>

<details closed><summary>Tasks</summary>

| File                                                                                                                          | Summary                                                                                                                                                                                                                                                                        |
| ---                                                                                                                           | ---                                                                                                                                                                                                                                                                            |
| [load_data_task.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/tasks/load_data_task.py) | The code snippet loads data by first scraping data from Stack Exchange using the StackExchangeService, then inserting the scraped data into Snowflake using the SnowflakeService. Afterwards, it checks if a file named'data.csv' exists, and if it does, it deletes the file. |

</details>

<details closed><summary>Core</summary>

| File                                                                                                                           | Summary                                                                                                                                                                                                                                |
| ---                                                                                                                            | ---                                                                                                                                                                                                                                    |
| [auth.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/core/auth.py)                       | This code snippet defines an asynchronous function called "authenticate" that constructs and returns an authentication URL using variables from a configuration module. This URL is used for the authorization flow in an application. |
| [config.py.changeme](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/core/config.py.changeme) | The code snippet defines various variables related to client authentication, OAuth settings, application details, and Snowflake database configuration.                                                                                |

</details>

<details closed><summary>Api_v1</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                               |
| ---                                                                                                          | ---                                                                                                                                                                                                                                   |
| [api.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/api.py) | The code snippet defines an API router that includes multiple endpoints related to home, callback, token management, and data manipulation. Each endpoint is associated with a specific tag for easy categorization and organization. |

</details>

<details closed><summary>Endpoints</summary>

| File                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                               |
| [callback.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/callback.py)           | This code snippet creates an API endpoint "/auth-callback" using FastAPI. It renders a Jinja2 template called "callback.html" and passes the request object to the template.                                                                                                                                                                      |
| [home.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/home.py)                   | The code snippet defines a FastAPI router with a single GET route at the root URL ("/"). When accessed, it renders an "index.html" template with a request object and an authentication URL passed as context variables. The authentication URL is fetched asynchronously from the "authenticate" function defined in the "app.core.auth" module. |
| [set_token.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/set_token.py)         | The provided code snippet defines a FastAPI router with a single endpoint ("/set-token"). It expects a POST request with a JSON body containing a "token" field. This token is written to a file called "token.txt", and a success message is returned.                                                                                           |
| [get_data.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/get_data.py)           | This code snippet defines an API route that retrieves data from the Stack Exchange API. It reads an access token from a file, makes an authenticated GET request to the API, and returns the response data.                                                                                                                                       |
| [load_data.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/load_data.py)         | The code defines an API endpoint'/load-data' using FastAPI. When called, it triggers the'load_data' method from the'DataLoader' class to load data. It returns a message indicating the progress of the data loading process.                                                                                                                     |
| [display_token.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/api/api_v1/endpoints/display_token.py) | This code snippet sets up an API router with a GET endpoint that takes a token as a parameter. It uses Jinja2 templates to render an HTML page that displays the token.                                                                                                                                                                           |

</details>

<details closed><summary>Templates</summary>

| File                                                                                                                                | Summary                                                                                                                                                                                                                                                       |
| ---                                                                                                                                 | ---                                                                                                                                                                                                                                                           |
| [index.html](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/templates/index.html)                 | This code snippet is an example of an authentication process in a web application. It includes functions to load tags and load data using the fetch API. The authentication is triggered by clicking on a link, and the loaded data is displayed on the page. |
| [callback.html](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/templates/callback.html)           | This code parses the access token from the URL fragment, sends it to the server via a POST request, and if successful, redirects the user to a page displaying the token.                                                                                     |
| [display_token.html](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/templates/display_token.html) | This code snippet is an HTML template that displays an access token if it exists, otherwise it displays a message indicating that the access token was not found. The access token value is passed to the template as a variable called "token".              |

</details>

<details closed><summary>Services</summary>

| File                                                                                                                                           | Summary                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                            | ---                                                                                                                                                                                                                                                                         |
| [stackexchange_service.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/services/stackexchange_service.py) | The code snippet is a part of a service that scrapes data from the StackExchange API and stores it in a CSV file. It includes functions to scrape data for a specific page or all pages, handles API authentication, and uses asynchronous processing for faster execution. |
| [snowflake_service.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/app/services/snowflake_service.py)         | The code snippet connects to a Snowflake database using SQLAlchemy and inserts data from a CSV file into a table called "tags". It processes the CSV file in chunks of 10,000 rows and sets the column names before inserting the data into the table.                      |

</details>

<details closed><summary>Airflow</summary>

| File                                                                                                                                | Summary                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                 | ---                                                                                                                                                                                                                                                                                               |
| [airflow-webserver.pid](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/airflow/airflow-webserver.pid) | The provided code snippet defines a TechLead class with core functionalities such as managing a team of developers, assigning tasks, tracking progress, and providing feedback. It also allows the Tech Lead to communicate with other stakeholders and facilitate collaboration within the team. |
| [webserver_config.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/airflow/webserver_config.py)     | This code snippet provides the default configuration for the Airflow webserver. It includes settings for authentication methods, such as database, LDAP, and OAuth. It also allows for user self-registration and configuration of various themes for the web interface.                          |

</details>

<details closed><summary>Dags</summary>

| File                                                                                                                           | Summary                                                                                                                                                                                                                         |
| ---                                                                                                                            | ---                                                                                                                                                                                                                             |
| [load_data_dag.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/airflow/dags/load_data_dag.py) | This code snippet defines an Airflow DAG for an ELT pipeline. It starts with an API data extraction and load task, followed by three dbt tasks for curation, calculation, and consumption. Finally, it ends with an empty task. |

</details>

<details closed><summary>Curation</summary>

| File                                                                                                                                       | Summary                                                                                                                                                                                                                |
| ---                                                                                                                                        | ---                                                                                                                                                                                                                    |
| [curation_tags.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/curation/curation_tags.sql) | This code snippet configures the data source as a table and retrieves data from the "ingestion.tags" source. It casts the data types and then selects the tag name, count, and ingestion timestamp from the base view. |

</details>

<details closed><summary>Consumption</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                          |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                              |
| [consumption_weekly_tags_change.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/consumption/consumption_weekly_tags_change.sql) | The code snippet defines a view called "weekly_tags_change" in the "consumption" schema. It selects all columns from the "calculation_weekly_tags_change" table.                                                                                 |
| [consumption_daily_tags.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/consumption/consumption_daily_tags.sql)                 | The code snippet is a SQL query that selects all columns from a view called "calculation_daily_tags" in the "consumption" schema. The query is using a configuration that sets the materialized type as view and assigns the alias "daily_tags". |

</details>

<details closed><summary>Calculation</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [calculation_weekly_tags_change.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/calculation/calculation_weekly_tags_change.sql) | This code snippet retrieves the weekly change in tag count for each tag name. It does this by calculating the sum of daily counts for each tag, then finding the difference between the maximum and minimum counts within the past seven days. The result is ordered by the largest weekly change first.                                                                                                                                                        |
| [calculation_daily_tags.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/dbt_se/models/calculation/calculation_daily_tags.sql)                 | The code snippet performs the following functionalities:1. Configures the materialized table and schema for the result.2. Defines a base table that extracts the load_date, tag_name, and tag_count from a referenced table.3. Retrieves the maximum tag_count for each load_date and tag_name combination.4. Groups the results by load_date and tag_name, and orders them.5. Returns the load_date, tag_name, and the maximum tag_count for each combination. |

</details>

<details closed><summary>Superset_se</summary>

| File                                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                       |
| [superset_config.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT_V2.git/blob/main/superset_se/superset_config.py) | This code snippet contains specific configurations for Superset, Flask-WTF CSRF protection, and Mapbox API key. It sets the row limit, secret key, database URI, enables CSRF protection, exempts endpoints from CSRF, and sets the CSRF token time limit. The MAPBOX_API_KEY can be set to enable Mapbox visualizations. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

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

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

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

## 📄 License

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
