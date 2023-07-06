
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>StackExchange_API_PKT
</h1>
<h3>◦ </h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/ShubhamPriyadarshi/StackExchange_API_PKT?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/ShubhamPriyadarshi/StackExchange_API_PKT?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/ShubhamPriyadarshi/StackExchange_API_PKT?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/ShubhamPriyadarshi/StackExchange_API_PKT?style&color=5D6D7E" alt="GitHub license" />
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



---

## ⚙️ Features



---


## 📂 Project Structure


```bash
repo
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
│   ├── logs
│   │   ├── dag_id=load_data_dag
│   │   │   ├── run_id=manual__2023-07-02T15:30:36.132059+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-02T15:42:22.363032+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       ├── attempt=1.log
│   │   │   │       └── attempt=2.log
│   │   │   ├── run_id=manual__2023-07-02T15:45:54.142264+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       ├── attempt=1.log
│   │   │   │       └── attempt=2.log
│   │   │   ├── run_id=manual__2023-07-02T15:57:21.920666+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       ├── attempt=1.log
│   │   │   │       ├── attempt=2.log
│   │   │   │       └── attempt=3.log
│   │   │   ├── run_id=manual__2023-07-02T16:07:10.585978+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-02T16:09:14.158663+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-02T16:11:42.310489+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-02T16:14:00.400287+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-02T16:15:53.761785+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       ├── attempt=1.log
│   │   │   │       └── attempt=2.log
│   │   │   ├── run_id=manual__2023-07-02T16:36:31.018999+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-02T20:45:02.552085+00:00
│   │   │   │   └── task_id=run_etl
│   │   │   │       └── attempt=1.log
│   │   │   └── run_id=scheduled__2023-07-02T00:00:00+00:00
│   │   │       └── task_id=run_etl
│   │   │           └── attempt=1.log
│   │   ├── dag_id=stackexchange_elt
│   │   │   ├── run_id=manual__2023-07-04T15:50:49.010236+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   └── attempt=1.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       ├── attempt=1.log
│   │   │   │       └── attempt=2.log
│   │   │   ├── run_id=manual__2023-07-04T15:55:44.311095+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   └── attempt=1.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       ├── attempt=1.log
│   │   │   │       └── attempt=2.log
│   │   │   ├── run_id=manual__2023-07-04T16:05:30.328585+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_calculation
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_consumption
│   │   │   │   │   └── attempt=1.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-05T12:13:11.144301+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_calculation
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_consumption
│   │   │   │   │   └── attempt=1.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-05T12:19:19.316881+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_calculation
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_consumption
│   │   │   │   │   └── attempt=1.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-05T12:21:58.442497+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_calculation
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_consumption
│   │   │   │   │   └── attempt=1.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=manual__2023-07-05T12:23:11.700312+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_calculation
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_consumption
│   │   │   │   │   └── attempt=1.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       └── attempt=1.log
│   │   │   ├── run_id=scheduled__2023-07-02T00:00:00+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   ├── attempt=1.log
│   │   │   │   │   └── attempt=2.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       ├── attempt=1.log
│   │   │   │       └── attempt=2.log
│   │   │   ├── run_id=scheduled__2023-07-03T00:00:00+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   ├── attempt=1.log
│   │   │   │   │   └── attempt=2.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       ├── attempt=1.log
│   │   │   │       └── attempt=2.log
│   │   │   ├── run_id=scheduled__2023-07-04T00:00:00+00:00
│   │   │   │   ├── task_id=api_extract_load
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_calculation
│   │   │   │   │   └── attempt=1.log
│   │   │   │   ├── task_id=dbt_consumption
│   │   │   │   │   └── attempt=1.log
│   │   │   │   └── task_id=dbt_curation
│   │   │   │       └── attempt=1.log
│   │   │   └── run_id=scheduled__2023-07-05T00:00:00+00:00
│   │   │       ├── task_id=api_extract_load
│   │   │       │   └── attempt=1.log
│   │   │       ├── task_id=dbt_calculation
│   │   │       │   └── attempt=1.log
│   │   │       ├── task_id=dbt_consumption
│   │   │       │   └── attempt=1.log
│   │   │       └── task_id=dbt_curation
│   │   │           └── attempt=1.log
│   │   ├── dag_processor_manager
│   │   │   └── dag_processor_manager.log
│   │   └── scheduler
│   │       ├── 2023-07-02
│   │       │   ├── load_data_dag.py.log
│   │       │   └── native_dags
│   │       │       └── example_dags
│   │       │           ├── example_bash_operator.py.log
│   │       │           ├── example_branch_datetime_operator.py.log
│   │       │           ├── example_branch_day_of_week_operator.py.log
│   │       │           ├── example_branch_labels.py.log
│   │       │           ├── example_branch_operator.py.log
│   │       │           ├── example_branch_operator_decorator.py.log
│   │       │           ├── example_branch_python_dop_operator_3.py.log
│   │       │           ├── example_complex.py.log
│   │       │           ├── example_dag_decorator.py.log
│   │       │           ├── example_datasets.py.log
│   │       │           ├── example_dynamic_task_mapping.py.log
│   │       │           ├── example_dynamic_task_mapping_with_no_taskflow_operators.py.log
│   │       │           ├── example_external_task_marker_dag.py.log
│   │       │           ├── example_kubernetes_executor.py.log
│   │       │           ├── example_latest_only.py.log
│   │       │           ├── example_latest_only_with_trigger.py.log
│   │       │           ├── example_local_kubernetes_executor.py.log
│   │       │           ├── example_nested_branch_dag.py.log
│   │       │           ├── example_params_trigger_ui.py.log
│   │       │           ├── example_params_ui_tutorial.py.log
│   │       │           ├── example_passing_params_via_test_command.py.log
│   │       │           ├── example_python_operator.py.log
│   │       │           ├── example_sensor_decorator.py.log
│   │       │           ├── example_sensors.py.log
│   │       │           ├── example_setup_teardown.py.log
│   │       │           ├── example_setup_teardown_taskflow.py.log
│   │       │           ├── example_short_circuit_decorator.py.log
│   │       │           ├── example_short_circuit_operator.py.log
│   │       │           ├── example_skip_dag.py.log
│   │       │           ├── example_sla_dag.py.log
│   │       │           ├── example_subdag_operator.py.log
│   │       │           ├── example_task_group.py.log
│   │       │           ├── example_task_group_decorator.py.log
│   │       │           ├── example_time_delta_sensor_async.py.log
│   │       │           ├── example_trigger_controller_dag.py.log
│   │       │           ├── example_trigger_target_dag.py.log
│   │       │           ├── example_xcom.py.log
│   │       │           ├── example_xcomargs.py.log
│   │       │           ├── plugins
│   │       │           │   ├── event_listener.py.log
│   │       │           │   ├── listener_plugin.py.log
│   │       │           │   └── workday.py.log
│   │       │           ├── subdags
│   │       │           │   └── subdag.py.log
│   │       │           ├── tutorial.py.log
│   │       │           ├── tutorial_dag.py.log
│   │       │           ├── tutorial_taskflow_api.py.log
│   │       │           └── tutorial_taskflow_api_virtualenv.py.log
│   │       ├── 2023-07-03
│   │       │   ├── load_data_dag.py.log
│   │       │   └── native_dags
│   │       │       └── example_dags
│   │       │           ├── example_bash_operator.py.log
│   │       │           ├── example_branch_datetime_operator.py.log
│   │       │           ├── example_branch_day_of_week_operator.py.log
│   │       │           ├── example_branch_labels.py.log
│   │       │           ├── example_branch_operator.py.log
│   │       │           ├── example_branch_operator_decorator.py.log
│   │       │           ├── example_branch_python_dop_operator_3.py.log
│   │       │           ├── example_complex.py.log
│   │       │           ├── example_dag_decorator.py.log
│   │       │           ├── example_datasets.py.log
│   │       │           ├── example_dynamic_task_mapping.py.log
│   │       │           ├── example_dynamic_task_mapping_with_no_taskflow_operators.py.log
│   │       │           ├── example_external_task_marker_dag.py.log
│   │       │           ├── example_kubernetes_executor.py.log
│   │       │           ├── example_latest_only.py.log
│   │       │           ├── example_latest_only_with_trigger.py.log
│   │       │           ├── example_local_kubernetes_executor.py.log
│   │       │           ├── example_nested_branch_dag.py.log
│   │       │           ├── example_params_trigger_ui.py.log
│   │       │           ├── example_params_ui_tutorial.py.log
│   │       │           ├── example_passing_params_via_test_command.py.log
│   │       │           ├── example_python_operator.py.log
│   │       │           ├── example_sensor_decorator.py.log
│   │       │           ├── example_sensors.py.log
│   │       │           ├── example_setup_teardown.py.log
│   │       │           ├── example_setup_teardown_taskflow.py.log
│   │       │           ├── example_short_circuit_decorator.py.log
│   │       │           ├── example_short_circuit_operator.py.log
│   │       │           ├── example_skip_dag.py.log
│   │       │           ├── example_sla_dag.py.log
│   │       │           ├── example_subdag_operator.py.log
│   │       │           ├── example_task_group.py.log
│   │       │           ├── example_task_group_decorator.py.log
│   │       │           ├── example_time_delta_sensor_async.py.log
│   │       │           ├── example_trigger_controller_dag.py.log
│   │       │           ├── example_trigger_target_dag.py.log
│   │       │           ├── example_xcom.py.log
│   │       │           ├── example_xcomargs.py.log
│   │       │           ├── plugins
│   │       │           │   ├── event_listener.py.log
│   │       │           │   ├── listener_plugin.py.log
│   │       │           │   └── workday.py.log
│   │       │           ├── subdags
│   │       │           │   └── subdag.py.log
│   │       │           ├── tutorial.py.log
│   │       │           ├── tutorial_dag.py.log
│   │       │           ├── tutorial_taskflow_api.py.log
│   │       │           └── tutorial_taskflow_api_virtualenv.py.log
│   │       ├── 2023-07-04
│   │       │   ├── load_data_dag.py.log
│   │       │   └── native_dags
│   │       │       └── example_dags
│   │       │           ├── example_bash_operator.py.log
│   │       │           ├── example_branch_datetime_operator.py.log
│   │       │           ├── example_branch_day_of_week_operator.py.log
│   │       │           ├── example_branch_labels.py.log
│   │       │           ├── example_branch_operator.py.log
│   │       │           ├── example_branch_operator_decorator.py.log
│   │       │           ├── example_branch_python_dop_operator_3.py.log
│   │       │           ├── example_complex.py.log
│   │       │           ├── example_dag_decorator.py.log
│   │       │           ├── example_datasets.py.log
│   │       │           ├── example_dynamic_task_mapping.py.log
│   │       │           ├── example_dynamic_task_mapping_with_no_taskflow_operators.py.log
│   │       │           ├── example_external_task_marker_dag.py.log
│   │       │           ├── example_kubernetes_executor.py.log
│   │       │           ├── example_latest_only.py.log
│   │       │           ├── example_latest_only_with_trigger.py.log
│   │       │           ├── example_local_kubernetes_executor.py.log
│   │       │           ├── example_nested_branch_dag.py.log
│   │       │           ├── example_params_trigger_ui.py.log
│   │       │           ├── example_params_ui_tutorial.py.log
│   │       │           ├── example_passing_params_via_test_command.py.log
│   │       │           ├── example_python_operator.py.log
│   │       │           ├── example_sensor_decorator.py.log
│   │       │           ├── example_sensors.py.log
│   │       │           ├── example_setup_teardown.py.log
│   │       │           ├── example_setup_teardown_taskflow.py.log
│   │       │           ├── example_short_circuit_decorator.py.log
│   │       │           ├── example_short_circuit_operator.py.log
│   │       │           ├── example_skip_dag.py.log
│   │       │           ├── example_sla_dag.py.log
│   │       │           ├── example_subdag_operator.py.log
│   │       │           ├── example_task_group.py.log
│   │       │           ├── example_task_group_decorator.py.log
│   │       │           ├── example_time_delta_sensor_async.py.log
│   │       │           ├── example_trigger_controller_dag.py.log
│   │       │           ├── example_trigger_target_dag.py.log
│   │       │           ├── example_xcom.py.log
│   │       │           ├── example_xcomargs.py.log
│   │       │           ├── plugins
│   │       │           │   ├── event_listener.py.log
│   │       │           │   ├── listener_plugin.py.log
│   │       │           │   └── workday.py.log
│   │       │           ├── subdags
│   │       │           │   └── subdag.py.log
│   │       │           ├── tutorial.py.log
│   │       │           ├── tutorial_dag.py.log
│   │       │           ├── tutorial_taskflow_api.py.log
│   │       │           └── tutorial_taskflow_api_virtualenv.py.log
│   │       ├── 2023-07-05
│   │       │   ├── load_data_dag.py.log
│   │       │   └── native_dags
│   │       │       └── example_dags
│   │       │           ├── example_bash_operator.py.log
│   │       │           ├── example_branch_datetime_operator.py.log
│   │       │           ├── example_branch_day_of_week_operator.py.log
│   │       │           ├── example_branch_labels.py.log
│   │       │           ├── example_branch_operator.py.log
│   │       │           ├── example_branch_operator_decorator.py.log
│   │       │           ├── example_branch_python_dop_operator_3.py.log
│   │       │           ├── example_complex.py.log
│   │       │           ├── example_dag_decorator.py.log
│   │       │           ├── example_datasets.py.log
│   │       │           ├── example_dynamic_task_mapping.py.log
│   │       │           ├── example_dynamic_task_mapping_with_no_taskflow_operators.py.log
│   │       │           ├── example_external_task_marker_dag.py.log
│   │       │           ├── example_kubernetes_executor.py.log
│   │       │           ├── example_latest_only.py.log
│   │       │           ├── example_latest_only_with_trigger.py.log
│   │       │           ├── example_local_kubernetes_executor.py.log
│   │       │           ├── example_nested_branch_dag.py.log
│   │       │           ├── example_params_trigger_ui.py.log
│   │       │           ├── example_params_ui_tutorial.py.log
│   │       │           ├── example_passing_params_via_test_command.py.log
│   │       │           ├── example_python_operator.py.log
│   │       │           ├── example_sensor_decorator.py.log
│   │       │           ├── example_sensors.py.log
│   │       │           ├── example_setup_teardown.py.log
│   │       │           ├── example_setup_teardown_taskflow.py.log
│   │       │           ├── example_short_circuit_decorator.py.log
│   │       │           ├── example_short_circuit_operator.py.log
│   │       │           ├── example_skip_dag.py.log
│   │       │           ├── example_sla_dag.py.log
│   │       │           ├── example_subdag_operator.py.log
│   │       │           ├── example_task_group.py.log
│   │       │           ├── example_task_group_decorator.py.log
│   │       │           ├── example_time_delta_sensor_async.py.log
│   │       │           ├── example_trigger_controller_dag.py.log
│   │       │           ├── example_trigger_target_dag.py.log
│   │       │           ├── example_xcom.py.log
│   │       │           ├── example_xcomargs.py.log
│   │       │           ├── plugins
│   │       │           │   ├── event_listener.py.log
│   │       │           │   ├── listener_plugin.py.log
│   │       │           │   └── workday.py.log
│   │       │           ├── subdags
│   │       │           │   └── subdag.py.log
│   │       │           ├── tutorial.py.log
│   │       │           ├── tutorial_dag.py.log
│   │       │           ├── tutorial_taskflow_api.py.log
│   │       │           └── tutorial_taskflow_api_virtualenv.py.log
│   │       ├── 2023-07-06
│   │       │   ├── load_data_dag.py.log
│   │       │   └── native_dags
│   │       │       └── example_dags
│   │       │           ├── example_bash_operator.py.log
│   │       │           ├── example_branch_datetime_operator.py.log
│   │       │           ├── example_branch_day_of_week_operator.py.log
│   │       │           ├── example_branch_labels.py.log
│   │       │           ├── example_branch_operator.py.log
│   │       │           ├── example_branch_operator_decorator.py.log
│   │       │           ├── example_branch_python_dop_operator_3.py.log
│   │       │           ├── example_complex.py.log
│   │       │           ├── example_dag_decorator.py.log
│   │       │           ├── example_datasets.py.log
│   │       │           ├── example_dynamic_task_mapping.py.log
│   │       │           ├── example_dynamic_task_mapping_with_no_taskflow_operators.py.log
│   │       │           ├── example_external_task_marker_dag.py.log
│   │       │           ├── example_kubernetes_executor.py.log
│   │       │           ├── example_latest_only.py.log
│   │       │           ├── example_latest_only_with_trigger.py.log
│   │       │           ├── example_local_kubernetes_executor.py.log
│   │       │           ├── example_nested_branch_dag.py.log
│   │       │           ├── example_params_trigger_ui.py.log
│   │       │           ├── example_params_ui_tutorial.py.log
│   │       │           ├── example_passing_params_via_test_command.py.log
│   │       │           ├── example_python_operator.py.log
│   │       │           ├── example_sensor_decorator.py.log
│   │       │           ├── example_sensors.py.log
│   │       │           ├── example_setup_teardown.py.log
│   │       │           ├── example_setup_teardown_taskflow.py.log
│   │       │           ├── example_short_circuit_decorator.py.log
│   │       │           ├── example_short_circuit_operator.py.log
│   │       │           ├── example_skip_dag.py.log
│   │       │           ├── example_sla_dag.py.log
│   │       │           ├── example_subdag_operator.py.log
│   │       │           ├── example_task_group.py.log
│   │       │           ├── example_task_group_decorator.py.log
│   │       │           ├── example_time_delta_sensor_async.py.log
│   │       │           ├── example_trigger_controller_dag.py.log
│   │       │           ├── example_trigger_target_dag.py.log
│   │       │           ├── example_xcom.py.log
│   │       │           ├── example_xcomargs.py.log
│   │       │           ├── plugins
│   │       │           │   ├── event_listener.py.log
│   │       │           │   ├── listener_plugin.py.log
│   │       │           │   └── workday.py.log
│   │       │           ├── subdags
│   │       │           │   └── subdag.py.log
│   │       │           ├── tutorial.py.log
│   │       │           ├── tutorial_dag.py.log
│   │       │           ├── tutorial_taskflow_api.py.log
│   │       │           └── tutorial_taskflow_api_virtualenv.py.log
│   │       └── latest -> /Users/shubhampriyadarshi/PycharmProjects/StackExchange_API_PKT/airflow/logs/scheduler/2023-07-06
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
│   │   └── auth.py
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
├── logs
│   └── dbt.log
├── main.py
└── superset_se
    ├── __pycache__
    │   └── superset_config.cpython-39.pyc
    ├── superset.db
    └── superset_config.py

135 directories, 356 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                     | Summary                                                                                        |
| ---                                                                                      | ---                                                                                            |
| [main.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/main.py) | The code snippet sets up a FastAPI application and includes a router for version 1 of the API. |

</details>

<details closed><summary>App</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                        |
| ---                                                                                                  | ---                                                                                                                                                                                                                                            |
| [database.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/database.py) | The code snippet sets up a database connection using SQLAlchemy and Snowflake. It creates an engine and sessionmaker to handle database operations. The get_db function provides a session for database interaction and manages its lifecycle. |

</details>

<details closed><summary>Tasks</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [load_data_task.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/tasks/load_data_task.py) | The code snippet defines a class DataLoader with a static method load_data(). Within this method, it first calls the StackExchangeService to scrape data from a website. Then, it uses the SnowflakeService to insert the scraped data into a Snowflake database from a CSV file. Finally, it checks if the CSV file exists and deletes it if it does, printing a corresponding message. The main block runs the load_data() method using asyncio. |

</details>

<details closed><summary>Core</summary>

| File                                                                                              | Summary                                                                                                                       |
| ---                                                                                               | ---                                                                                                                           |
| [auth.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/core/auth.py) | The code snippet generates an authentication URL by combining the authorization base URL, client ID, redirect URI, and scope. |

</details>

<details closed><summary>Api_v1</summary>

| File                                                                                                  | Summary                                                                                                                                                                                                                                                                         |
| ---                                                                                                   | ---                                                                                                                                                                                                                                                                             |
| [api.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/api/api_v1/api.py) | This code snippet creates an API router using FastAPI. It includes multiple sub-routers for different endpoints such as home, callback, set_token, display_token, load_data, and get_data. Each sub-router is tagged for easy organization and management of the API endpoints. |

</details>

<details closed><summary>Endpoints</summary>

| File                                                                                                                                | Summary                                                                                                                                                                                                                                                            |
| ---                                                                                                                                 | ---                                                                                                                                                                                                                                                                |
| [callback.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/api/api_v1/endpoints/callback.py)           | This code defines a route "/auth-callback" that returns a rendered HTML template called "callback.html" using the Jinja2Templates library and FastAPI's Request model.                                                                                             |
| [home.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/api/api_v1/endpoints/home.py)                   | This code snippet defines an API router using FastAPI framework. It includes a GET endpoint for the home route that renders an index.html template using Jinja2Templates. The template receives the request object and an authentication URL as context variables. |
| [set_token.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/api/api_v1/endpoints/set_token.py)         | This code snippet defines an API endpoint "/set-token" that receives a token as input and saves it to a file called "token.txt". The token is sent as a JSON object with a "token" field. The endpoint returns a success message.                                  |
| [get_data.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/api/api_v1/endpoints/get_data.py)           | The code snippet uses FastAPI and httpx to create an API endpoint that retrieves data from the Stack Exchange API. It reads an encrypted access token from a file, sends a GET request to the API with the token in the headers, and returns the response data.    |
| [load_data.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/api/api_v1/endpoints/load_data.py)         | The code creates an API endpoint "/load-data" that triggers the load_data() method from the DataLoader class when accessed. This method handles the loading of data and returns a message indicating that the loading process is in progress.                      |
| [display_token.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/api/api_v1/endpoints/display_token.py) | The code snippet defines an API route "/display-token" that accepts a GET request with a token parameter. It returns an HTML template response using Jinja2, passing the request and token values to the template.                                                 |

</details>

<details closed><summary>Templates</summary>

| File                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                   |
| [index.html](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/templates/index.html)                 | This code snippet is an authentication example in HTML. It allows users to authenticate, load data, and display tags with their count. The loadTags function fetches tag data from the server and dynamically adds it to the tag container. The loadData function fetches data and displays a message using an alert. |
| [callback.html](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/templates/callback.html)           | This code snippet retrieves an access token from the URL fragment, sends it to a server endpoint via a POST request, and redirects the user to a page displaying the token if the request is successful.                                                                                                              |
| [display_token.html](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/templates/display_token.html) | This code snippet is a basic HTML template that displays the value of a token if it exists, or a message indicating that the token is not found. It uses a conditional statement to check if the token variable is defined, and then displays the token value or the "Access Token not found" message accordingly.    |

</details>

<details closed><summary>Services</summary>

| File                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [stackexchange_service.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/services/stackexchange_service.py) | The provided code snippet is for a StackExchangeService class that has two main functionalities:1. The scrape() method sends a request to the Stack Exchange API to retrieve tag information for a specific page. It then saves the tag data to a CSV file.2. The scrape_all() method iterates through multiple pages of tag data by calling the scrape() method asynchronously. It runs a maximum of 3 requests per second using aiometer. It stops when there are no more pages to scrape. |
| [snowflake_service.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/app/services/snowflake_service.py)         | The code snippet establishes a connection with a Snowflake database and defines a class, SnowflakeService, which contains a method that inserts data from a CSV file into a table named "tags" in the Snowflake database using the Pandas library.                                                                                                                                                                                                                                           |

</details>

<details closed><summary>Airflow</summary>

| File                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                |
| [airflow-webserver.pid](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/airflow-webserver.pid) | The provided code snippet does not contain enough information to accurately determine its core functionalities.                                                                                                                                                                                                    |
| [webserver_config.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/webserver_config.py)     | The provided code snippet contains the default configuration for the Airflow webserver. It includes authentication settings, such as the type of authentication to use, role setup, user self-registration, and OAuth and LDAP configurations. It also includes theme configuration options for the web interface. |

</details>

<details closed><summary>Dags</summary>

| File                                                                                                                    | Summary                                                                                                                                                                              |
| ---                                                                                                                     | ---                                                                                                                                                                                  |
| [load_data_dag.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/dags/load_data_dag.py) | This code snippet sets up an Airflow DAG for an ELT pipeline. It includes tasks for API extraction, DBT curation, calculation, and consumption. The tasks are executed sequentially. |

</details>

<details closed><summary>Task_id=dbt_consumption</summary>

| File                                                                                                                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                                                                                                                | ---                                                                                                                                                                                                                                                                                                                     |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T16:05:30.328585+00:00/task_id=dbt_consumption/attempt=1.log) | The code snippet is logging information related to the execution of a task called "dbt_consumption". It shows the dependencies being met, the start and end times of the task, and its success status. The task is executed using a PythonOperator in Airflow. The task completes successfully with a return code of 0. |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:13:11.144301+00:00/task_id=dbt_consumption/attempt=1.log) | The provided code snippet shows the execution of a task named "dbt_consumption". The task is successfully executed and marked as a success. The task does not have any downstream tasks scheduled.                                                                                                                      |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:19:19.316881+00:00/task_id=dbt_consumption/attempt=1.log) | The code snippet is logging information about task dependencies, starting attempts, executing a Python operator, exporting environment variables, and marking the task as successful.                                                                                                                                   |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:21:58.442497+00:00/task_id=dbt_consumption/attempt=1.log) | This code snippet shows the execution of a task called "dbt_consumption" in Airflow. The task runs successfully and is marked as a success.                                                                                                                                                                             |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-05T00:00:00+00:00/task_id=dbt_consumption/attempt=1.log)     | The code snippet shows the execution of a task called "dbt_consumption" in an Airflow DAG. The task successfully completes without any errors.                                                                                                                                                                          |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:23:11.700312+00:00/task_id=dbt_consumption/attempt=1.log) | This code snippet is from an Airflow task instance. It shows the successful execution of the "dbt_consumption" task, with the task marked as SUCCESS. The task was executed with specific environment variables and returned a value of None.                                                                           |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-04T00:00:00+00:00/task_id=dbt_consumption/attempt=1.log)     | The code snippet is logging the execution of a task instance, its dependencies, and the attempt number. It then runs a PythonOperator task called "dbt_consumption" and logs the execution details. Finally, it marks the task as successful and provides the return code.                                              |

</details>

<details closed><summary>Task_id=dbt_calculation</summary>

| File                                                                                                                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                            |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T16:05:30.328585+00:00/task_id=dbt_calculation/attempt=1.log) | The code snippet is from an Airflow task that is executing a PythonOperator called "dbt_calculation". The task is marked as successful with a return code of 0.                                                                                                                                                                                                                                |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:13:11.144301+00:00/task_id=dbt_calculation/attempt=1.log) | The code snippet shows the execution of a task called "dbt_calculation" in a workflow. It starts with checking dependencies, followed by attempting the task execution. The task is a PythonOperator that runs a process. It exports environment variables, executes the task, and marks it as successful. The task exits with a return code of 0, and there is one downstream task scheduled. |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:19:19.316881+00:00/task_id=dbt_calculation/attempt=1.log) | The provided code snippet shows the execution of a task called "dbt_calculation" in an Airflow environment. The task is executed successfully and marked as a success.                                                                                                                                                                                                                         |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:21:58.442497+00:00/task_id=dbt_calculation/attempt=1.log) | The provided code snippet shows the execution of a PythonOperator task called "dbt_calculation" in an Airflow environment. The task is successfully executed and marked as a success.                                                                                                                                                                                                          |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-05T00:00:00+00:00/task_id=dbt_calculation/attempt=1.log)     | The code snippet shows the execution of a task called "dbt_calculation" in an airflow workflow. The task is started, executed, and marked as successful.                                                                                                                                                                                                                                       |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:23:11.700312+00:00/task_id=dbt_calculation/attempt=1.log) | This code snippet is executing a Python task called "dbt_calculation" as part of an Airflow workflow. The task runs successfully, returning None, and is marked as a success. A total of 1 downstream task is scheduled for execution.                                                                                                                                                         |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-04T00:00:00+00:00/task_id=dbt_calculation/attempt=1.log)     | The code snippet provides logs of a task instance in an Airflow workflow. It shows the execution of a Python operator named "dbt_calculation" on a specific date. The task is marked as successful with a return code of 0.                                                                                                                                                                    |

</details>

<details closed><summary>Task_id=dbt_curation</summary>

| File                                                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                               |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T16:05:30.328585+00:00/task_id=dbt_curation/attempt=1.log) | This code snippet shows the execution of a Python task in an Airflow workflow. It exports environment variables, runs the task, and marks it as successful.                                                                                                                                                                       |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:13:11.144301+00:00/task_id=dbt_curation/attempt=1.log) | The code snippet shows the execution of a task called "dbt_curation" within a larger workflow. The task is executed successfully, marked as a success, and triggers downstream tasks.                                                                                                                                             |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:19:19.316881+00:00/task_id=dbt_curation/attempt=1.log) | The provided code snippet shows the execution of a PythonOperator task named "dbt_curation" in an Airflow workflow. The task is marked as successful and has no returned value.                                                                                                                                                   |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:21:58.442497+00:00/task_id=dbt_curation/attempt=1.log) | The code snippet is a log of a task execution in an Airflow workflow. It shows the successful execution of the "dbt_curation" task, which exports environment variables and returns a None value. The task is marked as successful, and one downstream task is scheduled.                                                         |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-05T00:00:00+00:00/task_id=dbt_curation/attempt=1.log)     | The provided code snippet shows the execution of a task called "dbt_curation" in an Airflow workflow. The task runs successfully and is marked as a success. The task's execution is logged with relevant details such as start and end times.                                                                                    |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:23:11.700312+00:00/task_id=dbt_curation/attempt=1.log) | The provided code snippet is logging information about a task execution in Airflow. It shows the task dependencies being met, starting the task attempt, executing a Python operator task, exporting environment variables, completing the task successfully, and scheduling downstream tasks.                                    |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-02T00:00:00+00:00/task_id=dbt_curation/attempt=1.log)     | The code snippet shows an Airflow task that failed to execute a bash command "dbt run". The command returned a non-zero exit code, which caused the task to be marked as UP_FOR_RETRY for a future attempt.                                                                                                                       |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-02T00:00:00+00:00/task_id=dbt_curation/attempt=2.log)     | The code snippet shows the execution of a BashOperator task called "dbt_curation" in an Airflow DAG. The task fails with a non-zero exit code 2 due to a missing "dbt_project.yml" file.                                                                                                                                          |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-03T00:00:00+00:00/task_id=dbt_curation/attempt=1.log)     | The provided code snippet is logging information related to the execution of a task called "dbt_curation". It shows the attempt number, execution details, command execution output, and the error encountered. The task failed with a non-zero exit code, marking it for retry.                                                  |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-03T00:00:00+00:00/task_id=dbt_curation/attempt=2.log)     | The provided code snippet shows the execution of a BashOperator task in an Airflow workflow. The task is aimed at running a command using dbt, a data transformation tool. However, the task fails with an error indicating that the expected dbt_project.yml configuration file is missing.                                      |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T15:50:49.010236+00:00/task_id=dbt_curation/attempt=1.log) | The code snippet is a log of a task instance in an Airflow workflow. It shows the execution of the "dbt_curation" task, which encountered an error due to a missing file or directory ("/path/to/dbt_se/"). The task is marked for retry.                                                                                         |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T15:50:49.010236+00:00/task_id=dbt_curation/attempt=2.log) | The code snippet is a log of a failed task execution in an airflow job. It attempts to run a dbt command, but the command returns a non-zero exit status, resulting in the task being marked as failed.                                                                                                                           |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T15:55:44.311095+00:00/task_id=dbt_curation/attempt=1.log) | The provided code snippet shows the execution of a task called "dbt_curation" in the context of an Airflow workflow. The task attempts to run a command using the subprocess module, specifically the "dbt run" command with certain arguments. However, the task fails and returns a non-zero exit status, resulting in a retry. |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T15:55:44.311095+00:00/task_id=dbt_curation/attempt=2.log) | The code snippet shows the execution of a task called "dbt_curation" in an Airflow DAG. However, the task failed with a non-zero exit status 2, indicating an error during the execution.                                                                                                                                         |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-04T00:00:00+00:00/task_id=dbt_curation/attempt=1.log)     | The code snippet shows the execution of a task called "dbt_curation" within an Airflow DAG. The task is successfully executed, marked as a success, and triggers downstream tasks.                                                                                                                                                |

</details>

<details closed><summary>Task_id=api_extract_load</summary>

| File                                                                                                                                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                               |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T16:05:30.328585+00:00/task_id=api_extract_load/attempt=1.log) | The code snippet shows the execution of a BashOperator task called "api_extract_load". It runs a command to make a curl request to a local API endpoint and retrieves a response. The task is marked as successful, and there is one downstream task scheduled.                                                                                                                   |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:13:11.144301+00:00/task_id=api_extract_load/attempt=1.log) | The provided code snippet is a log output of a task execution. It shows the successful execution of a BashOperator task named "api_extract_load", which involves running a command to fetch data from a specified API endpoint. The task completes successfully with a return code of 0.                                                                                          |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:19:19.316881+00:00/task_id=api_extract_load/attempt=1.log) | The provided code snippet is a log of a task instance that executed a BashOperator. The operator ran a command to make a curl request to `http://localhost:8000/apiv1/load-data`. The request returned a "Not Found" error, but the task was marked as successful.                                                                                                                |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:21:58.442497+00:00/task_id=api_extract_load/attempt=1.log) | The code snippet is logging information about the execution of a task called "api_extract_load." It shows the attempt number, execution details, environment variables, and the command being executed. The task is making a curl request to a local server and receiving a response of "Not Found." The task is marked as successful and there is one downstream task scheduled. |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-05T00:00:00+00:00/task_id=api_extract_load/attempt=1.log)     | The provided code snippet is a log that shows the execution of a task called "api_extract_load". The task invokes a BashOperator that runs a curl command to fetch data from a specified API endpoint. The execution is marked as SUCCESS, indicating that the task completed without errors.                                                                                     |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-05T12:23:11.700312+00:00/task_id=api_extract_load/attempt=1.log) | The provided code snippet is executing a task called "api_extract_load" using the BashOperator. It runs a curl command to retrieve data from a specified API endpoint and marks the task as successful if the command returns a 0 exit code.                                                                                                                                      |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-02T00:00:00+00:00/task_id=api_extract_load/attempt=1.log)     | The provided code snippet shows the execution of a task called "api_extract_load" in an Airflow environment. The task is attempting to run a Bash command to curl a URL, but the command fails with a non-zero exit code. The task is marked for retry.                                                                                                                           |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-02T00:00:00+00:00/task_id=api_extract_load/attempt=2.log)     | The provided code snippet is part of a task in a workflow management system. It executes a Bash command using the curl command to make an HTTP request to http://localhost:8000/load-data. The response indicates that the requested data is not found. The task is marked as successful and there is one downstream task scheduled.                                              |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-03T00:00:00+00:00/task_id=api_extract_load/attempt=1.log)     | The code snippet shows the execution of a task called "api_extract_load". It attempts to run a bash command using curl to connect to a localhost server on port 8000 and retrieve data. However, the connection fails, resulting in a non-zero exit code and marking the task for retry.                                                                                          |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-03T00:00:00+00:00/task_id=api_extract_load/attempt=2.log)     | The provided code snippet executes a task called "api_extract_load" using a BashOperator. It runs a curl command to retrieve data from a URL and marks the task as successful if the command returns a 0 exit code.                                                                                                                                                               |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T15:50:49.010236+00:00/task_id=api_extract_load/attempt=1.log) | The code snippet is executing a BashOperator task called "api_extract_load". It runs a curl command to retrieve data from a specified URL. The output shows that the command was successful, and the task is marked as SUCCESS.                                                                                                                                                   |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=manual__2023-07-04T15:55:44.311095+00:00/task_id=api_extract_load/attempt=1.log) | This code snippet executes a BashOperator task called "api_extract_load" which sends an HTTP request to "http://localhost:8000/ap1/v1/load-data". The response received is "Not Found". The task is marked as SUCCESS and there is 1 downstream task scheduled.                                                                                                                   |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=stackexchange_elt/run_id=scheduled__2023-07-04T00:00:00+00:00/task_id=api_extract_load/attempt=1.log)     | The code snippet shows the execution of a task called "api_extract_load" in an Airflow workflow. The task sends a request to a local server using curl and receives a response. The task is marked as successful, and there is one downstream task scheduled.                                                                                                                     |

