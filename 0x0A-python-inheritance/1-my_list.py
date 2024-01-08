#!/usr/bin/python3
""" a class MyList"""


class MyList(list):
    """
    represnt a class MyList
    """
    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
