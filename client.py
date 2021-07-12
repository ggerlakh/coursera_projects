import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((host, port))

    def __del__(self):
        self.sock.close()

    def put(self, metric, metric_value, timestamp=0):
        try:
            int(timestamp)
            float(metric_value)
            if timestamp == 0:
                timestamp = int(time.time())
            self.sock.sendall(f"put {metric} {metric_value} {timestamp}\n".encode("utf-8"))
            put_response = self.sock.recv(1024)
            put_response = put_response.decode("utf-8")
            if put_response == 'error\nwrong command\n\n':
                raise ClientError()
        except Exception:
            raise ClientError()

    def get(self, metric):
        try:
            output_dict = {}
            l = list()
            self.sock.sendall(f"get {metric}\n".encode("utf-8"))
            get_response = self.sock.recv(1024)
            get_response = get_response.decode("utf-8")
            if get_response != 'ok\n\n':
                l = get_response.split('\n')[1:-2]
                if get_response.split('\n')[0] != 'ok' or get_response.split('\n')[-1] != '' or get_response.split('\n')[-2] != '':
                    raise ClientError()
                for elem in l:
                    if metric != '*':
                        if elem.split(' ')[0] != metric:
                            raise ClientError()
                    else:
                        if type(elem.split(' ')[0]) != str:
                            raise ClientError()
                    output_dict[elem.split(' ')[0]] = []
                for elem in l:
                    output_dict[elem.split(' ')[0]].append((int(elem.split(' ')[2]), float(elem.split(' ')[1])))
                for key in output_dict:
                    output_dict[key].sort() 
            return output_dict
        except Exception:
            raise ClientError()
