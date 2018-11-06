import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #サーバーを指定
    s.connect(('127.0.0.1'))
    #サーバーにメッセージを送る
    s.sendall(b'hello')
    #ネットワークのバッファサイズは1024。サーバーから文字列を取得する
    data = s.recv(1024)
    #
    print(repr(data))