</details>

<details closed><summary>2023-07-06</summary>

| File                                                                                                                                                 | Summary                                |
| ---                                                                                                                                                  | ---                                    |
| [load_data_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/load_data_dag.py.log) | Prompt exceeds max token limit: 12601. |

</details>

<details closed><summary>Example_dags</summary>

| File                                                                                                                                                                                                                                                              | Summary                                |
| ---                                                                                                                                                                                                                                                               | ---                                    |
| [example_branch_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_branch_operator.py.log)                                                                 | Prompt exceeds max token limit: 6281.  |
| [example_params_ui_tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_params_ui_tutorial.py.log)                                                           | Prompt exceeds max token limit: 10041. |
| [example_params_trigger_ui.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_params_trigger_ui.py.log)                                                             | Prompt exceeds max token limit: 9961.  |
| [example_local_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_local_kubernetes_executor.py.log)                                             | Prompt exceeds max token limit: 10959. |
| [example_setup_teardown.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_setup_teardown.py.log)                                                                   | Prompt exceeds max token limit: 8291.  |
| [example_sensor_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_sensor_decorator.py.log)                                                               | Prompt exceeds max token limit: 11641. |
| [example_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_kubernetes_executor.py.log)                                                         | Prompt exceeds max token limit: 6437.  |
| [example_time_delta_sensor_async.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_time_delta_sensor_async.py.log)                                                 | Prompt exceeds max token limit: 12601. |
| [example_datasets.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_datasets.py.log)                                                                               | Prompt exceeds max token limit: 12681. |
| [example_sla_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_sla_dag.py.log)                                                                                 | Prompt exceeds max token limit: 12681. |
| [example_branch_python_dop_operator_3.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_branch_python_dop_operator_3.py.log)                                       | Prompt exceeds max token limit: 6281.  |
| [example_subdag_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_subdag_operator.py.log)                                                                 | Prompt exceeds max token limit: 24215. |
| [example_sensors.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_sensors.py.log)                                                                                 | Prompt exceeds max token limit: 11801. |
| [tutorial_taskflow_api.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/tutorial_taskflow_api.py.log)                                                                     | Prompt exceeds max token limit: 12601. |
| [example_xcom.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_xcom.py.log)                                                                                       | Prompt exceeds max token limit: 12601. |
| [example_branch_day_of_week_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_branch_day_of_week_operator.py.log)                                         | Prompt exceeds max token limit: 6281.  |
| [example_external_task_marker_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_external_task_marker_dag.py.log)                                               | Prompt exceeds max token limit: 7625.  |
| [example_nested_branch_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_nested_branch_dag.py.log)                                                             | Prompt exceeds max token limit: 8966.  |
| [example_short_circuit_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_short_circuit_operator.py.log)                                                   | Prompt exceeds max token limit: 12601. |
| [example_dag_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_dag_decorator.py.log)                                                                     | Prompt exceeds max token limit: 6361.  |
| [example_complex.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_complex.py.log)                                                                                 | Prompt exceeds max token limit: 6361.  |
| [example_skip_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_skip_dag.py.log)                                                                               | Prompt exceeds max token limit: 12681. |
| [example_branch_datetime_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_branch_datetime_operator.py.log)                                               | Prompt exceeds max token limit: 8777.  |
| [example_python_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_python_operator.py.log)                                                                 | Prompt exceeds max token limit: 13718. |
| [example_bash_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_bash_operator.py.log)                                                                     | Prompt exceeds max token limit: 6281.  |
| [tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/tutorial.py.log)                                                                                               | Prompt exceeds max token limit: 12601. |
| [example_passing_params_via_test_command.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_passing_params_via_test_command.py.log)                                 | Prompt exceeds max token limit: 10761. |
| [example_short_circuit_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_short_circuit_decorator.py.log)                                                 | Prompt exceeds max token limit: 12441. |
| [example_dynamic_task_mapping.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_dynamic_task_mapping.py.log)                                                       | Prompt exceeds max token limit: 6361.  |
| [example_trigger_target_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_trigger_target_dag.py.log)                                                           | Prompt exceeds max token limit: 12601. |
| [example_task_group_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_task_group_decorator.py.log)                                                       | Prompt exceeds max token limit: 12601. |
| [example_setup_teardown_taskflow.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_setup_teardown_taskflow.py.log)                                                 | Prompt exceeds max token limit: 8346.  |
| [example_branch_operator_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_branch_operator_decorator.py.log)                                             | Prompt exceeds max token limit: 6281.  |
| [tutorial_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/tutorial_dag.py.log)                                                                                       | Prompt exceeds max token limit: 12601. |
| [example_latest_only_with_trigger.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_latest_only_with_trigger.py.log)                                               | Prompt exceeds max token limit: 7401.  |
| [example_xcomargs.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_xcomargs.py.log)                                                                               | Prompt exceeds max token limit: 15113. |
| [example_latest_only.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_latest_only.py.log)                                                                         | Prompt exceeds max token limit: 7001.  |
| [example_trigger_controller_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_trigger_controller_dag.py.log)                                                   | Prompt exceeds max token limit: 12601. |
| [tutorial_taskflow_api_virtualenv.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/tutorial_taskflow_api_virtualenv.py.log)                                               | Prompt exceeds max token limit: 11345. |
| [example_task_group.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_task_group.py.log)                                                                           | Prompt exceeds max token limit: 12601. |
| [example_branch_labels.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_branch_labels.py.log)                                                                     | Prompt exceeds max token limit: 6281.  |
| [example_dynamic_task_mapping_with_no_taskflow_operators.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/example_dynamic_task_mapping_with_no_taskflow_operators.py.log) | Prompt exceeds max token limit: 6361.  |
| [example_branch_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_branch_operator.py.log)                                                                 | Prompt exceeds max token limit: 8899.  |
| [example_params_ui_tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_params_ui_tutorial.py.log)                                                           | Prompt exceeds max token limit: 11104. |
| [example_params_trigger_ui.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_params_trigger_ui.py.log)                                                             | Prompt exceeds max token limit: 10819. |
| [example_local_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_local_kubernetes_executor.py.log)                                             | Prompt exceeds max token limit: 13079. |
| [example_setup_teardown.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_setup_teardown.py.log)                                                                   | Prompt exceeds max token limit: 12251. |
| [example_sensor_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_sensor_decorator.py.log)                                                               | Prompt exceeds max token limit: 17139. |
| [example_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_kubernetes_executor.py.log)                                                         | Prompt exceeds max token limit: 9245.  |
| [example_time_delta_sensor_async.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_time_delta_sensor_async.py.log)                                                 | Prompt exceeds max token limit: 18099. |
| [example_datasets.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_datasets.py.log)                                                                               | Prompt exceeds max token limit: 18629. |
| [example_sla_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_sla_dag.py.log)                                                                                 | Prompt exceeds max token limit: 18099. |
| [example_branch_python_dop_operator_3.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_branch_python_dop_operator_3.py.log)                                       | Prompt exceeds max token limit: 9104.  |
| [example_subdag_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_subdag_operator.py.log)                                                                 | Prompt exceeds max token limit: 34550. |
| [example_sensors.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_sensors.py.log)                                                                                 | Prompt exceeds max token limit: 17699. |
| [tutorial_taskflow_api.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/tutorial_taskflow_api.py.log)                                                                     | Prompt exceeds max token limit: 18259. |
| [example_xcom.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_xcom.py.log)                                                                                       | Prompt exceeds max token limit: 18099. |
| [example_branch_day_of_week_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_branch_day_of_week_operator.py.log)                                         | Prompt exceeds max token limit: 8899.  |
| [example_external_task_marker_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_external_task_marker_dag.py.log)                                               | Prompt exceeds max token limit: 11293. |
| [example_nested_branch_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_nested_branch_dag.py.log)                                                             | Prompt exceeds max token limit: 10179. |
| [example_short_circuit_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_short_circuit_operator.py.log)                                                   | Prompt exceeds max token limit: 18019. |
| [example_dag_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_dag_decorator.py.log)                                                                     | Prompt exceeds max token limit: 9139.  |
| [example_complex.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_complex.py.log)                                                                                 | Prompt exceeds max token limit: 9139.  |
| [example_skip_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_skip_dag.py.log)                                                                               | Prompt exceeds max token limit: 18019. |
| [example_branch_datetime_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_branch_datetime_operator.py.log)                                               | Prompt exceeds max token limit: 12535. |
| [example_python_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_python_operator.py.log)                                                                 | Prompt exceeds max token limit: 18529. |
| [example_bash_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_bash_operator.py.log)                                                                     | Prompt exceeds max token limit: 8899.  |
| [tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/tutorial.py.log)                                                                                               | Prompt exceeds max token limit: 18259. |
| [example_passing_params_via_test_command.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_passing_params_via_test_command.py.log)                                 | Prompt exceeds max token limit: 14179. |
| [example_short_circuit_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_short_circuit_decorator.py.log)                                                 | Prompt exceeds max token limit: 17859. |
| [example_dynamic_task_mapping.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_dynamic_task_mapping.py.log)                                                       | Prompt exceeds max token limit: 9299.  |
| [example_trigger_target_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_trigger_target_dag.py.log)                                                           | Prompt exceeds max token limit: 18099. |
| [example_task_group_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_task_group_decorator.py.log)                                                       | Prompt exceeds max token limit: 18099. |
| [example_setup_teardown_taskflow.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_setup_teardown_taskflow.py.log)                                                 | Prompt exceeds max token limit: 12251. |
| [example_branch_operator_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_branch_operator_decorator.py.log)                                             | Prompt exceeds max token limit: 9024.  |
| [tutorial_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/tutorial_dag.py.log)                                                                                       | Prompt exceeds max token limit: 18259. |
| [example_latest_only_with_trigger.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_latest_only_with_trigger.py.log)                                               | Prompt exceeds max token limit: 9779.  |
| [example_xcomargs.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_xcomargs.py.log)                                                                               | Prompt exceeds max token limit: 21853. |
| [example_latest_only.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_latest_only.py.log)                                                                         | Prompt exceeds max token limit: 9699.  |
| [example_trigger_controller_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_trigger_controller_dag.py.log)                                                   | Prompt exceeds max token limit: 18099. |
| [tutorial_taskflow_api_virtualenv.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/tutorial_taskflow_api_virtualenv.py.log)                                               | Prompt exceeds max token limit: 16457. |
| [example_task_group.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_task_group.py.log)                                                                           | Prompt exceeds max token limit: 18099. |
| [example_branch_labels.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_branch_labels.py.log)                                                                     | Prompt exceeds max token limit: 8899.  |
| [example_dynamic_task_mapping_with_no_taskflow_operators.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/example_dynamic_task_mapping_with_no_taskflow_operators.py.log) | Prompt exceeds max token limit: 9379.  |
| [example_branch_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_branch_operator.py.log)                                                                 | Prompt exceeds max token limit: 16681. |
| [example_params_ui_tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_params_ui_tutorial.py.log)                                                           | Prompt exceeds max token limit: 17801. |
| [example_params_trigger_ui.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_params_trigger_ui.py.log)                                                             | Prompt exceeds max token limit: 17641. |
| [example_local_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_local_kubernetes_executor.py.log)                                             | Prompt exceeds max token limit: 22407. |
| [example_setup_teardown.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_setup_teardown.py.log)                                                                   | Prompt exceeds max token limit: 16816. |
| [example_sensor_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_sensor_decorator.py.log)                                                               | Prompt exceeds max token limit: 23401. |
| [example_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_kubernetes_executor.py.log)                                                         | Prompt exceeds max token limit: 16421. |
| [example_time_delta_sensor_async.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_time_delta_sensor_async.py.log)                                                 | Prompt exceeds max token limit: 32921. |
| [example_datasets.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_datasets.py.log)                                                                               | Prompt exceeds max token limit: 33321. |
| [example_sla_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_sla_dag.py.log)                                                                                 | Prompt exceeds max token limit: 32521. |
| [example_branch_python_dop_operator_3.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_branch_python_dop_operator_3.py.log)                                       | Prompt exceeds max token limit: 16681. |
| [example_subdag_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_subdag_operator.py.log)                                                                 | Prompt exceeds max token limit: 62465. |
| [example_sensors.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_sensors.py.log)                                                                                 | Prompt exceeds max token limit: 24041. |
| [tutorial_taskflow_api.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/tutorial_taskflow_api.py.log)                                                                     | Prompt exceeds max token limit: 32921. |
| [example_xcom.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_xcom.py.log)                                                                                       | Prompt exceeds max token limit: 32921. |
| [example_branch_day_of_week_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_branch_day_of_week_operator.py.log)                                         | Prompt exceeds max token limit: 16521. |
| [example_external_task_marker_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_external_task_marker_dag.py.log)                                               | Prompt exceeds max token limit: 20201. |
| [example_nested_branch_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_nested_branch_dag.py.log)                                                             | Prompt exceeds max token limit: 17081. |
| [example_short_circuit_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_short_circuit_operator.py.log)                                                   | Prompt exceeds max token limit: 31401. |
| [example_dag_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_dag_decorator.py.log)                                                                     | Prompt exceeds max token limit: 16681. |
| [example_complex.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_complex.py.log)                                                                                 | Prompt exceeds max token limit: 16681. |
| [example_skip_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_skip_dag.py.log)                                                                               | Prompt exceeds max token limit: 31961. |
| [example_branch_datetime_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_branch_datetime_operator.py.log)                                               | Prompt exceeds max token limit: 23001. |
| [example_python_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_python_operator.py.log)                                                                 | Prompt exceeds max token limit: 22836. |
| [example_bash_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_bash_operator.py.log)                                                                     | Prompt exceeds max token limit: 16441. |
| [tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/tutorial.py.log)                                                                                               | Prompt exceeds max token limit: 32921. |
| [example_passing_params_via_test_command.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_passing_params_via_test_command.py.log)                                 | Prompt exceeds max token limit: 18521. |
| [example_short_circuit_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_short_circuit_decorator.py.log)                                                 | Prompt exceeds max token limit: 25321. |
| [example_dynamic_task_mapping.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_dynamic_task_mapping.py.log)                                                       | Prompt exceeds max token limit: 16761. |
| [example_trigger_target_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_trigger_target_dag.py.log)                                                           | Prompt exceeds max token limit: 32921. |
| [example_task_group_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_task_group_decorator.py.log)                                                       | Prompt exceeds max token limit: 32841. |
| [example_setup_teardown_taskflow.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_setup_teardown_taskflow.py.log)                                                 | Prompt exceeds max token limit: 17201. |
| [example_branch_operator_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_branch_operator_decorator.py.log)                                             | Prompt exceeds max token limit: 16681. |
| [tutorial_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/tutorial_dag.py.log)                                                                                       | Prompt exceeds max token limit: 32921. |
| [example_latest_only_with_trigger.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_latest_only_with_trigger.py.log)                                               | Prompt exceeds max token limit: 16841. |
| [example_xcomargs.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_xcomargs.py.log)                                                                               | Prompt exceeds max token limit: 39497. |
| [example_latest_only.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_latest_only.py.log)                                                                         | Prompt exceeds max token limit: 16841. |
| [example_trigger_controller_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_trigger_controller_dag.py.log)                                                   | Prompt exceeds max token limit: 32921. |
| [tutorial_taskflow_api_virtualenv.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/tutorial_taskflow_api_virtualenv.py.log)                                               | Prompt exceeds max token limit: 29561. |
| [example_task_group.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_task_group.py.log)                                                                           | Prompt exceeds max token limit: 32761. |
| [example_branch_labels.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_branch_labels.py.log)                                                                     | Prompt exceeds max token limit: 16601. |
| [example_dynamic_task_mapping_with_no_taskflow_operators.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/example_dynamic_task_mapping_with_no_taskflow_operators.py.log) | Prompt exceeds max token limit: 16841. |
| [example_branch_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_branch_operator.py.log)                                                                 | Prompt exceeds max token limit: 8281.  |
| [example_params_ui_tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_params_ui_tutorial.py.log)                                                           | Prompt exceeds max token limit: 9641.  |
| [example_params_trigger_ui.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_params_trigger_ui.py.log)                                                             | Prompt exceeds max token limit: 9081.  |
| [example_local_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_local_kubernetes_executor.py.log)                                             | Prompt exceeds max token limit: 11595. |
| [example_setup_teardown.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_setup_teardown.py.log)                                                                   | Prompt exceeds max token limit: 9886.  |
| [example_sensor_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_sensor_decorator.py.log)                                                               | Prompt exceeds max token limit: 13401. |
| [example_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_kubernetes_executor.py.log)                                                         | Prompt exceeds max token limit: 8387.  |
| [example_time_delta_sensor_async.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_time_delta_sensor_async.py.log)                                                 | Prompt exceeds max token limit: 16521. |
| [example_datasets.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_datasets.py.log)                                                                               | Prompt exceeds max token limit: 16521. |
| [example_sla_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_sla_dag.py.log)                                                                                 | Prompt exceeds max token limit: 16441. |
| [example_branch_python_dop_operator_3.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_branch_python_dop_operator_3.py.log)                                       | Prompt exceeds max token limit: 8281.  |
| [example_subdag_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_subdag_operator.py.log)                                                                 | Prompt exceeds max token limit: 31406. |
| [example_sensors.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_sensors.py.log)                                                                                 | Prompt exceeds max token limit: 13801. |
| [tutorial_taskflow_api.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/tutorial_taskflow_api.py.log)                                                                     | Prompt exceeds max token limit: 16681. |
| [example_xcom.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_xcom.py.log)                                                                                       | Prompt exceeds max token limit: 16601. |
| [example_branch_day_of_week_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_branch_day_of_week_operator.py.log)                                         | Prompt exceeds max token limit: 8281.  |
| [example_external_task_marker_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_external_task_marker_dag.py.log)                                               | Prompt exceeds max token limit: 10313. |
| [example_nested_branch_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_nested_branch_dag.py.log)                                                             | Prompt exceeds max token limit: 8761.  |
| [example_short_circuit_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_short_circuit_operator.py.log)                                                   | Prompt exceeds max token limit: 16361. |
| [example_dag_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_dag_decorator.py.log)                                                                     | Prompt exceeds max token limit: 8281.  |
| [example_complex.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_complex.py.log)                                                                                 | Prompt exceeds max token limit: 8281.  |
| [example_skip_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_skip_dag.py.log)                                                                               | Prompt exceeds max token limit: 16361. |
| [example_branch_datetime_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_branch_datetime_operator.py.log)                                               | Prompt exceeds max token limit: 11577. |
| [example_python_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_python_operator.py.log)                                                                 | Prompt exceeds max token limit: 14494. |
| [example_bash_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_bash_operator.py.log)                                                                     | Prompt exceeds max token limit: 8281.  |
| [tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/tutorial.py.log)                                                                                               | Prompt exceeds max token limit: 16681. |
| [example_passing_params_via_test_command.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_passing_params_via_test_command.py.log)                                 | Prompt exceeds max token limit: 10041. |
| [example_short_circuit_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_short_circuit_decorator.py.log)                                                 | Prompt exceeds max token limit: 15801. |
| [example_dynamic_task_mapping.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_dynamic_task_mapping.py.log)                                                       | Prompt exceeds max token limit: 8361.  |
| [example_trigger_target_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_trigger_target_dag.py.log)                                                           | Prompt exceeds max token limit: 16601. |
| [example_task_group_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_task_group_decorator.py.log)                                                       | Prompt exceeds max token limit: 16521. |
| [example_setup_teardown_taskflow.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_setup_teardown_taskflow.py.log)                                                 | Prompt exceeds max token limit: 10592. |
| [example_branch_operator_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_branch_operator_decorator.py.log)                                             | Prompt exceeds max token limit: 8281.  |
| [tutorial_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/tutorial_dag.py.log)                                                                                       | Prompt exceeds max token limit: 16681. |
| [example_latest_only_with_trigger.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_latest_only_with_trigger.py.log)                                               | Prompt exceeds max token limit: 8681.  |
| [example_xcomargs.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_xcomargs.py.log)                                                                               | Prompt exceeds max token limit: 20009. |
| [example_latest_only.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_latest_only.py.log)                                                                         | Prompt exceeds max token limit: 8601.  |
| [example_trigger_controller_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_trigger_controller_dag.py.log)                                                   | Prompt exceeds max token limit: 16521. |
| [tutorial_taskflow_api_virtualenv.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/tutorial_taskflow_api_virtualenv.py.log)                                               | Prompt exceeds max token limit: 15089. |
| [example_task_group.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_task_group.py.log)                                                                           | Prompt exceeds max token limit: 16441. |
| [example_branch_labels.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_branch_labels.py.log)                                                                     | Prompt exceeds max token limit: 8281.  |
| [example_dynamic_task_mapping_with_no_taskflow_operators.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/example_dynamic_task_mapping_with_no_taskflow_operators.py.log) | Prompt exceeds max token limit: 8361.  |
| [example_branch_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_branch_operator.py.log)                                                                 | Prompt exceeds max token limit: 6521.  |
| [example_params_ui_tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_params_ui_tutorial.py.log)                                                           | Prompt exceeds max token limit: 8361.  |
| [example_params_trigger_ui.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_params_trigger_ui.py.log)                                                             | Prompt exceeds max token limit: 8121.  |
| [example_local_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_local_kubernetes_executor.py.log)                                             | Prompt exceeds max token limit: 9475.  |
| [example_setup_teardown.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_setup_teardown.py.log)                                                                   | Prompt exceeds max token limit: 8731.  |
| [example_sensor_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_sensor_decorator.py.log)                                                               | Prompt exceeds max token limit: 11801. |
| [example_kubernetes_executor.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_kubernetes_executor.py.log)                                                         | Prompt exceeds max token limit: 6437.  |
| [example_time_delta_sensor_async.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_time_delta_sensor_async.py.log)                                                 | Prompt exceeds max token limit: 12921. |
| [example_datasets.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_datasets.py.log)                                                                               | Prompt exceeds max token limit: 13001. |
| [example_sla_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_sla_dag.py.log)                                                                                 | Prompt exceeds max token limit: 12921. |
| [example_branch_python_dop_operator_3.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_branch_python_dop_operator_3.py.log)                                       | Prompt exceeds max token limit: 6521.  |
| [example_subdag_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_subdag_operator.py.log)                                                                 | Prompt exceeds max token limit: 24674. |
| [example_sensors.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_sensors.py.log)                                                                                 | Prompt exceeds max token limit: 12361. |
| [tutorial_taskflow_api.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/tutorial_taskflow_api.py.log)                                                                     | Prompt exceeds max token limit: 13001. |
| [example_xcom.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_xcom.py.log)                                                                                       | Prompt exceeds max token limit: 12921. |
| [example_branch_day_of_week_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_branch_day_of_week_operator.py.log)                                         | Prompt exceeds max token limit: 6521.  |
| [example_external_task_marker_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_external_task_marker_dag.py.log)                                               | Prompt exceeds max token limit: 7817.  |
| [example_nested_branch_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_nested_branch_dag.py.log)                                                             | Prompt exceeds max token limit: 7401.  |
| [example_short_circuit_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_short_circuit_operator.py.log)                                                   | Prompt exceeds max token limit: 12921. |
| [example_dag_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_dag_decorator.py.log)                                                                     | Prompt exceeds max token limit: 6521.  |
| [example_complex.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_complex.py.log)                                                                                 | Prompt exceeds max token limit: 6521.  |
| [example_skip_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_skip_dag.py.log)                                                                               | Prompt exceeds max token limit: 12921. |
| [example_branch_datetime_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_branch_datetime_operator.py.log)                                               | Prompt exceeds max token limit: 9113.  |
| [example_python_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_python_operator.py.log)                                                                 | Prompt exceeds max token limit: 12942. |
| [example_bash_operator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_bash_operator.py.log)                                                                     | Prompt exceeds max token limit: 6521.  |
| [tutorial.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/tutorial.py.log)                                                                                               | Prompt exceeds max token limit: 13272. |
| [example_passing_params_via_test_command.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_passing_params_via_test_command.py.log)                                 | Prompt exceeds max token limit: 9721.  |
| [example_short_circuit_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_short_circuit_decorator.py.log)                                                 | Prompt exceeds max token limit: 12921. |
| [example_dynamic_task_mapping.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_dynamic_task_mapping.py.log)                                                       | Prompt exceeds max token limit: 6521.  |
| [example_trigger_target_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_trigger_target_dag.py.log)                                                           | Prompt exceeds max token limit: 12921. |
| [example_task_group_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_task_group_decorator.py.log)                                                       | Prompt exceeds max token limit: 12921. |
| [example_setup_teardown_taskflow.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_setup_teardown_taskflow.py.log)                                                 | Prompt exceeds max token limit: 8786.  |
| [example_branch_operator_decorator.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_branch_operator_decorator.py.log)                                             | Prompt exceeds max token limit: 6441.  |
| [tutorial_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/tutorial_dag.py.log)                                                                                       | Prompt exceeds max token limit: 13001. |
| [example_latest_only_with_trigger.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_latest_only_with_trigger.py.log)                                               | Prompt exceeds max token limit: 6841.  |
| [example_xcomargs.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_xcomargs.py.log)                                                                               | Prompt exceeds max token limit: 15497. |
| [example_latest_only.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_latest_only.py.log)                                                                         | Prompt exceeds max token limit: 6681.  |
| [example_trigger_controller_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_trigger_controller_dag.py.log)                                                   | Prompt exceeds max token limit: 12921. |
| [tutorial_taskflow_api_virtualenv.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/tutorial_taskflow_api_virtualenv.py.log)                                               | Prompt exceeds max token limit: 11705. |
| [example_task_group.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_task_group.py.log)                                                                           | Prompt exceeds max token limit: 12921. |
| [example_branch_labels.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_branch_labels.py.log)                                                                     | Prompt exceeds max token limit: 6521.  |
| [example_dynamic_task_mapping_with_no_taskflow_operators.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/example_dynamic_task_mapping_with_no_taskflow_operators.py.log) | Prompt exceeds max token limit: 6521.  |

