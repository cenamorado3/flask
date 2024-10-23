import psutil
from flask_restful import Resource
from flask import jsonify

class Health(Resource):
    def get(self):
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return jsonify({
            "CPU": f'{psutil.cpu_percent(interval=1)}%',
            "MEM": f'{mem.used / (1024 ** 3):.2f} / {mem.total / (1024 ** 3):.2f} GB',
            "DISK": f'{disk[1] / (1024 ** 3):.2f} / {disk[2] / (1024 ** 3):.2f} GB'
        })