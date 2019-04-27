# hashCracker

Introduction from [1fge/hashCracker][orig]:

> `hashCracker` is Python program used to crack unknown hashes. Currently, it
> only supports md5 hashes and dictionary attacks with the rockyou.txt wordlist
> which must be in the hashCracker folder. However, I plan on adding more
> algorithms and implementing the use of custom wordlists in later versions.

## Usage

## Example usage

```bash
python3 hashCracker.py -a md5 -wf rockyou.txt -hf sample_hashes.txt
```

Output:

```text
Algorithm: MD5
Wordlist: rockyou.txt
Time: 3.554 seconds
Solved hashes:
    Hashed: dbe7e69e0992132f4a18394556ef8720
    String: wellard1

    Hashed: e6c155570d6ff6464619a887076b6e36
    String: aron2006
```

## Testfile

```bash
./hashCracker_test.py
```

[orig]: https://github.com/1fge/hashCracker

