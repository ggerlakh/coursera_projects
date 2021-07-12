import asyncio


def run_server(host, port):
    class ClientServerProtocol(asyncio.Protocol):

        server_data = {}

        #def __init__(self):
            #self.d = {}

        def connection_made(self, transport):
            self.transport = transport

        def data_received(self, data):
            addr = self.transport.get_extra_info("peername")[1]
            message = data.decode()
            if '\r' in message:
                message = message.replace('\r', '')
            #print(f"Получены данные {message} от {addr}")
            if message.split(' ')[0] == 'put':
                if len(message.split(' ')) == 4 and message.split('\n')[1] == '' and len(message.split('\n')) == 2:
                    try:
                        float(message.split(' ')[2])
                        int(message.split(' ')[3].split('\n')[0])
                        message = message.split(' ')[0] + " " + message.split(' ')[1] + " " + str(float(message.split(' ')[2])) + " " + message.split(' ')[3]
                        #print(f"message: {message}")
                        try:
                            #print("message.split(' ')[3]:", message.split(' ')[3].split('\n')[0])
                            #print("self.server_data[port]:", self.server_data[port])
                            if message.split(' ')[3].split('\n')[0] in self.server_data[port] and message.split(' ')[1] in self.server_data[port]:
                                for elem in self.server_data[port].split('\n'):
                                    if elem != '':
                                        if message.split(' ')[3].split('\n')[0] == elem.split(' ')[2].split('\n')[0] and message.split(' ')[1] == elem.split(' ')[0]:
                                            #print("True")
                                            self.server_data[port] = self.server_data[port].replace(elem + '\n', ' '.join(message.split(' ')[1:]))
                                if ' '.join(message.split(' ')[1:]) not in self.server_data[port] and ' '.join(message.split(' ')[1:]) not in self.server_data.values():
                                    self.server_data[port] += ' '.join(message.split(' ')[1:])
                                self.transport.write("ok\n\n".encode())
                                #print("Отапрвлено: ok\n\n")
                            else:
                                if ' '.join(message.split(' ')[1:]) not in self.server_data[port] and ' '.join(message.split(' ')[1:]) not in self.server_data.values():
                                    self.server_data[port] += ' '.join(message.split(' ')[1:])
                                self.transport.write("ok\n\n".encode())
                                #print("Принято:", ' '.join(message.split(' ')[1:]))
                                #print("Отправлено: ok\n\n")
                        except KeyError: 
                            self.server_data[port] = ' '.join(message.split(' ')[1:])
                            self.transport.write("ok\n\n".encode())
                            #print("Отправлено: ok\n\n")
                    except ValueError:
                        self.transport.write("error\nwrong command\n\n".encode())
                        #print("Отправлено: error\nwrong command\n\n")
                else:
                    self.transport.write("error\nwrong command\n\n".encode())
                    #print("Отправлено: error\nwrong command\n\n")
            elif message.split(' ')[0] == 'get':
                if len(message.split(' ')) == 2 and message.split('\n')[1] == '' and len(message.split('\n')) == 2:
                    l = ''.join(list(self.server_data.values()))
                    #print(f"l:{l}")
                    #print(f"message: {message}")
                    #print("message.split(' ')", message.split(" "))
                    if message.split(' ')[1].split('\n')[0] == '*':
                        try:
                            self.transport.write(f"ok\n{l}\n".encode())
                            #print(f"Отправлено: ok\n{l}\n")
                        except KeyError:
                            self.transport.write("ok\n\n".encode())
                            #print("Отправлено: ok\n\n")
                    elif message.split(' ')[1].split('\n')[0] in l:
                        get_list = []
                        for item in l.split('\n'):
                            if message.split(' ')[1].split('\n')[0] in item:
                                if item not in get_list:
                                    #print(f"item:{item}")
                                    item += '\n'
                                    get_list.append(item)
                        res = ""
                        def sort_timestamp(input_val):
                            return int(input_val.split(' ')[2].split('\n')[0])
                        get_list.sort(key=sort_timestamp)
                        for i in range(len(get_list)):
                            #print("message.split(' ')[1]:", message.split(' ')[1])
                            #print("get_list[i].split(' ')[0]:", get_list[i].split(' ')[0])
                            #print(f"{message.split(' ')[1]} == {get_list[i].split(' ')[0]}", message.split(' ')[1] == get_list[i].split(' ')[0])
                            if message.split(' ')[1].split('\n')[0] == get_list[i].split(' ')[0]:
                                res += get_list[i]
                                #print(res)
                        self.transport.write(f"ok\n{res}\n".encode())
                        #print("get_list:", get_list)
                        #print(f"Отправлено:ok\n{res}\n")
                    elif message.split(' ')[1].split('\n')[0] not in l:
                        self.transport.write("ok\n\n".encode())
                        #print("Отправлено: ok\n\n")
                else:
                    self.transport.write("error\nwrong command\n\n".encode())
                    #print("Отправлено: error\nwrong command\n\n")
            else:
                self.transport.write("error\nwrong command\n\n".encode())
                #print("Отправлено: error\nwrong command\n\n")

    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
