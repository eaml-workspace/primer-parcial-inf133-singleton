from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs, urlparse
import random

partidas = {}

class IDs:
    def id_partida(partidas):
        ids= list(partidas.keys())
        ids.sort()
        if ids==[]:
            ids.append(1)
            return ids[-1]
        else:
            a=ids[-1]+1
            ids.append(a)
            return a

class Player:
    _instances = None
    
    def __init__(cls, nombre, number_guess):
        number_guess = random.randrange(1,100)
        if not cls._instances:
            cls._instances = super().__new__(cls)
            cls._instances.name = nombre
            cls._instances.number_guess = number_guess
        return cls._instances
    
    def to_dict(self):
        return {"player": self._instances.name(), "number": self._instances.number_guess()}

class Guess:
    def __init__(self):
        self.player= Player

    def new_player(self, name):
        Player (name)
        self.player(nombre=name)
        
    def guess_attempt(self, number):
        number_guess= self.player.number_guess
        

class HTTPDataHandler(BaseHTTPRequestHandler):
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_header("Content-type", "application/json")
        handler.send_response(status)
        handler.end_headers()
        handler.wfile.write(json.dumps(status, data).encode("utf-8"))
    
    """@staticmethod
    def handle_reader(handler, data):
        content_length = int(self.headers(["Content-Length"]))
        post_data = rfile.read(data)"""

class PlayerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == ("/guess"):
            HTTPDataHandler.handle_response(self, 200, partidas)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error":"Ruta inexistente"})
    def do_POST(self):
        if self.path.startswith("/guess/"):
            print()