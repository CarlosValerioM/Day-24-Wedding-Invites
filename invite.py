#!/usr/bin/env python3
"""
invitations_generator.py - A script for generating personalized wedding invitations.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/26
License: MIT
Dependencies: None (built-in functions only)

Description:
This script generates personalized wedding invitations using predefined data.
It includes:
1. A list of guest names imported from an external module.
2. A predefined invitation template.
3. Writing personalized invitations to a text file.
4. Printing invitations to the console.

Usage:
Run the script:
    python invite.py

Example Output:
- The script reads guest names from a data source.
- It formats each invitation using a template.
- Each invitation is written to a file and displayed in the console.
"""

from data import invitation_data  # Import invitation template
from person import name  # Import guest names

def main():
    names = name  # List of guest names
    data = invitation_data  # Invitation template

    # Open a file to write invitations
    with open("archivo.txt", "w", encoding="utf-8") as file:
        for guest in names:
            file.write(data.format(guest=guest))  # Write formatted invitation

    # Print formatted invitations to the console
    for guest in names:
        print(data.format(guest=guest))

if __name__ == '__main__':
    main()
