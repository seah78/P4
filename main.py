#! /usr/bin/env python3
# coding: utf-8

from controllers.applicationcontroller import ApplicationController

def main():
    app = ApplicationController()
    app.start()

if __name__ == "__main__":
    main()