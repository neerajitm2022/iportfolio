import time
import asyncio

async def test_fun1():
  time.sleep(5)
  print("test_fun")


async def test_fun2():
  time.sleep(5)
  print("test_fun2")


async def funmain():
  test_fun1()
  test_fun2()


asyncio.run(funmain())