</details>

<details closed><summary>Plugins</summary>

| File                                                                                                                                                                                      | Summary                                |
| ---                                                                                                                                                                                       | ---                                    |
| [listener_plugin.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/plugins/listener_plugin.py.log) | Prompt exceeds max token limit: 8676.  |
| [workday.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/plugins/workday.py.log)                 | Prompt exceeds max token limit: 11345. |
| [event_listener.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/plugins/event_listener.py.log)   | Prompt exceeds max token limit: 8676.  |
| [listener_plugin.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/plugins/listener_plugin.py.log) | Prompt exceeds max token limit: 12691. |
| [workday.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/plugins/workday.py.log)                 | Prompt exceeds max token limit: 12691. |
| [event_listener.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/plugins/event_listener.py.log)   | Prompt exceeds max token limit: 12636. |
| [listener_plugin.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/plugins/listener_plugin.py.log) | Prompt exceeds max token limit: 22591. |
| [workday.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/plugins/workday.py.log)                 | Prompt exceeds max token limit: 29561. |
| [event_listener.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/plugins/event_listener.py.log)   | Prompt exceeds max token limit: 22591. |
| [listener_plugin.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/plugins/listener_plugin.py.log) | Prompt exceeds max token limit: 11646. |
| [workday.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/plugins/workday.py.log)                 | Prompt exceeds max token limit: 14842. |
| [event_listener.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/plugins/event_listener.py.log)   | Prompt exceeds max token limit: 11536. |
| [listener_plugin.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/plugins/listener_plugin.py.log) | Prompt exceeds max token limit: 8951.  |
| [workday.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/plugins/workday.py.log)                 | Prompt exceeds max token limit: 8951.  |
| [event_listener.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/plugins/event_listener.py.log)   | Prompt exceeds max token limit: 8951.  |

