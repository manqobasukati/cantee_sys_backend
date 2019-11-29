from application import create_app
import socket    

app = create_app()

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 

print(IPAddr)

if __name__ == "__main__":
    # app.run(str(IPAddr))
     app.run(host='127.0.0.1')
