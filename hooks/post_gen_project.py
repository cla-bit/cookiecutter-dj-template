#!/usr/bin/env python

import os
import shutil
import subprocess

# Extract choices
REMOVE_DOCKER: bool = "{{ cookiecutter.use_docker }}".lower() == "no"
REMOVE_CELERY: bool = "{{ cookiecutter.use_celery }}".lower() == "no"
REMOVE_CLOUD_PROVIDER: bool = "{{ cookiecutter.cloud_provider}}".lower() == "none"

CLOUD_PROVIDER: str = "{{ cookiecutter.cloud_provider }}".lower()


def remove_file(filepath) -> None:
    """Safely removes a file relative to the generated project root."""
    full_path = os.path.join(os.getcwd(), filepath)
    if os.path.exists(full_path):
        os.remove(full_path)


def remove_directory(dirpath) -> None:
    """Safely removes a directory relative to the generated project root."""
    full_path = os.path.join(os.getcwd(), dirpath)
    if os.path.exists(full_path):
        shutil.rmtree(full_path)


def clean_docker_files() -> None:
    """Removes Docker-related files if the user opted out."""
    print("Removing Docker configuration files...")
    remove_file("compose.yaml")
    remove_file("Dockerfile")
    remove_file(".dockerignore")


def clean_celery_files() -> None:
    print("Removing Celery configuration components...")
    remove_file(os.path.join("configs/library_configs", "celery.py"))


def clean_aws_files() -> None:
    print("Removing AWS Cloud deployment configurations...")
    remove_file(os.path.join("configs/library_configs/deploy", "aws.py"))


def clean_azure_files() -> None:
    print("Removing AWS Cloud deployment configurations...")
    remove_file(os.path.join("configs/library_configs/deploy", "azure.py"))


def init_git():
    """Initializes a Git repository in the generated project directory."""
    pass


def handle_conditional_files() -> None:
    # If a user does not want Docker, remove Docker configuration files
    if REMOVE_DOCKER:
        clean_docker_files()

    # If a user does NOT want Celery, remove Celery configuration files
    if REMOVE_CELERY:
        clean_celery_files()

    # If cloud provider is None, clean up all cloud-specific deployment setups
    if REMOVE_CLOUD_PROVIDER:
        print("Removing Cloud deployment configurations...")
        clean_aws_files()
        clean_azure_files()
        remove_directory("configs/library_configs/deploy")
    else:
        # Extra cleanup: If they chose AWS, delete Azure files, and vice versa
        if CLOUD_PROVIDER == "aws":
            clean_azure_files()
        if CLOUD_PROVIDER == "azure":
            clean_aws_files()


def main() -> None:
    handle_conditional_files()

    print("\n🎉 Project files generated and cleaned up successfully!")
    print("To start developing, run the following commands:")
    print(f" 1. cd {{ cookiecutter.project_slug }}")
    print("  2. python/python3 -m venv .venv")
    print("  3. activate your virtual environment pending on your OS")
    print("  4. poetry install")


if __name__ == "__main__":
    main()