</details>

<details closed><summary>Subdags</summary>

| File                                                                                                                                                                    | Summary                                |
| ---                                                                                                                                                                     | ---                                    |
| [subdag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-06/native_dags/example_dags/subdags/subdag.py.log) | Prompt exceeds max token limit: 8676.  |
| [subdag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/native_dags/example_dags/subdags/subdag.py.log) | Prompt exceeds max token limit: 12691. |
| [subdag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/native_dags/example_dags/subdags/subdag.py.log) | Prompt exceeds max token limit: 22591. |
| [subdag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/native_dags/example_dags/subdags/subdag.py.log) | Prompt exceeds max token limit: 11646. |
| [subdag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/native_dags/example_dags/subdags/subdag.py.log) | Prompt exceeds max token limit: 8951.  |

</details>

<details closed><summary>2023-07-02</summary>

| File                                                                                                                                                 | Summary                                |
| ---                                                                                                                                                  | ---                                    |
| [load_data_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-02/load_data_dag.py.log) | Prompt exceeds max token limit: 18659. |

</details>

<details closed><summary>2023-07-05</summary>

| File                                                                                                                                                 | Summary                                |
| ---                                                                                                                                                  | ---                                    |
| [load_data_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-05/load_data_dag.py.log) | Prompt exceeds max token limit: 24441. |

