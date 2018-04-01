import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
	# 每调用一个测试方法的前后分别被执行 应用：连接关闭数据库
	def setUp(self):
		print('setUp...')
	def tearDown(self):
		print('tearDown')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 运行方式是在mydict_test.py的最后加上两行代码：
# 或者直接在命令行 python3 -m unittest mydict_test
if __name__ == '__main__':
    unittest.main()
