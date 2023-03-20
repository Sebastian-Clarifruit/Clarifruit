import time
from utils_new import get_inspections, delete_inspection, import_inspections
import json
import requests
import os


def run_script():
    sebastián_company = 403305
    result = get_inspections(sebastián_company)
    print('got all inspections, about to iterate them, count:' + str(len(result)))
    iterate_inspections(result)


def iterate_inspections(result):
    for i in result:
        id_ = i["id"]
        delete_inspection(id_)
    import_inspections()


if __name__ == '__main__':
    run_script()
