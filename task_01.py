#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This is Week5 synthesizing task_01."""

import datetime

CURDATE = None


def get_current_date():
    """Return current date from datetime module.

    When this function called without passing any argument, it will return
    current date.

    Args:
        get_date(mix): The datetime module will be measured.
    Returns:
        date(int): If the datetime module measured then it will return current
        date.
    Example:
        >>> get_current_date()
        datetime.date(2015, 9, 27)
        >>> CURDATE
        datetime.date(2015, 9, 27)
    """
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
