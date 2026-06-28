#!/usr/bin/env python

import shutil
import subprocess
import sys


def check_command_exists(command: str) -> bool:
    """Check if a command-line tool is available in the system PATH."""
    return shutil.which(command) is not None


def check_python_version() -> bool:
    """Ensure Python is available (which it is, running Cookiecutter), but log it."""
    print("Checking Python installation...")
    if check_command_exists("python3") or check_command_exists("python"):
        # Extra: Get major/minor version string
        version = sys.version.split()[0]
        print(f"  - Found Python version: {version} ✅")
        return True
    print("  - ERROR: Python execution environment not detected. ❌")
    return False


def check_git() -> bool:
    """Check if Git is installed."""
    print("Checking Git installation...")
    if check_command_exists("git"):
        try:
            res = subprocess.run(["git", "--version"], capture_output=True, text=True, check=True)
            print(f"  - Found Git: {res.stdout.strip()} ✅")
            return True
        except subprocess.SubprocessError:
            pass
    print("  - ERROR: Git is not installed or not in system PATH. ❌")
    return False


def check_poetry() -> bool:
    """Check if the Poetry dependency manager is installed."""
    print("Checking Poetry installation...")
    if check_command_exists("poetry"):
        try:
            res = subprocess.run(["poetry", "--version"], capture_output=True, text=True, check=True)
            print(f"  - Found Poetry: {res.stdout.strip()} ✅")
            return True
        except subprocess.SubprocessError:
            pass
    print("  - ERROR: Poetry is not installed or not in system PATH. ❌")
    return False


def check_docker() -> bool:
    """Check if Docker CLI is installed and the daemon is actively running."""
    print("Checking Docker installation...")
    if not check_command_exists("docker"):
        print("  - ERROR: Docker CLI is not installed. ❌")
        return False

    try:
        # Check if docker daemon is reachable
        subprocess.run(["docker", "info"], capture_output=True, check=True)
        print("  - Found Docker (Engine daemon is running) ✅")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("  - ERROR: Docker CLI found, but the Docker daemon is NOT running. ❌")
        print("Please start Docker before running this template.")
        return False


def check_postgresql() -> bool:
    """Check if PostgreSQL client tools (psql) or engine tools are installed."""
    print("Checking PostgreSQL tools...")
    # Checking for 'psql' (CLI client) or 'postgres' (Server binary)
    if check_command_exists("psql") or check_command_exists("postgres"):
        try:
            res = subprocess.run(["psql", "--version"], capture_output=True, text=True, check=True)
            print(f"  - Found PostgreSQL Client CLI: {res.stdout.strip()} ✅")
            return True
        except subprocess.SubprocessError:
            print("  - Found PostgreSQL binary tools. ✅")
            return True

    print("  - ERROR: PostgreSQL binaries (psql/postgres) were not detected in system PATH. ❌")
    return False


def main() -> None:
    print("=" * 60)
    print("System Check: Validating Environment Prerequisites")
    print("=" * 60)

    critical_checks = {
        "Python": check_python_version(),
        "Git": check_git(),
        "Poetry": check_poetry(),
    }

    conditional_checks = {
        "Docker": check_docker(),
        "PostgreSQL": check_postgresql()
    }

    print("-" * 60)

    # Process Hard Failures
    failed_critical = [name for name, passed in critical_checks.items() if not passed]
    if failed_critical:
        print("❌ CRITICAL ERROR: Missing core system environment requirements!")
        print(f"The template requires these dependencies to build: {', '.join(failed_critical)}")
        print("Aborting project generation workflow.")
        print("=" * 60)
        sys.exit(1)  # Terminate early before prompting user inputs

    # Track Soft Failures
    failed_conditional = [name for name, passed in conditional_checks.items() if not passed]

    if failed_conditional:
        print("⚠️  NOTICE: Missing conditional dependencies detected:")
        print(f"  - {', '.join(failed_conditional)}")
        print("\n  You can safely continue. When prompted by Cookiecutter, make sure to")
        print("  select 'no' for features utilizing these tools if you cannot run them.")
        print("-" * 60)


    print("🎉 All core pre-requisite dependencies satisfied! Moving to project setup prompts...")
    print("=" * 60)


if __name__ == "__main__":
    print("Checking system prerequisites...")
    main()
