import sys
from opcua import ua, Server

server = Server()

server.set_endpoint('opc.tcp://0.0.0.1:4840/')
server.set_server_name("OPC UA Server")

uri = "http://server"
idx = server.register_namespace(uri)

objects = server.get_objects_node()

object_1 = object.add_object(idx, 'Temperature_Sensor')

discret_1 = object_1.add_variable(idx, 'Temperature', [0,0,0,0,0])

server.start()
