import math, base64, urllib.parse, hashlib, uuid, random, string, zlib, re, statistics, datetime, time, os, binascii, random, socket, requests, gzip

#--------CORE MATH--------

def add(f, s):
    try:
        f = float(f)
    except Exception as e:
        print(e)
        pass
    try:
        s = float(s)
        return f + s
    except Exception as e:
        print(e)
        pass
    
    
def sub(f, s):
    try:
        f = float(f)
    except Exception as e:
        print(e)
        pass
    try:
        s = float(s)
        return f - s
    except Exception as e:
        print(e)
        pass
    
    
def mul(f, s):
    try:
        f = float(f)
    except Exception as e:
        print(e)
        pass
    try:
        s = float(s)
        return f * s
    except Exception as e:
        print(e)
        pass
    
    
def div(f, s):
    try:
        f = float(f)
    except Exception as e:
        print(e)
        pass
    try:
        s = float(s)
        return f / s
    except Exception as e:
        print(e)
        pass
    
    
def ddv(f, s):
    try:
        f = float(f)
    except Exception as e:
        print(e)
        pass
    try:
        s = float(s)
        return f // s
    except Exception as e:
        print(e)
        pass
    
    
def com(f, s):
    try:
        f = float(f)
    except Exception as e:
        print(e)
        pass
    try:
        s = float(s)
        if s > f:
            return False
        if f > s:
            return True
        if f == s:
            return True
    except Exception as e:
        print(e)
        pass
    
    
#--------TRIGONOMETRY--------

def sin(f):
    try:
        f = float(f)
        return math.sin(f)
    except Exception as e:
        print(e)
        pass
    
    
def cos(f):
    try:
        f = float(f)
        return math.cos(f)
    except Exception as e:
        print(e)
        pass
    
    
def tan(f):
    try:
        f = float(f)
        return math.tan(f)
    except Exception as e:
        print(e)
        pass
    
    
#--------GEOMETRY--------

def tri(b, h):
    try:
        b = float(b)
        h = float(h)
        return b * h / 2
    except Exception as e:
        print(e)
        pass
    
    
def sqr(s):
    try:
        s = float(s)
        return s * s
    except Exception as e:
        print(e)
        pass
    
    
def rec(b, h):
    try:
        b = float(b)
        h = float(h)
        return b * h
    except Exception as e:
        print(e)
        pass
    
    
def cir(r):
    try:
        r = float(r)
        return math.pi * (r ** 2)
    except Exception as e:
        print(e)
        pass
    
    
def rcp(w, l, h):
    try:
        w = float(w)
        h = float(h)
        l = float(l)
        return l * w * h
    except Exception as e:
        print(e)
        pass
    
    
def sph(r):
    try:
        r = float(r)
        return 1.33 * math.pi * (r ** 3)
    except Exception as e:
        print(e)
        pass
    
    
def cyl(r, h):
    try:
        r = float(r)
        h = float(h)
        return  cir(r) * h
    except Exception as e:
        print(e)
        pass
    
    
#--------DISTANCE & ALGEBRA--------

def cd2(x1, y1, x2, y2):
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
    except Exception as e:
        print(e)
        pass
    
    
def cd3(x1, y1, z1, x2, y2, z2):
    try:
        x1 = float(x1)
        y1 = float(y1)
        z1 = float(z1)
        x2 = float(x2)
        y2 = float(y2)
        z2 = float(z2)
        return math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    except Exception as e:
        print(e)
        pass
    
    
def pth(a, b):
    try:
        a = float(a)
        b = float(b)
        return math.sqrt(a*a + b*b)
    except Exception as e:
        print(e)
        pass
    
    