</details>

<details closed><summary>2023-07-04</summary>

| File                                                                                                                                                 | Summary                               |
| ---                                                                                                                                                  | ---                                   |
| [load_data_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-04/load_data_dag.py.log) | Prompt exceeds max token limit: 9487. |

</details>

<details closed><summary>2023-07-03</summary>

| File                                                                                                                                                 | Summary                                |
| ---                                                                                                                                                  | ---                                    |
| [load_data_dag.py.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/scheduler/2023-07-03/load_data_dag.py.log) | Prompt exceeds max token limit: 13001. |

</details>

<details closed><summary>Task_id=run_etl</summary>

| File                                                                                                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T16:07:10.585978+00:00/task_id=run_etl/attempt=1.log) | The provided code snippet is from an execution log of a task in a data processing pipeline. It shows the dependencies being met, attempts made, execution start, and an error occurring during serialization of a coroutine object, causing the task to fail and be marked for retry.                                              |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T16:36:31.018999+00:00/task_id=run_etl/attempt=1.log) | The code snippet shows the execution of a task called "run_etl" in the "load_data_dag" DAG. The task is executed using a BashOperator, which runs a curl command to load data from a local server. The task is marked as successful upon completion.                                                                               |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=scheduled__2023-07-02T00:00:00+00:00/task_id=run_etl/attempt=1.log)     | The provided code snippet is executing a BashOperator task called "run_etl" on a specified date and time. It runs a command to curl a URL "http://localhost:8000/load-data". The task is marked as successful with a return code of 0.                                                                                             |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T20:45:02.552085+00:00/task_id=run_etl/attempt=1.log) | The code snippet shows the execution of a task called "run_etl" in a data pipeline. The task is executed using a BashOperator and involves making a curl request to a local server. The task completes successfully and no downstream tasks are scheduled.                                                                         |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T16:14:00.400287+00:00/task_id=run_etl/attempt=1.log) | The code snippet is from an Airflow task instance log. It shows the execution of a task called "run_etl" in the "load_data_dag" DAG. The task encountered an error due to the "httpx" module lacking the "run" attribute, resulting in the task being marked for retry. The task failed with a return code of 1.                   |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T15:42:22.363032+00:00/task_id=run_etl/attempt=1.log) | The code snippet is logging information about task dependencies, starting attempt, executing a Python operator, running a task process, exporting environment variables, and encountering dependency failures.                                                                                                                     |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T15:42:22.363032+00:00/task_id=run_etl/attempt=2.log) | The code snippet shows the execution of a task called "run_etl". It attempts to call an endpoint and log a message. However, it fails due to a NameError:'logging' is not defined. The task is marked as failed.                                                                                                                   |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T16:09:14.158663+00:00/task_id=run_etl/attempt=1.log) | The code snippet shows an airflow task instance attempting to run the "run_etl" task within the "load_data_dag" DAG. However, the task fails due to an error in serializing a coroutine object, resulting in a retry being scheduled.                                                                                              |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T15:30:36.132059+00:00/task_id=run_etl/attempt=1.log) | The code snippet represents the execution of a task instance in an Airflow DAG. It shows the dependencies being met, attempts and executions being logged, and the task being run with its associated parameters and environment variables.                                                                                        |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T15:57:21.920666+00:00/task_id=run_etl/attempt=1.log) | The code snippet shows the execution of a task called "run_etl" from the "load_data_dag" DAG. It exports environment variables and makes a call to an endpoint. However, the task fails due to dependencies not being met.                                                                                                         |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T15:57:21.920666+00:00/task_id=run_etl/attempt=2.log) | The code snippet is from a log file of an ETL process. It shows the execution flow, including task dependencies, attempts, and execution details. The code attempts to run the "run_etl" task, exports environment variables, and makes a call to an endpoint. However, the task is not able to be run due to failed dependencies. |
| [attempt=3.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T15:57:21.920666+00:00/task_id=run_etl/attempt=3.log) | The code snippet is logging the execution of a task instance in an Airflow DAG. It shows the start of the task, the execution attempt, the execution command, and the failure due to serialization error with a coroutine object.                                                                                                  |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T16:11:42.310489+00:00/task_id=run_etl/attempt=1.log) | The code snippet shows the execution of a task in an Airflow DAG. The task starts an attempt, executes a Python function called "run_etl", and encounters an error due to JSON serialization of a coroutine object. The task is marked for retry.                                                                                  |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T16:15:53.761785+00:00/task_id=run_etl/attempt=1.log) | The code snippet shows the execution of a task called "run_etl" in a data pipeline. The task is being executed with various dependencies and environment variables. However, the task is not able to run due to failed dependencies.                                                                                               |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T16:15:53.761785+00:00/task_id=run_etl/attempt=2.log) | The provided code snippet shows the execution of a task called "run_etl" in a data pipeline. It attempts to run a Bash command to call an API endpoint. However, the command fails with a non-zero exit code 5, resulting in the task being marked as failed.                                                                      |
| [attempt=1.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T15:45:54.142264+00:00/task_id=run_etl/attempt=1.log) | The code snippet shows a log of a task instance in a workflow. It includes information about task dependencies, attempts, execution, environment variables, and an API call. The task is terminated due to a failed dependency and cannot be run.                                                                                  |
| [attempt=2.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_id=load_data_dag/run_id=manual__2023-07-02T15:45:54.142264+00:00/task_id=run_etl/attempt=2.log) | The code snippet shows the execution of a task called "run_etl" in the "load_data_dag" DAG. The task attempted to call an endpoint, but it was terminated before completion due to running out of memory.                                                                                                                          |

