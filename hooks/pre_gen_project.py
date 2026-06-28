import re
import sys

# Pull variables using Jinja2 context syntax
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
CLOUD_PROVIDER = "{{ cookiecutter.cloud_provider }}"
USE_CELERY = "{{ cookiecutter.use_celery }}"

# Regex for a valid Python package/module name
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'


def validate_slug() -> None:
    if not re.match(MODULE_REGEX, PROJECT_SLUG):
        print(f"ERROR: '{PROJECT_SLUG}' is not a valid Python identifier!")
        print("The project name must start with a letter and contain only alphanumeric characters or underscores.")
        sys.exit(1)


def validate_architecture() -> None:
    # Celery required and infrastructure architecture is not required
    if USE_CELERY == "yes" and CLOUD_PROVIDER == "None":
        print("WARNING/ERROR: You enabled Celery but selected no Cloud Provider.")
        print("--> Architecture Info: Setting up local Celery configuration without cloud engine integration.")
        print("Production Celery setups require a message broker (Redis/SQS) usually provisioned via cloud.")
        return

    # Celery required and infrastructure architecture is required
    elif USE_CELERY == "yes" and CLOUD_PROVIDER != "None":
        print(f"--> Architecture Info: Configuring Celery alongside {CLOUD_PROVIDER} configurations.")
        return

    # Celery is not required and infrastructure architecture is required
    elif USE_CELERY == "no" and CLOUD_PROVIDER != "None":
        print(f"❌ ARCHITECTURE ERROR: Cloud provider '{CLOUD_PROVIDER}' was chosen, but Celery is disabled.")
        print("This template requires Celery to be enabled if a Cloud Provider is specified.")
        sys.exit(1)

    # Celery is not required and Infrastructure architecture is not required
    else:
        return


if __name__ == "__main__":
    validate_slug()
    validate_architecture()