# coding = utf-8

def getBase64EncodedMD5String(input_string):
    import hashlib
    import base64
    hash_ins = hashlib.md5()
    hash_ins.update(input_string)
    value = hash_ins.digest()
    return base64.encodestring(value).replace('\n', '')
