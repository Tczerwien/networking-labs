# Skeleton — fill in yourself.
import socket

HOST = '127.0.0.1'
PORT = 9998

# Create a TCP socket
# Bind to (HOST, PORT)
# Listen
# Loop:
#   accept() returns (conn, addr)
#   Loop receiving on conn:
#     Print what was received
#     Echo it back
#     If empty data, break
#   Close conn
