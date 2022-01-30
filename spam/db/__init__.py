import json
from operator import index
from re import S
from pymongo import MongoClient
import os


class DB:

    def __init__(self, mongo_url) -> None:
        self.db_url = mongo_url
        self.vanitas = MongoClient(self.db_url)['Vanitas']['VANITASMODE']
        self.sibyl = MongoClient(self.db_url)['Sibyl']['SIBYLMODE']

    def is_vanitas(self, chat_id: int) -> bool:
        x = self.vanitas.find_one({"chat_id": chat_id})
        if x:
            return True
        return False

    def set_vanitas(self, chat_id: int):
        set_vanitas = self.is_vanitas(chat_id)
        if set_vanitas:
            return
        return self.vanitas.insert_one({"chat_id": chat_id})

    def rm_vanitas(self, chat_id: int):
        rm_vanitas = self.is_vanitas(chat_id)
        if not rm_vanitas:
            return
        return self.vanitas.delete_one({"chat_id": chat_id})


    def is_sibyl(self, chat_id: int) -> bool:
        x = self.sibyl.find_one({"chat_id": chat_id})
        if x:
            return True
        return False

    def set_sibyl(self, chat_id: int):
        set_sibyl = self.is_sibyl(chat_id)
        if set_sibyl:
            return
        return self.sibyl.insert_one({"chat_id": chat_id})

    def rm_sibyl(self, chat_id: int):
        rm_sibyl = self.is_sibyl(chat_id)
        if not rm_sibyl:
            return
        return self.sibyl.delete_one({"chat_id": chat_id})

   
