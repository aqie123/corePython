import pickle
# d = dict(name = 'aqie', aqge = 16, score = 99)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
# d = pickle.dumps(d)
# print(d)

# pickle.dump()直接把对象序列化后写入一个file-like Object
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# pickle.loads()方法反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)