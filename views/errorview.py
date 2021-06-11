#! /usr/bin/env python3
# coding: utf-8


class ErrorView:

    @staticmethod
    def get_alpha_message_error(value):
        print(f"La valeur '{value}' doit être au format alphabétique")

    @staticmethod
    def get_date_message_error():
        print("La date doit être au format jj-mm-aaaa")

    @staticmethod
    def get_int_message_error(value):
        print(f"L'entrée '{value}' doit être un entier numérique")

