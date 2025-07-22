# I received a CSR file (Certificate Signing Request). As a file readmycert.csr. 

# The CSR file was encoded and not readable directly.  I realized I needed to decode it                          to see what's inside.

# I checked online how to decrypt a CSR file (screenshot attached). I realized that I don't need to decrypt using an algorithm but rather use SSL DECODER.

# Installed OpenSSL – a free tool that helps with reading and creating encrypted files.
  used the command - openssl req -in readmycert.csr -noout -text
  This command shows the content of the CSR file in a human-readable format.

# After running the command, I saw the flag inside the subject field - picoCTF{read_mycert_373b4ab0}

  




