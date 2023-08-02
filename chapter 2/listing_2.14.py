from asyncio import Future

my_future = Future()

print(f'Does my_future ready? {my_future.done()}')

my_future.set_result(42)

print(f'Does my_future ready? {my_future.done()}')

print(f'What is the result stored inside my_future? {my_future.result()}')