import logging
# 配置日志记录
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别为DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',  # 设置日志格式
    filename='app.log',  # 指定日志文件名
    filemode='w'  # 指定日志文件的打开模式（此处为覆盖写入）
)
# 创建Logger对象
logger = logging.getLogger('log')
#--------------------------------------------

import asyncio
import websockets
import json

# 保存客户端连接的列表
connected_clients = []

# 处理WebSocket连接的协程函数
async def handle_connection(websocket, path):
    # 将新连接添加到列表
    connected_clients.append(websocket)
    print("New client connected.",connected_clients)

    try:
        # 接收客户端的消息
        async for message in websocket:
            #解析json消息
            print(f"Received message from client: {message}")
            data = json.loads(message)
            print(f"Server received message: {data['content']} from {data['ip']+'#'+data['randstr']}")
            # 发送消息给所有客户端 除了发送者
            response = f"{data['randstr']}: {data['content']}"
            response = json.dumps(data)
            await broadcast(response,websocket)

    except websockets.exceptions.ConnectionClosedError:
        print("Client connection closed.")

    finally:
        # 将连接从列表中移除
        connected_clients.remove(websocket)
        print("Client disconnected.")

# 向所有客户端广播消息
async def broadcast(message,websocket):
    # 遍历连接列表，发送消息给每个客户端 除了发送者
    for client in connected_clients:
        if client != websocket:
            await client.send(message)

# 启动WebSocket服务器
async def start_server():
    async with websockets.serve(handle_connection, "localhost", 8000):
        await asyncio.Future()  # 保持服务器运行，直到显式取消

# 运行WebSocket服务器
asyncio.run(start_server())
#-------------------------------------------

import daemon
with daemon.DaemonContext():
    asyncio.run(start_server())