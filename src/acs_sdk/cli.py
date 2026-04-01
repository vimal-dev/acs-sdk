"""Command-line interface module for Apache CloudStack SDK.

This module provides CLI functionality for interacting with Apache CloudStack
from the command line, offering a convenient alternative to programmatic usage.
"""


def main():
    """Main entry point for the CloudStack CLI.

    This function serves as the command-line interface entry point for the
    Apache CloudStack SDK. It's typically invoked when the acs-sdk command
    is run from the terminal.

    Example:
        $ acs-sdk list-users
        $ acs-sdk create-vm --template ubuntu --zone us-west-1
    """
    print("Apache CloudStack CLI")
