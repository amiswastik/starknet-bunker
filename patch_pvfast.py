import pvfast
import os

path = os.path.join(os.path.dirname(pvfast.__file__), 'remote_client.py')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix all mode checks
text = text.replace('stat.S_IMODE(path.stat().st_mode) != 0o600', 'os.name != "nt" and stat.S_IMODE(path.stat().st_mode) != 0o600')
text = text.replace('mode != 0o600:', 'os.name != "nt" and mode != 0o600:')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Successfully patched all Windows mode checks in remote_client.py!')
