def encrypt(offset, text):
    cap = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    sml = list("abcdefghijklmnopqrstuvwxyz")
    result = ""
    for i in text:
        if i in cap:
            result += cap[(cap.index(i) + offset) % len(cap)]
        elif i in sml:
            result += sml[(sml.index(i) + offset) % len(sml)]
        else:
            result += i

    return result


def decrypt(offset, text):
    return encrypt(-offset, text)
