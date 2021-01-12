## ARP Shenanigans

### HOWTO

The terminal provides three tmux windows by default.  Copy and paste the three "stepN" bash scripts to files of the same name in the terminal.  Then:

1. In the first tmux window, run [step1.bash](step1.bash).
2. In the second tmux window, run [step2.bash](step2.bash).
3. In the third tmux window, run [step3.bash](step3.bash).
4. When you see the log of the deb package downloaded in the first tmux window, run the nc command shown in third tmux window.


### File Descriptions

* [arp-resp.py](arp-resp.py): provided template for ARP responder
* [arp.py](arp.py): ARP responder code
* [dns-resp.py](dns-resp.py): provided template for DNS responder
* [dns.py](dns.py): DNS responder code
* [show_arp.py](show_arp.py): Display what the sample ARP query and response PCAPS look like to Scapy
* [show_dns.py](show_dns.py): Display what the sample DNS query and response PACSP look like to Scapy
* [step1.bash](step1.bash) - Build and host the Debian package for my version of Jack's backdoor
* [step2.bash](step2.bash) - Run the DNS responder script
* [step3.bash](step3.bash) - Run the ARP responder script
