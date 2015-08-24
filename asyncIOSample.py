#coding = utf-8

'''
A simple example of Async IO.
'''

import asyncio

@asyncio.coroutine	#Set this function to a async coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect		#Wait until connect returns a pair of (StreamReader, StreamWriter)
    header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()	#Wait until drain after writing data into the stream
    while True:
        line = yield from reader.readline()		#Wait until reader returns the data
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

#Get an event loop
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
