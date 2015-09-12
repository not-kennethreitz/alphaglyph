
CODEX = {
    'A': (u'\u0391', 'Alpha'),
    'B': (u'\u0392', 'Beta'),
    'C': (u'\u0393', 'Gamma'),
    'D': (u'\u0394', 'Delta'),
    'E': (u'\u0395', 'Epsilon'),
    'F': (u'\u0396', 'Zeta'),
    'G': (u'\u0397', 'Eta'),
    'H': (u'\u0398', 'Theta'),
    'I': (u'\u0399', 'Iota'),
    'J': (u'\u039A', 'Kappa'),
    'K': (u'\u039B', 'Lamda'),
    'L': (u'\u039C', 'Mu'),
    'M': (u'\u039D', 'Nu'),
    'N': (u'\u039E', 'Xi'),
    'O': (u'\u039F', 'Omicron'),
    'P': (u'\u03A0', 'Pi'),
    'Q': (u'\u03A1', 'Rho'),
    'R': (u'\u03A3', 'Sigma'),
    'S': (u'\u03A4', 'Tau'),
    'T': (u'\u03A5', 'Upsilon'),
    'U': (u'\u03A6', 'Phi'),
    'V': (u'\u03A7', 'Chi'),
    'W': (u'\u03A8', 'Psi'),
    'X': (u'\u03A9', 'Omega'),
    'a': (u'\u03B1', 'alpha'),
    'b': (u'\u03B2', 'beta'),
    'c': (u'\u03B3', 'gamma'),
    'd': (u'\u03B4', 'delta'),
    'e': (u'\u03B5', 'epsilon'),
    'f': (u'\u03B6', 'zeta'),
    'g': (u'\u03B7', 'eta'),
    'h': (u'\u03B8', 'theta'),
    'i': (u'\u03B9', 'iota'),
    'j': (u'\u03BA', 'kappa'),
    'k': (u'\u03BB', 'lamda'),
    'l': (u'\u03BC', 'mu'),
    'm': (u'\u03BD', 'nu'),
    'n': (u'\u03BE', 'xi'),
    'o': (u'\u03BF', 'omicron'),
    'p': (u'\u03C0', 'pi'),
    'q': (u'\u03C1', 'rho'),
    'r': (u'\u03C3', 'sigma'),
    's': (u'\u03C4', 'tau'),
    't': (u'\u03C5', 'upsilon'),
    'u': (u'\u03C6', 'phi'),
    'v': (u'\u03C7', 'chi'),
    'w': (u'\u03C8', 'psi'),
    'x': (u'\u03C9', 'omega')
}

for latin_letter, (greek_letter, name) in CODEX.items():
    CODEX[greek_letter] = (latin_letter, latin_letter)


def iter_transcode(s):

    for a in s:
        if a in CODEX:
            yield CODEX[a][0]
        else:
            yield a

def transcode(s):
    return ''.join([a for a in iter_transcode(s)])


def transcode_stream(instream, outstream):
    buf = b''
    while True:
        octet = instream.read(1)
        buf += octet
        try:
            text = buf.decode('utf-8')
        except UnicodeDecodeError:
            pass
        else:
            buf = b''
            outstream.write(transcode(text))
            outstream.flush()
        if not octet:
            break


if __name__ == '__main__':
    import sys
    transcode_stream(sys.stdin, sys.stdout)
