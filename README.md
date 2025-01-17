# MiTM-Attack-ARP-Spoofing-and-TCP-Hijacking

** Check master branch **

## Overview

  This project aims to explore and demonstrate the concept of Security Protocols in computer networks. The project focuses on ARP Spoofing, a type of Man-in-the-Middle (MiTM) attack, and provides a detailed theoretical explanation of how this attack works, its potential effects, and methods to detect and mitigate it. We have implemented a Proof of Concept (PoC) that demonstrates the attack in a controlled environment using Docker and tcpdump for network traffic capture.


## Objective

  The primary objective of this project is to:

-Explore the concept of ARP Spoofing and its role in network security vulnerabilities.
-Implement a PoC that demonstrates how ARP Spoofing can intercept and alter communication between network devices.
-Provide techniques for detecting and mitigating ARP Spoofing attacks.


## Attack Method: ARP Spoofing

What is ARP Spoofing?

  ARP Spoofing (also known as ARP poisoning) is a technique used by attackers to send false ARP (Address Resolution Protocol) messages over a network. This allows the attacker to associate their MAC address with the IP address of another device (usually a gateway or another device), redirecting the traffic to the attacker’s machine. This attack is typically used in Man-in-the-Middle (MiTM) scenarios, where the attacker can intercept, modify, or even block communication between the devices.


How ARP Spoofing Works

  The attacker sends fraudulent ARP messages to a local network, associating the attacker's MAC address with the IP address of the victim device.
As a result, traffic intended for the victim device is redirected to the attacker's machine.
The attacker can then capture, modify, or even drop network packets between the victim devices.


Effects of ARP Spoofing

-Traffic Interception: The attacker can capture sensitive data, such as passwords, tokens, and other unencrypted traffic.
-Data Manipulation: The attacker can modify the intercepted data before forwarding it to the intended destination.
-Denial of Service: The attacker can disrupt normal communication by dropping or blocking network traffic.


## Mitigation Techniques

-Static ARP Entries: Configure static ARP entries on devices to prevent the ARP cache from being poisoned.
-ARP Spoofing Detection Tools: Use tools such as arpwatch or XArp to monitor for unusual ARP traffic.
-Encryption: Use protocols such as HTTPS, SSH, or VPNs to protect data even if an ARP Spoofing attack is successful.


## Proof of Concept 

Implementation

We have implemented a PoC using Python and Docker to simulate an ARP Spoofing attack. The implementation involves:

Creating a controlled network with Docker containers.
Using Python scripts to perform ARP Spoofing and intercept traffic.
Capturing network traffic using tcpdump to show the attack in action.


Tools Used:

Docker: For containerization and isolating the network environment.
Python: For writing the ARP Spoofing script.
tcpdump: For capturing and analyzing the network traffic.
GitHub: For version control and sharing the PoC code.


## Results

The PoC demonstrates how ARP Spoofing can be successfully executed in a controlled Docker environment. We show how traffic can be intercepted and how the attacker can manipulate or block the communication between two devices.

## Conclusion

This project demonstrates the risks associated with ARP Spoofing and provides insights into how such attacks can be mitigated. The PoC code serves as a practical demonstration of the vulnerability, and the mitigation techniques discussed are crucial in securing networks against such threats.
