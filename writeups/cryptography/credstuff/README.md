# credstuff

This is the write-up for the challenge **"credstuff"** from PicoCTF.

---

## The Challenge

### Description  
I managed to snag a leaked password database from the dark web. Can you find the password of the user `cultiris` and recover the flag?

[Challenge link](https://play.picoctf.org/practice/challenge/261?category=2&difficulty=2&page=2)

![Challenge Page Screenshot](img/screenshot1.png)

---

## Initial Look

We're given a `.tar` archive named `leak.tar`. Extracting it gives us two files:

- `usernames.txt`
- `passwords.txt`

It looks like these are **parallel lists** — each username corresponds to the password on the same line number.

---

## How to Solve It

---

### Step 1: Extract the Archive

Run this command to extract the contents:

```bash
tar -xf leak.tar
```

---

### Step 2: Find the Line Number of the Username

We want to find the password of the user `cultiris`.

#### On PowerShell:

```powershell
Select-String -Path usernames.txt -Pattern "cultiris"
```

**Output:**

```
usernames.txt:378:cultiris
```

This means `cultiris` is on line **378**.

---

### Step 3: Get the Corresponding Password

Since PowerShell uses 0-based indexing, line 378 is at index **377**:

```powershell
(Get-Content passwords.txt)[377]
```

**Output:**

```
cvpbPGS{P7e1S_54I35_71Z3}
```

This looks like an encoded flag!

---

### Step 4: Decode with ROT13

The prefix `cvpbPGS` suggests the use of ROT13. You can decode it using:

#### Python:

```python
import codecs
print(codecs.decode("cvpbPGS{P7e1S_54I35_71Z3}", "rot_13"))
```

#### Or online:

Go to [https://rot13.com](https://rot13.com) and paste the text.

**Decoded Output:**

```
picoCTF{C7r1F_54V35_71M3}
```

---

## Final Result

After decoding, we get the flag 

**Flag:** `picoCTF{C7r1F_54V35_71M3}`

---

Cheers and happy hacking! 
