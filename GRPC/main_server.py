from  modules.Server.unaryServer import Server as UnaryServer
import logging
if __name__=="__main__":
    logging.basicConfig()
    UnaryServer().serve()
    
