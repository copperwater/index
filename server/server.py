import asyncio
import json

# We received a JSON message over the socket,
# handle it here.
async def handle_message(reader, writer):
    data = await reader.read(100)
    message = json.loads(data.decode())
    
    addr = writer.get_extra_info('peername')
    
    # DEBUG: Display the JSON message we received
    print("Received from %r: %r" % (addr, message))
    
    # TODO: Additional message handling

    # Send a response back to the client
    
    # TODO: For now, test response
    response = {'test' : 'Test Response'}
    writer.write(json.dumps(response).encode())
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_message, '0.0.0.0', 5350, loop=loop)
server = loop.run_until_complete(coro)

print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close() 