def qad(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        disc = b*b - 4*a*c
        if disc < 0:
            return None
        r1 = (-b + math.sqrt(disc)) / (2*a)
        r2 = (-b - math.sqrt(disc)) / (2*a)
        return (r1, r2)
    except Exception as e:
        print(e)
        pass
    
    
#--------LOGS & EXPONENTS--------

def log(x):
    try:
        x = float(x)
        return math.log10(x)
    except Exception as e:
        print(e)
        pass


def ln(x):
    try:
        x = float(x)
        return math.log(x)
    except Exception as e:
        print(e)
        pass
    
    
#--------CRYPTO CIPHERS & HASHING--------

def csr(text, shift):
    try:
        shift = int(shift)
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result
    except Exception as e:
        print(e)
        pass
    
    
def rot13(text):
    return csr(text, 13)


def vig(text, key):
    try:
        result = ""
        key = key.lower()
        ki = 0  # key index

        for char in text:
            if char.isalpha():
                shift = ord(key[ki % len(key)]) - ord('a')
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
                ki += 1
            else:
                result += char
        return result
    except Exception as e:
        print(e)
        pass
    
    
def sha256(text):
    try:
        return hashlib.sha256(text.encode()).hexdigest()
    except Exception as e:
        print(e)
        pass


def md5(text):
    try:
        return hashlib.md5(text.encode()).hexdigest()
    except Exception as e:
        print(e)
        pass
    
    
def hash_string(text, salt=""):
    try:
        return hashlib.sha256((salt + text).encode()).hexdigest()
    except Exception as e:
        print(e)
        pass
    
    
#--------ENCODING/DECODING--------

def htd(x):
    try:
        return int(x, 16)
    except Exception as e:
        print(e)
        pass
    
    
def dth(x):
    try:
        x = int(float(x))
        return hex(x)
    except Exception as e:
        print(e)
        pass
    
    
def btd(x):
    try:
        return int(x, 2)
    except Exception as e:
        print(e)
        pass


def dtb(x):
    try:
        x = int(float(x))
        return bin(x)
    except Exception as e:
        print(e)
        pass
    
    
def b64e(text):
    try:
        return base64.b64encode(text.encode()).decode()
    except Exception as e:
        print(e)
        pass
    
    
def b64d(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception as e:
        print(e)
        pass
    
    
def urle(text):
    try:
        return urllib.parse.quote(text)
    except Exception as e:
        print(e)
        pass
    

def urld(text):
    try:
        return urllib.parse.unquote(text)
    except Exception as e:
        print(e)
        pass


def base32_encode(text):
    try:
        return base64.b32encode(text.encode()).decode()
    except Exception as e:
        print(e)
        pass


def base32_decode(text):
    try:
        return base64.b32decode(text.encode()).decode()
    except Exception as e:
        print(e)
        pass


def base85_encode(text):
    try:
        return base64.b85encode(text.encode()).decode()
    except Exception as e:
        print(e)
        pass


def base85_decode(text):
    try:
        return base64.b85decode(text.encode()).decode()
    except Exception as e:
        print(e)
        pass


def ascii_to_int(char):
    try:
        return ord(char)
    except Exception as e:
        print(e)
        pass


def int_to_ascii(num):
    try:
        num = int(float(num))
        return chr(num)
    except Exception as e:
        print(e)
        pass


def bytes_to_hex(text):
    try:
        return binascii.hexlify(text.encode()).decode()
    except Exception as e:
        print(e)
        pass


def hex_to_bytes(hexstr):
    try:
        return binascii.unhexlify(hexstr).decode()
    except Exception as e:
        print(e)
        pass
    
    
#--------UTILITIES--------

def uuid():
    try:
        return str(uuid.uuid4())
    except Exception as e:
        print(e)
        pass
    
    
def gen_password(length=16):
    try:
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(int(length)))
    except Exception as e:
        print(e)
        pass
    
    
def crc32(text):
    try:
        return format(zlib.crc32(text.encode()), '08x')
    except Exception as e:
        print(e)
        pass
    
    
def regex_find(pattern, text):
    try:
        return re.findall(pattern, text)
    except Exception as e:
        print(e)
        pass
    
    
#--------FILE UTILITIES--------

def file_hash(path, algo="sha256"):
    try:
        h = getattr(hashlib, algo)()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        print(e)
        pass
    
    
def file_size(path):
    try:
        return os.path.getsize(path)
    except Exception as e:
        print(e)
        pass


def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        print(e)
        pass


def write_file(path, text):
    try:
        with open(path, "w") as f:
            f.write(text)
            return True
    except Exception as e:
        print(e)
        pass


def append_file(path, text):
    try:
        with open(path, "a") as f:
            f.write(text)
            return True
    except Exception as e:
        print(e)
        pass


def list_dir(path):
    try:
        return os.listdir(path)
    except Exception as e:
        print(e)
        pass


def file_exists(path):
    try:
        return os.path.exists(path)
    except Exception as e:
        print(e)
        pass

#--------BANKING--------

def simple_interest(P, r, t):
    try:
        P = float(P)
        r = float(r)
        t = float(t)
        return  mul(P,  mul(r, t))
    except Exception as e:
        print(e)
        pass


def compound_interest(P, r, n, t):
    try:
        P = float(P)
        r = float(r)
        n = float(n)
        t = float(t)
        return P * (1 + (r / n)) ** (n * t)
    except Exception as e:
        print(e)
        pass


def loan_payment(P, r, n):
    try:
        P = float(P)
        r = float(r)
        n = float(n)
        monthly = r
        top = monthly * (1 + monthly) ** n
        bottom = (1 + monthly) ** n - 1
        return P * (top / bottom)
    except Exception as e:
        print(e)
        pass
    
    
def total_interest(P, r, n):
    try:
        P = float(P)
        payment =  loan_payment(P, r, n)
        total_paid =  mul(payment, n)
        return  sub(total_paid, P)
    except Exception as e:
        print(e)
        pass


def roi(gain, cost):
    try:
        gain = float(gain)
        cost = float(cost)
        net =  sub(gain, cost)
        return  mul( div(net, cost), 100)
    except Exception as e:
        print(e)
        pass


def percent_change(old, new):
    try:
        old = float(old)
        new = float(new)
        diff =  sub(new, old)
        return  mul( div(diff, old), 100)
    except Exception as e:
        print(e)
        pass


def currency_convert(amount, rate):
    try:
        amount = float(amount)
        rate = float(rate)
        return  mul(amount, rate)
    except Exception as e:
        print(e)
        pass


def savings_goal(target, r, n, t):
    try:
        target = float(target)
        r = float(r)
        n = float(n)
        t = float(t)
        factor = (1 + r) ** (n * t)
        return target * r / (factor - 1)
    except Exception as e:
        print(e)
        pass


#--------STATISTICS--------

def median(*nums):
    try:
        nums = [float(n) for n in nums]
        return statistics.median(nums)
    except Exception as e:
        print(e)
        pass


def mode(*nums):
    try:
        nums = [float(n) for n in nums]
        return statistics.mode(nums)
    except Exception as e:
        print(e)
        pass


def variance(*nums):
    try:
        nums = [float(n) for n in nums]
        return statistics.variance(nums)
    except Exception as e:
        print(e)
        pass


def stdev(*nums):
    try:
        nums = [float(n) for n in nums]
        return statistics.stdev(nums)
    except Exception as e:
        print(e)
        pass


def zscore(x, mean, stdev):
    try:
        x = float(x)
        mean = float(mean)
        stdev = float(stdev)
        return (x - mean) / stdev
    except Exception as e:
        print(e)
        pass

#--------VALIDATION--------

def valid_email(text):
    try:
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", text) is not None
    except Exception as e:
        print(e)
        pass


def valid_url(text):
    try:
        return re.fullmatch(r"https?://[^\s]+", text) is not None
    except Exception as e:
        print(e)
        pass


def valid_ipv4(text):
    try:
        return re.fullmatch(r"(\d{1,3}\.){3}\d{1,3}", text) is not None
    except Exception as e:
        print(e)
        pass


def valid_ipv6(text):
    try:
        return re.fullmatch(r"([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}", text) is not None
    except Exception as e:
        print(e)
        pass


def valid_hex_color(text):
    try:
        return re.fullmatch(r"#[0-9a-fA-F]{6}", text) is not None
    except Exception as e:
        print(e)
        pass


def strong_password(text):
    try:
        return re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}", text) is not None
    except Exception as e:
        print(e)
        pass

