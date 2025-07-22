# INDULGENTIA: OSINT tool for analyzing Certificate Transparency and found subdomains.

---

## Description

**INDULGENTIA** is a tool for automating OSINT analysis related to Certificate Transparency (CT) and phishing domain detection.  
The script uses [crt.sh](https://crt.sh) to finding possible subdomains, checks their registration and activity, takes alives of the main pages and generates a detailed report in DOCX format.

---

## Relevance and vulnerabilities of Certificate Transparency

**Certificate Transparency (CT)** is an open log of SSL/TLS certificates that allows you to track all issued certificates for domains.  
However, CT logs can be used by attackers to:

- **Search for new subdomains and services** (including test and internal ones) that accidentally "lit up" in public logs.
- **Attacks on newly registered domains** (for example, phishing or to quickly exploit vulnerabilities).
- **Automation of the search for phishing targets** — attackers can quickly find new domains and subdomains, register similar names and launch phishing campaigns.

**INDULGENTIA** helps to identify such risks and promptly respond to the appearance of suspicious domains.

---

## Features

- Finding of subdomains based on the target name (via crt.sh)
- Domain Registration Verification (WHOIS)
- HTTP and HTTPS activity verification
- Taking alives of the main pages of active sites
- Generation of a DOCX format report with results.
- Multithreaded processing to speed up analysis
- Automatic installation of dependencies for Arch Linux, Kali Linux, Ubuntu/Debian

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/toxy4ny/indulgentia.git
cd indulgentia
python3 indulgentia.py
```
## Safety
Use the script only for legitimate purposes and with the permission of the owners of the analyzed domains.
Do not use it to attack other people's resources.

## License
MIT License
