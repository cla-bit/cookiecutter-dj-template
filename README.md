# Django Enterprise API Starter Template

A highly scalable, production-ready backend architecture blueprint powered by Django 6.0 and Django REST Framework (DRF). 
This template streamlines microservice or modular monolithic setups, offering pre-configured workflows for background tasks, structured correlation logging, API schema documentation, and containerization structures.

---

## 🏗️ Core Architecture Overview

This template enforces a strict separation of concerns, providing architectural scaffolding for modern backend projects:

- **Framework Core**: Choice of Django 6.0 or 5.2 running under Python 3.14/3.13/3.12.

- **API Documentation**: OpenAPI 3.0 schema generation natively integrated with drf-spectacular (Swagger UI & Redoc).

- **Asynchronous Processing**: Built-in decoupled configurations for Celery and Redis for task management and cron scheduling.

- **Observable Tracking**: Integrated with ``django-guid`` to automatically inject unique Correlation IDs across all HTTP request cycles and downstream background Celery executions.

- **Environment Execution**: Clean fallback paths between lightweight local SQLite workflows and robust PostgreSQL engines.


## 🛠️ System Prerequisites & Tooling

Before generating a project from this blueprint, ensure your local workstation satisfies the following requirements:

- Cookiecutter installed globally. This is required to parse this template, run the system-check hooks, and build the project directory.
    ```shell
    # Recommended: Install via pipx to keep your global python environment clean
    pipx install cookiecutter
    
    # Alternative: Standard global pip installation
    pip install cookiecutter
    ```

    **💡 Note on Lifecycle:** Cookiecutter is only an initiation tool. It runs for a few seconds to compile the code workspace. 
Once your project is generated, Cookiecutter is no longer needed; it does not need to be added to your dependencies or installed by team members who clone your finished repository later.


- Python 3.12+ installed globally.

- Git version control system configured.

- Poetry dependency manager globally accessible (pipx install poetry or standard installer script).

- Docker - installed and running. Optional if you want to use docker

- Postgresql CLI / pgAdmin - installed. Optional if you want to use Postgresql.


## 🚀 How to Generate a New Project

This command clones the template in your root directory.
```shell
cookiecutter gh:cla-bit/cookiecutter-dj-template
```

## 💻 Local Environment Setup

To keep project generation lightweight, dependency compilation is handed entirely to the developer. Follow these steps once your custom workspace folder has been emitted.

1. **Initialize the Environment & Poetry Connection**
   
    Navigate into your generated folder *(using your chosen project_slug)* and build a local isolated virtual environment:

    ```shell
    # Change directory to your new codebase workspace
    cd your_project_slug
    
    # Create a standard, local virtual environment (Windows)
    python -m venv .venv

    # Create a standard, local virtual environment (Ubuntu)
    python3 -m venv .venv
    ```

2. **Install Project Dependencies**
    
    Run the installation script to process package boundaries and build your lockfile:

3. **Run Environment Verifications**

    Verify your installation environment context by launching your application server:

    ```shell
    # Check if all your configurations are ok
    python manage.py check
        
    # Boot up the local development web server
    python manage.py runserver
    ```

## 📂 Configuration Options & Context Matrix

When initializing the template, you will control project scaffolding via the following interactive variables:

| Context Key             | Default Options  | Architectural Impact                                                                                                                                                                     |
|-------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| use_djangorestframework | yes, no          | Conditionally structures CORS and API payload rendering engines.                                                                                                                         |
| use_docker              | yes, no          | Provisions base multi-stage Dockerfiles and compose orchestration manifests.                                                                                                             |
| use_postgresql          | yes, no          | Dynamically alters `settings/development.py` between a production-ready database engine driver and a lightweight SQLite footprint. If no, following database prompts are cleanly skipped. |
| use_celery              | yes, no          | Generates structural background configurations `configs/celery.py`, registers middleware hooks, and wires connection retries.                                                            |
| use_drf_spectacular     | yes, no          | Injects auto-updating Swagger/Redoc endpoints directly into system-level routing paths `configs/urls.py`.                                                                                 |
| cloud_provider          | None, AWS, Azure | Retains cloud infrastructure provisioning folders or dynamically clips irrelevant operational files post-generation.                                                                                                                                                                                         |

