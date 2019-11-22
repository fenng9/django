import paramiko


class ParaClient():
    '''paramiko '''

    def __init__(self, host_info):
        self.host = host_info['host']
        self.port = host_info['port']
        self.username = host_info['username']
        self.passwd = host_info['password']


    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(hostname=self.host,port=self.port,username=self.username,password=self.passwd,timeout=3.0)
        except Exception as err:
            print(err)
            self.client.close()


    def run(self,command):
        stdin, stdout, stderr = self.client.exec_command(command)
        if stderr.read():
            return stderr.read().decode()
        else:
            return stdout.read().decode()
