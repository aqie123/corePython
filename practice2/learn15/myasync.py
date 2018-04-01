# @asyncio.coroutine可以把一个generator标记为coroutine类型
# 在coroutine内部用yield from调用另一个coroutine实现异步操作
# 简化并更好地标识异步IO 引入async和await
import asyncio

async def hello():
	print("hello aqie")
	r = await asyncio.sleep(1)
	print("hello world")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()