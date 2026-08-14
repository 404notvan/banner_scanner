import socket
import threading
import sys
import argparse

parser = argparse.ArgumentParser(description="Advanced Port Scanner")
parser.add_argument("target",help="Host Or IP Target")
parser.add_argument("--start-port","-s",default=1,type=int,help="Value Start Port")
parser.add_argument("--end-port","-e",default=1024,type=int,help="Value End Port")
parser.add_argument("--timeout","-t",default=1.0,type=float,help="Timeout Per Port In Second")

args = parser.parse_args()

class PortScanner:
    def __init__(self,target,timeout=1.0):
        self.target = target
        self.timeout = timeout
        self.open_ports = []
    
    def check_port(self,port):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(self.timeout)
            try:
                s.connect((self.target,port))
                return True
            except (socket.timeout,ConnectionRefusedError):
                return False
            
    def _scan_worker(self,port):
        if self.check_port(port):
            self.open_ports.append(port)
            print(f"[+] Port {port} OPEN")
        
    def scan(self,start_port,end_port):
        threads = []
        for port in range(start_port,end_port + 1):
            t = threading.Thread(target=self._scan_worker,args=(port,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    
    def grab_banner(self,port):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(self.timeout)
            try:
                s.connect((self.target,port))
                banner = s.recv(1024)
                return banner.decode(errors="ignore")
            except (socket.timeout,ConnectionRefusedError): 
                return None
                
    
try:
    host_check = socket.gethostbyname(args.target)
except socket.gaierror:
    print(f"[!] The Host You Are Looking For Was Not Found")
    sys.exit(1)
            
if args.start_port > args.end_port:
    print("[!] The Start Port Value Is Greater Than The End Value")
    sys.exit(1)
    

scanner = PortScanner(args.target,args.timeout)

try:
    scanner.scan(args.start_port,args.end_port)
    for port in scanner.open_ports:
        banner = scanner.grab_banner(port)
        if banner:
            print(f"[+] Banner Port {port} : {banner}")
except KeyboardInterrupt:
    exit(1)