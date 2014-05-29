http://www.pythoncentral.io/hashing-strings-with-python/

Hash functions are used inside some cryptographic algorithms, in digital
signatures, message authentication codes, manipulation detection, fingerprints,
checksums (message integrity check), hash tables, password storage and much
more. As a Python programmer you may need these functions to check for duplicate
data or files, to check data integrity when you transmit information over a
network, to securely store passwords in databases, or maybe some work related to
cryptography.

I want to make clear that hash functions are not a cryptographic protocol, they
do not encrypt or decrypt information, but they are a fundamental part of many
cryptographic protocols and tools.

Some of the most used hash functions are:

    MD5: Message digest algorithm producing a 128 bit hash value. This is widely
    used to check data integrity. It is not suitable for use in other fields due
    to the security vulnerabilities of MD5. SHA: Group of algorithms designed by
    the U.S's NSA that are part of the U.S Federal Information processing
    standard. These algorithms are used widely in several cryptographic
    applications. The message length ranges from 160 bits to 512 bits.

The hashlib module, included in The Python Standard library is a module
containing an interface to the most popular hashing algorithms. hashlib
implements some of the algorithms, however if you have OpenSSL installed,
hashlib is able to use this algorithms as well.


A hash function is a function that takes input of a variable length sequence of
bytes and converts it to a fixed length sequence. It is a one way function. This
means if f is the hashing function, calculating f(x) is pretty fast and simple,
but trying to obtain x again will take years. The value returned by a hash
function is often called a hash, message digest, hash value, or checksum. Most
of the time a hash function will produce unique output for a given input.
However depending on the algorithm, there is a possibility to find a collision
due to the mathematical theory behind these functions.

Hash functions are used inside some cryptographic algorithms, in digital
signatures, message authentication codes, manipulation detection, fingerprints,
checksums (message integrity check), hash tables, password storage and much
more. As a Python programmer you may need these functions to check for duplicate
data or files, to check data integrity when you transmit information over a
network, to securely store passwords in databases, or maybe some work related to
cryptography.

I want to make clear that hash functions are not a cryptographic protocol, they
do not encrypt or decrypt information, but they are a fundamental part of many
cryptographic protocols and tools.

Some of the most used hash functions are:

    MD5: Message digest algorithm producing a 128 bit hash value. This is widely
    used to check data integrity. It is not suitable for use in other fields due
    to the security vulnerabilities of MD5. SHA: Group of algorithms designed by
    the U.S's NSA that are part of the U.S Federal Information processing
    standard. These algorithms are used widely in several cryptographic
    applications. The message length ranges from 160 bits to 512 bits.

The hashlib module, included in The Python Standard library is a module
containing an interface to the most popular hashing algorithms. hashlib
implements some of the algorithms, however if you have OpenSSL installed,
hashlib is able to use this algorithms as well.
