#!/usr/bin/env python
import os
import sys


def main():
    """Run administrative tasks."""
    # Try to auto-detect the settings module
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check if task_management/settings.py exists
    if os.path.exists(os.path.join(current_dir, 'task_management', 'settings.py')):
        settings_module = 'task_management.settings'
    # Check if settings.py is in root
    elif os.path.exists(os.path.join(current_dir, 'settings.py')):
        settings_module = 'settings'
    else:
        # Default to what Render expects
        settings_module = 'settings_module.render'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

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