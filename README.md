# Digital Signature Algorithm with RSA

## About

The Digital Signature Algorithm (DSA) is a Federal Information Processing Standard for digital signatures, based on the mathematical concept of modular exponentiation and the discrete logarithm problem. DSA is a variant of the Schnorr and ElGamal signature schemes. The National Institute of Standards and Technology (NIST) proposed DSA for use in their Digital Signature Standard (DSS) in 1991, and adopted it as FIPS 186 in 1994. Four revisions to the initial specification have been released. The newest specification is FIPS 186-4 from July 2013. DSA is patented but NIST has made this patent available worldwide royalty-free. A draft version of the specification FIPS 186-5 indicates DSA will no longer be approved for digital signature generation, but may be used to verify signatures generated prior to the implementation date of that standard.
* Project status: prototype

## Table of contents

> * [Digital Signature Algorithm with RSA](#title--repository-name)
>   * [About](#about--synopsis)
>   * [Table of contents](#table-of-contents)
>   * [Installation](#installation)
>   * [Usage](#usage)
>   * [Code](#code)
>     * [Content](#content)
>       * [Description](#description)
>       * [Modules](#modules)
>   * [License](#license)

## Code
![](https://img.shields.io/static/v1?label=build&message=passing&color=succes) ![](https://img.shields.io/static/v1?label=test&message=passing&color=succes) ![GitHub language count](https://img.shields.io/github/languages/count/christophermontero/DSA-RSA) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/christophermontero/DSA-RSA) ![Lines of code](https://img.shields.io/tokei/lines/github/christophermontero/DSA-RSA) ![PyPI - License](https://img.shields.io/pypi/l/pycryptodome) ![Conda](https://img.shields.io/conda/v/conda-forge/pycryptodome) ![Conda](https://img.shields.io/conda/pn/conda-forge/pycryptodome)

### Content
#### Description
This project seeks to implement a Digital Signature Algorithm (DSA) scheme, for this, it uses the following steps:
> 1. Input: Receive a text file
> 2. Hash function: A function is chosen from the following functions to calculate the diget of the previous file:
```
  - sha224
  - sha256
  - sha384
  - sha512
  - keccak
```
> 3. Algorithm: Initialize the key pair with the RSA algorithm
> 4. Signature: Encrypt the digest with the private key
> 5. Validation: Decrypt the signature with the public key and validate that the digest matches that of the file
> 6. Certificate: Print a certificate with the following information
```  
  - Certificate name
  - Name of signatory
  - Password (digest)
  - Salt
  - Hash function
  - Algorithm
  - Public and private key
  - Signature
  - Message
```

#### Modules
- GUI: It is the module that implements the algorithms and allows the reading of the text file through a graphical interface with text boxes, buttons and labels.
- Algorithm: This module contains the classes to create the RSA (2048) key pair, the hash functions and compute the expanded key.
- Utils: It contains the class to read the file and the necessary methods to convert the file from text to bytes.

## License

[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

[New BSD License](https://opensource.org/licenses/BSD-3-Clause)
