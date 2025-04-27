🐺 WebHound - Red Team Web Hacking Toolkit

  
  Advanced Web Penetration Testing for Ethical Hackers
  Unleash the power of automated reconnaissance, vulnerability scanning, and stealth operations.
![TryHackMe](https://tryhackme-badges.s3.amazonaws.com/GamikaSanjana.png)

          



🔒 Overview
# WebHound - A red team toolkit for ethical web hacking
# Author: GamikaSanjana (https://github.com/GamikaSanjana)
# Mission: Empower pentesters to secure the web responsibly

WebHound is a Python-based, multi-functional tool designed for red team operators and ethical hackers. It automates web reconnaissance, vulnerability scanning, and exploitation preparation with a focus on stealth and efficiency. Whether you’re crawling for hidden endpoints, testing for SQL injection, or hunting admin panels, WebHound delivers a hacker-grade experience with a cyberpunk flair.
Key Features:

🌐 Web Crawler: Discovers URLs, forms, and parameters for comprehensive recon.
💉 SQL Injection Scanner: Integrates SQLMap for automated injection testing with WAF bypass.
🕸️ XSS Tester: Detects reflected and stored XSS vulnerabilities with customizable payloads.
🔑 Admin Panel Finder: Locates hidden login pages using wordlists.
🕵️ Stealth Mode: Supports Tor, proxy rotation, and User-Agent randomization.
📊 Reporting: Generates polished HTML reports for client deliverables.
🐺 Hacker Aesthetic: ASCII art, colored logs, and a terminal-like CLI.


🛠️ Installation
# Clone the repository
git clone https://github.com/GamikaSanjana/WebHound.git
cd WebHound

# Install dependencies
pip install requests beautifulsoup4 sqlmap stem colorlog Jinja2

# Install Tor for stealth mode (Kali Linux)
sudo apt update
sudo apt install tor
sudo systemctl start tor

Requirements:

Python 3.8+
Kali Linux or similar pentesting environment
A wordlist for admin panel discovery (e.g., /usr/share/wordlists/dirb/common.txt)
Optional: Proxy list or GitHub Personal Access Token for report uploads


🚀 Usage
python3 webhound.py --url <TARGET_URL> [OPTIONS]

Examples

Basic Scan (crawl, SQLi, XSS, admin panels):python3 webhound.py --url https://example.com --output-dir /home/kali/reports


Stealth Mode with Tor:python3 webhound.py --url https://example.com --tor --verbose


Proxy Rotation:python3 webhound.py --url https://example.com --proxies proxies.txt


Upload Report to GitHub:python3 webhound.py --url https://example.com --github-token YOUR_TOKEN --github-repo GamikaSanjana/reports



Options



Flag
Description
Default



--url
Target website URL (required)
None


--crawl-depth
Crawl depth for URL discovery
3


--wordlist
Wordlist for admin panel discovery
/usr/share/wordlists/dirb/common.txt


--proxies
File with proxy list (one per line)
None


--tor
Use Tor for anonymous requests
False


--github-token
GitHub PAT for report upload
None


--github-repo
GitHub repo for report upload (e.g., GamikaSanjana/reports)
None


--output-dir
Directory to save reports
/home/kali/Desktop/webhound_reports


--verbose
Enable verbose logging
False


Output:

Logs: Saved to webhound_YYYYMMDD_HHMMSS.log.
Reports: HTML files in --output-dir (e.g., webhound_report_20250427_141500.html).
Console: Colorful feedback with vulnerabilities and progress.


🔐 Ethical Hacking Guidelines

"Hack to secure, not to destroy. Test only what you’re authorized to touch."


Authorization: Use WebHound only on websites you have explicit, written permission to test (e.g., client sites, lab environments like DVWA, or CTF platforms).
Legal Compliance: Unauthorized hacking violates laws like the U.S. Computer Fraud and Abuse Act or Sri Lanka’s Computer Crimes Act. Document your scope and permissions.
Responsible Use: Avoid aggressive scans on production systems without coordination. Report vulnerabilities to site owners responsibly.
Practice Safely:
Local: Install DVWA (sudo apt install dvwa).
Online: Use Hack The Box, TryHackMe, or authorized test sites.
Example: python3 webhound.py --url http://localhost/dvwa




🐾 Features in Action
Web Crawler
Discovers URLs and forms for reconnaissance:
[*] Crawled 15 URLs and found 3 forms
[+] Form: action=https://example.com/login, inputs=[username, password]

SQL Injection Scanner
Tests for SQLi with SQLMap integration:
[+] SQL Injection found: DBMS: MySQL, Parameters: {'name': 'test'}

XSS Tester
Detects XSS vulnerabilities:
[+] XSS found: Payload: <script>alert('XSS')</script>, Parameter: search

Admin Panel Finder
Locates hidden admin pages:
[+] Potential admin panel found: https://example.com/admin

Stealth Mode
Uses Tor or proxies for anonymity:
[*] Tor circuit renewed: New IP assigned
[*] Rotated to proxy: http://123.45.67.89:8080

Reporting
Generates HTML reports:
[*] Report saved to /home/kali/reports/webhound_report_20250427_141500.html


📊 Example Report
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
        <tr><td>XSS</td><td>https://example.com/form</td><td>Payload: &lt;script&gt;alert('XSS')&lt;/script&gt;, Parameter: search</td></tr>
        <tr><td>Admin Panel</td><td>https://example.com/admin</td><td>Accessible admin page detected</td></tr>
    </table>
</body>
</html>


🤝 Contributing
Contributions are welcome! To contribute:

Fork the repo: https://github.com/GamikaSanjana/WebHound
Create a branch: git checkout -b feature/new-module
Commit changes: git commit -m "Add CSRF tester"
Push and open a PR: git push origin feature/new-module

Ideas:

New vulnerability scanners (e.g., CSRF, SSRF, LFI).
WAF detection with wafw00f integration.
Real-time CLI dashboard with rich.


🔑 License
MIT License - © 2025 Gamika Sanjana

🌐 Connect with the Author

  
    
  
  
    
  
  
    
  
  
    
  


Contact: Email gamikasanjana1@gmail.com or DM on WhatsApp +94763200676.

⚠️ Disclaimer
WebHound is for ethical hacking and authorized penetration testing only. The author, Gamika Sanjana, is not responsible for misuse or illegal activities. Always obtain permission before testing any system.

  
  Hack ethically, secure the web.


Last updated: April 27, 2025
