# 🐺 WebHound - Red Team Web Hacking Toolkit

<div align="center">
  <img src="https://raw.githubusercontent.com/GamikaSanjana/WebHound/main/assets/webhound_banner.gif" alt="WebHound Cyberpunk Banner" width="800"/>
  <h3>Advanced Penetration Testing for Ethical Hackers</h3>
  <p>Automated reconnaissance, vulnerability scanning, and stealth ops with a cyberpunk edge.</p>

  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&pause=1000&color=1F6FEB&center=true&vCenter=true&width=435&lines=Scan.+Exploit.+Secure.;Unleash+the+Hound..." alt="Typing SVG"/>

  <p>
    <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FGamikaSanjana%2FWebHound&count_bg=%231F6FEB&title_bg=%231A1A1A&icon=python.svg&icon_color=%23E7E7E7&title=Views&edge_flat=false" alt="Repo Views"/>
    <img src="https://img.shields.io/github/forks/GamikaSanjana/WebHound?label=Forks&style=social" alt="Forks"/>
    <img src="https://img.shields.io/github/stars/GamikaSanjana/WebHound?style=social" alt="Stars"/>
    <img src="https://img.shields.io/github/license/GamikaSanjana/WebHound?color=%237B2CBF&label=License&style=flat-square" alt="License"/>
    <img src="https://img.shields.io/static/v1?label=Author&message=Gamika%20Sanjana&color=%237B2CBF&style=flat-square" alt="Author"/>
  </p>
  <p>
    <img src="https://tryhackme-badges.s3.amazonaws.com/GamikaSanjana.png" alt="TryHackMe Badge" width="150"/>
  </p>
</div>

---

## 🔒 Overview

```bash
# WebHound v1.0
# Author: GamikaSanjana (github.com/GamikaSanjana)
# Mission: Empower red teamers to secure the web ethically
```

WebHound is a **Python-based toolkit** for **red team operators** and **ethical hackers**, designed to automate **web reconnaissance**, **vulnerability scanning**, and **exploitation preparation**. With features like web crawling, SQL injection testing, XSS detection, and admin panel discovery, WebHound delivers a **stealthy, efficient, and hacker-grade** experience.

**Why WebHound?**
- 🌐 **Comprehensive Recon**: Crawls URLs, forms, and parameters.
- 💉 **Vulnerability Scanning**: Tests for SQLi, XSS, and more with WAF bypass.
- 🔑 **Hidden Endpoint Discovery**: Finds admin panels and sensitive pages.
- 🕵️ **Stealth Operations**: Supports Tor, proxies, and User-Agent randomization.
- 📊 **Professional Reports**: Generates HTML reports for clients.
- 🐺 **Cyberpunk Aesthetic**: ASCII art, neon logs, and a slick CLI.

---

## 🛠️ Installation

Get WebHound up and running on your Kali Linux system in minutes.

```bash
# Clone the repository
git clone https://github.com/GamikaSanjana/WebHound.git
cd WebHound

# Install Python dependencies
pip install requests beautifulsoup4 sqlmap stem colorlog Jinja2

# Install Tor for stealth mode
sudo apt update
sudo apt install tor
sudo systemctl start tor
```

**Requirements**:
- 🐍 Python 3.8+
- 🐧 Kali Linux or similar pentesting OS
- 📜 Wordlist (e.g., `/usr/share/wordlists/dirb/common.txt`)
- 🌐 Optional: Proxy list or GitHub Personal Access Token (PAT)

<details>
<summary>🔍 Troubleshooting Installation</summary>
- **Tor not running?** Check status: `sudo systemctl status tor`
- **Pip errors?** Use: `pip install --user <package>`
- **Missing wordlist?** Download: `sudo apt install wordlists`
</details>

---

## 🚀 Usage

Run WebHound with a single command to unleash its power.

```bash
python3 webhound.py --url <TARGET_URL> [OPTIONS]
```

### Quick Examples
| Task | Command |
|------|---------|
| **Basic Scan** (crawl, SQLi, XSS, admin panels) | `python3 webhound.py --url https://example.com --output-dir /home/kali/reports` |
| **Stealth Mode** (Tor, verbose) | `python3 webhound.py --url https://example.com --tor --verbose` |
| **Proxy Rotation** | `python3 webhound.py --url https://example.com --proxies proxies.txt` |
| **GitHub Report Upload** | `python3 webhound.py --url https://example.com --github-token YOUR_TOKEN --github-repo GamikaSanjana/reports` |

### Options
| Flag | Description | Default |
|------|-------------|---------|
| `--url` | Target website URL (required) | None |
| `--crawl-depth` | Crawl depth for URL discovery | 3 |
| `--wordlist` | Wordlist for admin panel discovery | `/usr/share/wordlists/dirb/common.txt` |
| `--proxies` | File with proxy list (one per line) | None |
| `--tor` | Use Tor for anonymous requests | False |
| `--github-token` | GitHub PAT for report upload | None |
| `--github-repo` | GitHub repo for report upload | None |
| `--output-dir` | Directory to save reports | `/home/kali/Desktop/webhound_reports` |
| `--verbose` | Enable verbose logging | False |

**Output**:
- 📜 **Logs**: `webhound_YYYYMMDD_HHMMSS.log`
- 📊 **Reports**: HTML files in `--output-dir` (e.g., `webhound_report_20250427_141500.html`)
- 🖥️ **Console**: Neon-colored feedback with vulnerabilities