</details>

<details closed><summary>Dag_processor_manager</summary>

| File                                                                                                                                                            | Summary                                  |
| ---                                                                                                                                                             | ---                                      |
| [dag_processor_manager.log](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/airflow/logs/dag_processor_manager/dag_processor_manager.log) | Prompt exceeds max token limit: 1032135. |

</details>

<details closed><summary>Curation</summary>

| File                                                                                                                                | Summary                                                                                                                                                                    |
| ---                                                                                                                                 | ---                                                                                                                                                                        |
| [curation_tags.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/dbt_se/models/curation/curation_tags.sql) | This code snippet retrieves the tag_name, tag_count, and ingestion_timestamp from the'ingestion' source in the'curation' schema, and then displays them in a table format. |

</details>

<details closed><summary>Consumption</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                    |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                        |
| [consumption_weekly_tags_change.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/dbt_se/models/consumption/consumption_weekly_tags_change.sql) | The provided code snippet creates a materialized view named "weekly_tags_change" under the "consumption" schema. It selects all the data from a previously defined calculation named "calculation_weekly_tags_change".     |
| [consumption_daily_tags.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/dbt_se/models/consumption/consumption_daily_tags.sql)                 | This code snippet selects all columns from the view "calculation_daily_tags" in the "consumption" schema and aliases it as "daily_tags". It uses the configuration options "materialized='view'" and "tags='consumption'". |