#--------PHYSICS--------

def force(m, a):
    try:
        m = float(m)
        a = float(a)
        return m * a
    except Exception as e:
        print(e)
        pass


def kinetic_energy(m, v):
    try:
        m = float(m)
        v = float(v)
        return 0.5 * m * (v ** 2)
    except Exception as e:
        print(e)
        pass


def potential_energy(m, g, h):
    try:
        m = float(m)
        g = float(g)
        h = float(h)
        return m * g * h
    except Exception as e:
        print(e)
        pass


def momentum(m, v):
    try:
        m = float(m)
        v = float(v)
        return m * v
    except Exception as e:
        print(e)
        pass


def ohms_law(v, r):
    try:
        v = float(v)
        r = float(r)
        return v / r
    except Exception as e:
        print(e)
        pass
    

def wattage(v, a):
    try:
        v = float(v)
        a = float(a)
        return v * a
    except Exception as e:
        print(e)
        pass


#--------DATE & TIME UTILITIES--------

def now_timestamp():
    try:
        return time.time()
    except Exception as e:
        print(e)
        pass


def now_datetime():
    try:
        return datetime.datetime.now()
    except Exception as e:
        print(e)
        pass


def seconds_to_hms(sec):
    try:
        sec = int(float(sec))
        h = sec // 3600
        m = (sec % 3600) // 60
        s = sec % 60
        return f"{h:02}:{m:02}:{s:02}"
    except Exception as e:
        print(e)
        pass


