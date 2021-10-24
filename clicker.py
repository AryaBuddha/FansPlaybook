import sockets

from users import add_ticket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 3000))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    conn.send(b'Waiting for opponent')

    conn1, addr1 = sock.accept()
    conn1.send(b'Waiting for opponent')

    conn.send(b'Connected!')
    conn1.send(b'Connected!')

    conn_count = 0
    conn1_count = 0
    winner = ''

    while True:
        if(conn.recv(1024)) == b'click':
            conn.send(bytes(str(conn1_count), 'utf-8'))
            conn_count += 1

        if(conn1.recv(1024)) == b'click':
            conn1.send(bytes(str(conn_count), 'utf-8'))
            conn1_count += 1
        
        if(abs(conn_count - conn1_count)) > 20:
            if conn_count > conn1_count:
                conn.send(b'You win!')
                conn1.send(b'You lose!')
                winner = conn
            else:
                conn.send(b'You lose!')
                conn1.send(b'You win!')
                winner = conn1
            break

    seat = winner.recv(1024)
    add_ticket(seat)
        

