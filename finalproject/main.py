# -*- coding: utf-8 -*-
"""
Edward Goldstein
"""

from eligibility import immigration_status
from help_menu import help_menu


def main():
    immigration_eligibility = immigration_status()
    help_menu(immigration_eligibility)

if __name__ == "__main__":
    main()
