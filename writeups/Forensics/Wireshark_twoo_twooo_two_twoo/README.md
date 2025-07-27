# Nicole Kazantsev CTF Wireshark 
1. I opened the `.pcap` file and started analyzing for suspicious activity.
2. I found several HTTP requests containing the keyword **"flag"**. (GET_flag.png)
3. I followed one of the HTTP requests and received a flag.(follow_HTTP.png)
4. I submitted the flag, but it turned out to be **invalid**.(not_flag.png)
5. I decided to inspect **DNS traffic**, so I applied a filter to display only DNS requests.
(DNS.png)
6. I noticed two IP addresses:
   - `8.8.8.8` (Google DNS)
   - `18.217.1.57` – associated with a domain called `reddshrimpandherring.com`
7. I attempted to visit the domain, but received a **"domain not found"** error.
(DOMAIN.png)
8. I filtered only the packets sent to `18.217.1.57`.
(DNS_ip.png)
9. I applied an additional filter for packets of **exact size 93 bytes** to isolate the relevant queries.
(len_93.png)
10. I noticed that each DNS query included a **unique prefix** of random-looking characters.
11. I copied all the encoded parts of the DNS queries **in order**, and concatenated them into a single string.
(reddshrimpandherring.txt)
12. The result resembled a **Base64-encoded string**.
13. I used [CyberChef](https://gchq.github.io/CyberChef/) to decode the string from Base64.
14. The decoded result was the correct **flag**.


