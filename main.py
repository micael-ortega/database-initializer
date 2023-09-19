#!/usr/bin/env python

from DatabaseInitializer import DatabaseInitializer


def main():
    db_initializer = DatabaseInitializer()
    db_initializer.create_connection()
    db_initializer.create_cursor()
    db_initializer.create_table()
    db_initializer.commit_session()
    db_initializer.close_connection()


main()
