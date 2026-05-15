import base64, struct, os, sys
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateNumbers, RSAPublicNumbers
from cryptography.hazmat.primitives import serialization

def read_string(d, o):
    n = struct.unpack_from('>I', d, o)[0]
    return d[o+4:o+4+n], o+4+n

def read_mpint(d, o):
    n = struct.unpack_from('>I', d, o)[0]
    return int.from_bytes(d[o+4:o+4+n], 'big'), o+4+n

raw = os.environ.get('SSH_KEY', '')
print(f"[diag] raw length: {len(raw)}")
print(f"[diag] actual newlines: {raw.count(chr(10))}")
print(f"[diag] literal \\\\n: {raw.count(chr(92)+'n')}")
print(f"[diag] first line repr: {repr(raw[:80])}")

# Handle both actual newlines and escaped \n sequences
if raw.count('\n') < 3:
    raw = raw.replace('\\n', '\n')

lines = raw.replace('\r\n', '\n').replace('\r', '\n').strip().split('\n')
print(f"[diag] line count after split: {len(lines)}")
print(f"[diag] first 3 lines: {lines[:3]}")

def get_val(key):
    return next(l.split(': ', 1)[1] for l in lines if l.startswith(key))

def get_block(key):
    count = int(get_val(key))
    start = next(i for i, l in enumerate(lines) if l.startswith(key)) + 1
    return base64.b64decode(''.join(lines[start:start+count]))

pub  = get_block('Public-Lines:')
priv = get_block('Private-Lines:')

_, o = read_string(pub, 0)
e, o = read_mpint(pub, o)
n, o = read_mpint(pub, o)
d, o = read_mpint(priv, 0)
p, o = read_mpint(priv, o)
q, o = read_mpint(priv, o)
u, _ = read_mpint(priv, o)

key = RSAPrivateNumbers(p, q, d, d % (p-1), d % (q-1), u,
                        RSAPublicNumbers(e, n)).private_key()

pem = key.private_bytes(
    serialization.Encoding.PEM,
    serialization.PrivateFormat.TraditionalOpenSSL,
    serialization.NoEncryption()
)

out = sys.argv[1] if len(sys.argv) > 1 else '/tmp/deploy_key'
with open(out, 'wb') as f:
    f.write(pem)

print(f"Key written to {out}")
