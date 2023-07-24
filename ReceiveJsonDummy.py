import json
import socket

def tcp_ctrl_server():

    UDP_IP = "0.0.0.0"  # Endereço IP local
    UDP_PORT = 8001 # Porta para escutar
    
    global defined

    global s

    # Cria um objeto de socket TCP/IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Liga o socket ao endereço e porta especificados
    s.bind((UDP_IP, UDP_PORT))

    # Define o número máximo de conexões pendentes na fila


    print(f'Aguardando conexões em {UDP_IP}:{UDP_PORT}')


    while True:

        # Aguarda por conexões
        data, addr = s.recvfrom(1024)
        json_data = data.decode().split('/n')[0]
        # Recebe dados do cliente
        obj = json.loads(json_data)
        print(obj)

        # objects = []

        # for obj_str in data.decode().split('\n'):
        #     if obj_str:
        #         obj = json.loads(obj_str)
        #         objects.append(obj)
        # print(objects)

tcp_ctrl_server()

defined = False

while True:
    if (defined):
        print(defined)