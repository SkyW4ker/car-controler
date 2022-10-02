from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse


# Care API
def camera_left():
    print("camera_left")

def camera_right():
    print("camera_right")

def car_up():
    print("car_up")

def car_left():
    print("car_left")

def car_right():
    print("car_right")

def car_down():
    print("car_down")


# Control Server
app = FastAPI()


@app.get("/")
def root():
    return FileResponse("./index.html")

@app.get("/style.css")
def root_style():
    return FileResponse("./style.css")

@app.get("/script.js")
def root_script():
    return FileResponse("./script.js")


# websocket: WebSocket
websocket = None

@app.websocket("/ws")
async def websocket_endpoint(new_websocket: WebSocket):
    global websocket

    websocket = new_websocket

    await websocket.accept()
    await websocket.send_text("connented")
    
    while websocket is not None:
        try:
            data = await websocket.receive_text()

            if data == 'camera/left':
                camera_left()
            elif data == 'camera/right':
                camera_right()
            elif data == 'car/up':
                car_up()
            elif data == 'car/left':
                car_left()
            elif data == 'car/right':
                car_right()
            elif data == 'car/down':
                car_down()
            else:
                print(data)
        
        except Exception:
            websocket = None