</details>

<details closed><summary>Calculation</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                       |
| [calculation_weekly_tags_change.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/dbt_se/models/calculation/calculation_weekly_tags_change.sql) | This code retrieves the weekly change in tag counts by subtracting the minimum from the maximum daily count for each tag within the past 7 days. The result is grouped by tag name and sorted in descending order based on the weekly change.             |
| [calculation_daily_tags.sql](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/dbt_se/models/calculation/calculation_daily_tags.sql)                 | The code snippet defines a table and retrieves daily tag counts. It selects the load date, tag name, and the maximum tag count for each day from the base table. The results are grouped by the load date and tag name, and ordered by date and tag name. |

</details>

<details closed><summary>Superset_se</summary>

| File                                                                                                                       | Summary                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                        | ---                                                                                                                                                                                                                                                                                        |
| [superset_config.py](https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT/blob/main/superset_se/superset_config.py) | This code snippet configures Superset by setting parameters such as row limit, secret key, database URI, CSRF protection, and Mapbox API key. It enables CSRF protection and exempts certain endpoints. It also sets a CSRF token that expires in 1 year and allows Mapbox visualizations. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 📦 Installation

1. Clone the StackExchange_API_PKT repository:
```sh
git clone https://github.com/ShubhamPriyadarshi/StackExchange_API_PKT
```

2. Change to the project directory:
```sh
cd StackExchange_API_PKT
```

3. Install the dependencies:
```sh
`ℹ️  INSERT-DESCRIPTION`
```

### 🎮 Using StackExchange_API_PKT

```sh
`ℹ️  INSERT-DESCRIPTION`
```

### 🧪 Running Tests
```sh
`ℹ️  INSERT-DESCRIPTION`
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