def hms_to_seconds(h, m, s):
    try:
        h = int(float(h))
        m = int(float(m))
        s = int(float(s))
        return h * 3600 + m * 60 + s
    except Exception as e:
        print(e)
        pass


def days_between(d1, d2):
    try:
        d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)
    except Exception as e:
        print(e)
        pass


#--------RANDOM UTILITIES--------

def rand_int(a, b):
    try:
        a = int(float(a))
        b = int(float(b))
        return random.randint(a, b)
    except Exception as e:
        print(e)
        pass


def rand_float(a, b):
    try:
        a = float(a)
        b = float(b)
        return random.uniform(a, b)
    except Exception as e:
        print(e)
        pass


def rand_choice(lst):
    try:
        return random.choice(lst)
    except Exception as e:
        print(e)
        pass


def rand_string(length=12):
    try:
        length = int(float(length))
        chars = string.ascii_letters
        return ''.join(random.choice(chars) for _ in range(length))
    except Exception as e:
        print(e)
        pass


def rand_hex(length=8):
    try:
        length = int(float(length))
        return ''.join(random.choice("0123456789abcdef") for _ in range(length))
    except Exception as e:
        print(e)
        pass


#--------NETWORKING UTILITIES--------

def ping_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except Exception:
        return False


def dns_lookup(host):
    try:
        return socket.gethostbyname(host)
    except Exception as e:
        print(e)
        pass


def port_open(host, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        result = s.connect_ex((host, int(port)))
        s.close()
        return result == 0
    except Exception as e:
        print(e)
        pass


def http_get(url):
    try:
        return requests.get(url).text
    except Exception as e:
        print(e)
        pass


def http_post(url, data):
    try:
        return requests.post(url, data=data).text
    except Exception as e:
        print(e)
        pass


#--------TEXT PROCESSING--------

def word_count(text):
    try:
        return len(text.split())
    except Exception as e:
        print(e)
        pass


def sentence_count(text):
    try:
        return len(re.split(r"[.!?]+", text)) - 1
    except Exception as e:
        print(e)
        pass


def remove_punctuation(text):
    try:
        return re.sub(r"[^\w\s]", "", text)
    except Exception as e:
        print(e)
        pass


def tokenize(text):
    try:
        return text.split()
    except Exception as e:
        print(e)
        pass


def ngrams(text, n):
    try:
        words = text.split()
        return [words[i:i+n] for i in range(len(words)-n+1)]
    except Exception as e:
        print(e)
        pass


def freq_map(text):
    try:
        words = text.split()
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        return freq
    except Exception as e:
        print(e)
        pass


#--------COMPRESSION UTILITIES--------

def gzip_compress(text):
    try:
        return base64.b64encode(gzip.compress(text.encode())).decode()
    except Exception as e:
        print(e)
        pass


def gzip_decompress(b64text):
    try:
        return gzip.decompress(base64.b64decode(b64text.encode())).decode()
    except Exception as e:
        print(e)
        pass


def zlib_compress(text):
    try:
        return base64.b64encode(zlib.compress(text.encode())).decode()
    except Exception as e:
        print(e)
        pass


def zlib_decompress(b64text):
    try:
        return zlib.decompress(base64.b64decode(b64text.encode())).decode()
    except Exception as e:
        print(e)
        pass


