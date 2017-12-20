import socket, sys

def getHostIP(domain_name):
    ip_addr = socket.gethostbyname(domain_name)
    return ip_addr

if __name__ == '__main__':
    domain = sys.argv[1]
    print('Address IP %s domain is %s' % (domain, getHostIP(domain)))
