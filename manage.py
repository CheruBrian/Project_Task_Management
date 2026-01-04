#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_root)

    # Check which settings module to use
    if os.path.exists(os.path.join(project_root, 'task_management', 'settings.py')):
        settings_module = 'task_management.settings'
    else:
        settings_module = 'settings'

    # Set the environment variable if it's not already set, or override it with the correct one?
    # We are going to set it to what we determined.
    os.environ['DJANGO_SETTINGS_MODULE'] = settings_module

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()