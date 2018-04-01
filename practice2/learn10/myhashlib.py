# 摘要算法又称哈希算法、散列算法，如MD5，SHA1等等

# 计算一个字符串MD5值
# (固定的128 bit字节，通常用一个32位的16进制字符串表示)
import hashlib
md5 = hashlib.md5()
md5.update("how to use md5 in python hashlib? by aqie".encode('utf-8'))

print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update("how to use md5 in python hashlib? by aqie".encode('utf-8'))
print(sha1.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示