#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A2SL.settings')
    
    # Get the port from the environment variables
    port = os.environ.get('PORT', '8000')  # Default to 8000 if PORT is not set
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Check if the runserver command is being used and bind to 0.0.0.0:<PORT>
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        sys.argv[2] = f'0.0.0.0:{port}'
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