<details>
<summary>🔍 Sample Console Output</summary>
```bash
 __          __  _
| \        / | | |
|  \      /  | | |__   ___
|   \    /   | | '_ \ / __|
|    \  /    | | | | | (__
|     \/     |_|_| |_|___|
   Red Team Web Hacking Toolkit

2025-04-27 14:15:00 [INFO] Initializing WebHound for https://example.com
2025-04-27 14:15:01 [INFO] Crawled 15 URLs and found 3 forms
2025-04-27 14:15:02 [INFO] SQL Injection found: DBMS: MySQL
2025-04-27 14:15:03 [INFO] Report saved to /home/kali/reports/webhound_report_20250427_141500.html
[*] Done. Hack ethically, secure the web.
```
</details>

---

## 🔐 Ethical Hacking Guidelines

> 🚨 **Hack to secure, not to destroy. Test only what you’re authorized to touch.**

WebHound is a **powerful tool** for **authorized penetration testing**. Misuse can lead to legal consequences under laws like the **U.S. Computer Fraud and Abuse Act** or **Sri Lanka’s Computer Crimes Act**.

- **Authorization**: Obtain **explicit, written permission** before testing any website.
- **Responsible Use**: Avoid aggressive scans on production systems without coordination. Report vulnerabilities responsibly.
- **Safe Practice**:
  - **Local**: Set up DVWA: `sudo apt install dvwa`
  - **Online**: Use Hack The Box, TryHackMe, or authorized test sites
  - **Example**: `python3 webhound.py --url http://localhost/dvwa`

---

## 🐾 Features in Action

### 🌐 Web Crawler
Discovers hidden endpoints and forms:
```bash
[*] Crawled 15 URLs and found 3 forms
[+] Form: action=https://example.com/login, inputs=[username, password]
```

### 💉 SQL Injection Scanner
Automates SQLi testing with SQLMap:
```bash
[+] SQL Injection found: DBMS: MySQL, Parameters: {'name': 'test'}
```

### 🕸️ XSS Tester
Detects XSS vulnerabilities:
```bash
[+] XSS found: Payload: <script>alert('XSS')</script>, Parameter: search
```

### 🔑 Admin Panel Finder
Locates sensitive pages:
```bash
[+] Potential admin panel found: https://example.com/admin
```

### 🕵️ Stealth Mode
Evades detection with Tor/proxies:
```bash
[*] Tor circuit renewed: New IP assigned
[*] Rotated to proxy: http://123.45.67.89:8080
```

### 📊 Reporting
Generates client-ready HTML reports:
```bash
[*] Report saved to /home/kali/reports/webhound_report_20250427_141500.html
```

<details>
<summary>🔍 Example Report</summary>
```html
<!DOCTYPE html>
<html>
<head>
    <title>WebHound Report - https://example.com</title>
    <style>
        body { font-family: Arial, sans-serif; background: #1a1a1a; color: #00ff00; }
        h1 { text-align: center; }
        table { width: 80%; margin: 20px auto; border-collapse: collapse; }
        th, td { border: 1px solid #00ff00; padding: 10px; text-align: left; }
        th { background: #333; }
    </style>
</head>
<body>
    <h1>WebHound Penetration Testing Report</h1>
    <p>Target: https://example.com</p>
    <p>Date: 2025-04-27 14:15:00</p>
    <table>
        <tr><th>Type</th><th>URL</th><th>Details</th></tr>
        <tr><td>SQL Injection</td><td>https://example.com/search</td><td>DBMS: MySQL, Parameters: {'name': 'test'}</td></tr>
        <tr><td>XSS</td><td>https://example.com/form</td><td>Payload: <script>alert('XSS')</script>, Parameter: search</td></tr>
        <tr><td>Admin Panel</td><td>https://example.com/admin</td><td>Accessible admin page detected</td></tr>
    </table>
</body>
</html>
```
</details>

---

## 🤝 Contributing

Join the pack! Contribute to WebHound to make it even deadlier.

1. Fork: `https://github.com/GamikaSanjana/WebHound`
2. Branch: `git checkout -b feature/new-module`
3. Commit: `git commit -m "Add CSRF tester"`
4. PR: `git push origin feature/new-module`

**Ideas**:
- 🛡️ WAF detection with `wafw00f`
- 🔍 New scanners (CSRF, SSRF, LFI)
- 📈 Real-time CLI dashboard with `rich`

---

## 🔑 License

[MIT License](LICENSE) - © 2025 Gamika Sanjana

---

## 🌐 Connect with the Author

<div align="center">
  <a href="https://github.com/GamikaSanjana">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/gamika-sanjana11/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="https://x.com/VehanRajintha">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"/>
  </a>
  <a href="https://www.instagram.com/vehanrajintha/">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"/>
  </a>
  <a href="mailto:gamikasanjana1@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
</div>

📫 **Email**: [gamikasanjana1@gmail.com](mailto:gamikasanjana1@gmail.com)  
💬 **WhatsApp**: [+94763200676](https://wa.me/+94763200676)

---

## ⚠️ Disclaimer

WebHound is for **ethical hacking and authorized penetration testing only**. Misuse violates laws and GitHub’s terms. The author, **Gamika Sanjana**, is not responsible for illegal activities. Always obtain written permission before testing.

<div align="center">
  <img src="https://raw.githubusercontent.com/GamikaSanjana/WebHound/main/assets/terminal.gif" alt="Terminal Animation" width="400"/>
  <p>🐺 Hack Ethically. Secure the Web.</p>
</div>

*Last updated: April 27, 2025*
