import hashlib


def hashCracker(alg, wordfile_path, hashlist):
    unsolved = hashlist
    solved = []
    with open(wordfile_path, 'r', -1, 'utf8', 'ignore') as wordfile:
        for word in wordfile:
            word = word.strip()
            _alg = alg()
            _alg.update(word.encode('utf-8'))
            hashed = _alg.hexdigest()
            i = 0
            while i < len(unsolved):
                if hashed == unsolved[i]:
                    solved += [(unsolved.pop(i), word)]
                i += 1
            if len(unsolved) == 0:
                break
    return solved, unsolved


if __name__ == '__main__':
    import argparse, time

    alg_keys = ['md5', 'sha1', 'sha256']
    alg_names = {'md5':'MD5', 'sha1':'SHA-1', 'sha256':'SHA-256'}
    algs = {
            alg_keys[0]: hashlib.md5,
            alg_keys[1]: hashlib.sha1,
            alg_keys[2]: hashlib.sha256 }

    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-a', '--algorithm', choices=alg_keys, required=True,
            help='Hashing algorithm to use')
    parser.add_argument(
            '-wf', '--wordfile', required=True,
            help='World file path')
    parser.add_argument(
            '-hf', '--hashfile', required=True,
            help='Hash file path')

    args = parser.parse_args()
    alg = algs[args.algorithm]
    hashlist = list(map(str.strip, open(args.hashfile, 'r').readlines()))
    start = time.time()
    solved, unsolved = hashCracker(alg, args.wordfile, hashlist)
    end = time.time()

    _solved = str.join('\n\n', [f'''\
    Hashed: {hashed}
    String: {cracked}''' for hashed, cracked in solved])
    _unsolved = str.join('\n\n', [f'''\
    Hashed: {hashed}''' for hashed in unsolved])

    print(f'''\
Algorithm: {alg_names[args.algorithm]}
Wordlist: {args.wordfile}
Time: {end-start:.3f} seconds''')
    if _solved:
        print(f'''\
Solved hashes:
{_solved}''')
    if _unsolved:
        print(f'''\
Unsolved hashes:
{_unsolved}''')

