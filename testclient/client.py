import asyncio
import json


async def send_test_message(message, loop):
    reader, writer = await asyncio.open_connection('0.0.0.0', 5350,
                                                   loop=loop)

    print('Send: %r' % message)
    writer.write(json.dumps(message).encode())

    data = await reader.read(100)
    data_json = json.loads(data.decode())
    print('Received response: %r' % data_json)
    
    writer.close()


message = {'test': 'Test Message'}
loop = asyncio.get_event_loop()
loop.run_until_complete(send_test_message(message, loop))
loop.close()
