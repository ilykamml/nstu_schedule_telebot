import json
import os
from idlelib.iomenu import encoding

GROUPS = 'groups.json'
STUDENTS = 'students.json'

def load_groups():
    if os.path.exists(GROUPS):
        with open(GROUPS, 'r', encoding='utf-8') as file:
            db = json.load(file)
            if 'groups' not in db:
                db['groups'] = []
            return db
    return {'groups': []}


def load_students():
    if os.path.exists(STUDENTS):
        with open(STUDENTS, 'r', encoding='utf-8') as file:
            db = json.load(file)
            if 'students' not in db:
                db['students'] = []
            return db
    return {'students': []}