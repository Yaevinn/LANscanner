# LANscanner

Python script to scanning open TCP ports in networks.
Script is running in threads. Default = 10 threads.
To speed up scanning incrase threads limit by '-t' parameter (try 100 :) )

## Usage example

#### Show help
python3 lanscanner/portScanner.py -h

#### Run scanner for only one port on one IP
python3 lanscanner/portScanner.py -n 127.0.0.1 -p 443

#### Run scanner for only one port on whole network
python3 lanscanner/portScanner.py -n 192.168.1.0/24 -p 443

#### Run scanner for list of ports on whole network
python3 lanscanner/portScanner.py -n 192.168.1.0/24 -k 80,443,3306

#### Run scanner for port range on one IP
python3 lanscanner/portScanner.py -n 192.168.1.10 -l 1 -m 9999

#### Run scanner in 20 threads
python3 lanscanner/portScanner.py -n 127.0.0.1 -p 443 -t 20

#### Run scanner and save output to file
python3 lanscanner/portScanner.py -n 127.0.0.1 -p 80 --fileoutput