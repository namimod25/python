import socket

PC_name = socket.gethostname()

def selamat_datang():
    
    
    style = "-" * (len(PC_name) + 6)
    print(style)
    print(f"{PC_name}")
    print(style)