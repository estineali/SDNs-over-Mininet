from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class MyNet():
    def __init__(self): 
        self.net = Mininet()
        self.c0 = self.net.addController('c0')
        self.currentHostId = 1
        self.currentSwitchId = 1
        setLogLevel('info')
    
    def addHost(self):
        host = self.net.addHost("h" + str(self.currentHostId))
        self.currentHostId += 1
        return host
    
    def addSwitch(self):
        switch = self.net.addSwitch("s" + str(self.currentSwitchId))
        self.currentSwitchId += 1
        print("add switch in mininet")
        return switch
    
    def addLink(self, node1, node2):
        self.net.addLink(node1, node2)

    def start(self):
        self.net.start() 

    def pingAll(self):
        self.net.pingAll()      
    
    def stop(self):
        self.net.stop()
    
    def startCLI(self):
        CLI(self.net)
    
    def dumpInfo(self):
        dumpNodeConnections(self.net.hosts)


def simpleTest():
    net = MyNet()
    h1 = net.addHost()
    h2 = net.addHost()
    s1 = net.addSwitch()
    s2 = net.addSwitch()
    net.addLink(s1, h1)
    net.addLink(s2, h1)
    net.addLink(s1, h2)
    net.start()
    net.dumpInfo()
    net.pingAll()
    net.startCLI()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()