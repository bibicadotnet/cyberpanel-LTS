import signal
import sys
import ssl
from SimpleWebSocketServer import WebSocket, SimpleSSLWebSocketServer
import paramiko
import os
import json
import threading as multi
import time

class SSHServer(multi.Thread):

    def loadPublicKey(self):
        pubkey = '/root/.ssh/cyberpanel.pub'
        data = open(pubkey, 'r').read()
        authFile = '/root/.ssh/authorized_keys'

        checker = 1

        try:
            authData = open(authFile, 'r').read()
            if authData.find(data) > -1:
                checker = 0
        except:
            pass

        if checker:
            writeToFile = open(authFile, 'a')
            writeToFile.writelines(data)
            writeToFile.close()

    def __init__(self, websocket):
        multi.Thread.__init__(self)
        self.sshclient = paramiko.SSHClient()
        self.sshclient.load_system_host_keys()
        self.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        k = paramiko.RSAKey.from_private_key_file('/root/.ssh/cyberpanel')

        ## Load Public Key
        self.loadPublicKey()

        self.sshclient.connect('127.0.0.1', 22, username='root', pkey=k)
        self.shell = self.sshclient.invoke_shell(term='xterm')
        self.shell.settimeout(0)

        self.websocket = websocket

    def recvData(self):
        while True:
            try:
                if os.path.exists(self.websocket.verifyPath):
                    if self.shell.recv_ready():
                        self.websocket.sendMessage(self.shell.recv(9000).decode("utf-8"))
                    else:
                        time.sleep(0.1)
            except BaseException, msg:
                time.sleep(2)

    def run(self):
        try:
            self.recvData()
        except BaseException, msg:
            print(str(msg))


class WebTerminalServer(WebSocket):

   def handleMessage(self):
       try:
           data = json.loads(self.data)
           if str(self.data).find('"tp":"init"') > -1:
               self.verifyPath = str(data['data']['verifyPath'])
           else:
               if os.path.exists(self.verifyPath):
                   self.shell.send(str(data['data']))
       except:
           pass

   def handleConnected(self):
      self.sh = SSHServer(self)
      self.shell = self.sh.shell
      self.sh.start()

   def handleClose(self):
      try:
          os.remove(self.verifyPath)
      except:
          pass


if __name__ == "__main__":
   pidfile = '/usr/local/CyberCP/WebTerminal/pid'

   writeToFile = open(pidfile, 'w')
   writeToFile.write(str(os.getpid()))
   writeToFile.close()

   server = SimpleSSLWebSocketServer('0.0.0.0', '5678', WebTerminalServer,  '/usr/local/lscp/conf/cert.pem', '/usr/local/lscp/conf/key.pem', version=ssl.PROTOCOL_TLSv1)

   def close_sig_handler(signal, frame):
      server.close()
      sys.exit()

   signal.signal(signal.SIGINT, close_sig_handler)
   server.serveforever()