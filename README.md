# freezie
Freezie is a command-line tool inspired by hping3, designed for sending customized packets over the network. It allows users to craft packets with specific source and destination addresses, control the number of packets sent, add extra bytes to the data packet, specify the destination port, and enable "freeze" mode for testing network resilience.
## Requirements
Before using Freezie, make sure you have the following requirements installed on your system:
1. **Python 3**: Freezie is implemented in Python, so you need to have Python 3 installed. You can download Python 3 from the official website: **Python.org**
2. **pip3**: pip3 is the package installer for Python 3. If you have Python 3 installed, pip3 usually comes with it by default.
3. **scapy**: Freezie utilizes Scapy, a powerful interactive packet manipulation program. You can install Scapy using pip3 with the following command:
```pip3 install scapy```
## Help Page
To view the available command-line arguments and their usage, run Freezie with the **-h** or **--help** option:
```sudo python3 freezie.py```
The following command-line arguments are supported by Freezie:

    -h, --help: Display the help message and exit.

    -s <source_address>: Set the source address for the packets to be sent.

    -d <destination_address>: Specify the destination address for the packets.

    -c <packet_count>: Set the number of packets to send.

    -b <bytes_to_add>: Add extra bytes to the data packet. This can be used for a heavier impact when testing.

    -p <destination_port>: Specify the destination port for sending the traffic.

    -f: Enable freeze mode. In freeze mode, Freezie sends packets continuously until interrupted, useful for testing network resilience and load handling.
## Example Usage
1. Sending 100 packets to destination 192.168.1.1 from a spoofed address:```sudo python3 freezie.py -s 192.168.1.100 -d 192.168.1.1 -c 100```
2. Sending continuous packets to destination 192.168.1.10 from a spoofed address using freeze mode:```sudo python3 freezie.py -s 192.168.1.100 -d 192.168.1.10 -f```
3. (Be in an administrator terminal before testing this on Windows.) Sending continuous packets to destination 192.168.1.1 from 192.168.1.50 using freeze mode:```python3 freezie.py -s 192.168.1.50 -d 192.168.1.1 -f```
# Remember!
Use freezie responsibly and only on networks you own or have permission to test. Happy crafting!
