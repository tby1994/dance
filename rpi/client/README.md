### Running client.py manually

1. Create a python virtual environment if you haven't already with `python3 -m venv client`.
2. `cd` into the folder and `pip3 install pycrypto`.
3. `python3 client.py <ip_address> <port> <aes_key>` will start a client that connects to the server at the port/address specified, encrypted with the AES key in cipher mode. Press <kbd>Enter</kbd> after starting the client to send a test message to the server and exit. 
> If you are running the server on your laptop, ensure you use the IP address on the network the pi is connected to.