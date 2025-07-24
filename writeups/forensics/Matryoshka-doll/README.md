# Matryoshka Doll

This is the write-up for the challenge "Matryoshka Doll" from PicoCTF 2021.

# The challenge

## Description
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?

Image:

![](img/dolls.jpg)

## Hints
1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as `picoCTF{XXXXX}`

## Initial look
The challenge provides an image called `dolls.jpg`. The theme (Matryoshka dolls) and hint suggest there are hidden files embedded inside this image, like dolls inside dolls. This clearly points toward a **steganography challenge** using **embedded archives**.

# How to solve it

## Step 1: Use `binwalk` to extract embedded data
I started by running `binwalk -e` to look for embedded data in the image:

```bash
binwalk -e dolls.jpg
```

This extracted a ZIP archive at a specific offset and created a folder:

```
extractions/dolls.jpg.extracted/4286C
```

## Step 2: Rename and unzip the embedded file
The extracted file had no extension, so I renamed it to `.zip` and tried to unzip it:

```bash
cd extractions/dolls.jpg.extracted
mv 4286C layer1.zip
```

However, this revealed an important twist: **the unzipped content was inside a folder also named `layer1.zip/base_images`** - a pattern that repeated.

## Step 3: Recursively go through layers
From here, I had to go through several nested folders using this pattern:

1. `cd layerX.zip/base_images`
2. Locate the embedded JPG (e.g., `2_c.jpg`)
3. Run `binwalk -e` on it:
   ```bash
   binwalk -e 2_c.jpg
   ```
4. Go into the new `.extracted` folder:
   ```bash
   cd _2_c.jpg.extracted
   ```
5. Rename the extracted binary:
   ```bash
   mv <random_name> layer(X+1).zip
   ```
6. Unzip it into a new folder:
   ```bash
   unzip layer(X+1).zip -d layer(X+1)
   ```

Then repeat the cycle. I had to do this **5 times** until I reached `flag.txt`.

## Step 4: Read the flag
Finally, after reaching `layer5.zip/base_images`, I found the long-awaited `flag.txt`:

```bash
cat flag.txt
```

# Solution

The flag found inside the final file was:

```
picoCTF{bf6acf878dcbd752f4721e41b1b1b66b}
```

Voila!!! 😎  
Cheers 😄
