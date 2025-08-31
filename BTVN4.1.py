# Ma hoa bng thuat toan CAESAR
def caesar_encrypt(text, k):
    result = ""
    for c in text:
        if c.isupper():
            result += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        elif c.islower():
            result += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        else:
            result += c
    return result


if __name__ == "__main__":
    text = input("Nhap chuoi can ma hoa: ")
    k = int(input("Nhap khoa k: "))
    encrypted = caesar_encrypt(text, k)
    print("Chuoi da ma hoa:", encrypted)
  