// init socket
const socket = new WebSocket("ws://" + window.location.host + "/ws");

socket.onmessage = function(event) {
    switch (event.data) {
        case "connented":
            document.getElementById("camera-container").style.backgroundColor = "green"
            return;
    }
}

// Buttons
document.getElementById("camera-left").addEventListener("mousedown", () => {
    socket.send('camera/left')
})

document.getElementById("camera-right").addEventListener("mousedown", () => {
    socket.send('camera/right')
})

document.getElementById("car-up").addEventListener("mousedown", () => {
    socket.send('car/up')
})

document.getElementById("car-left").addEventListener("mousedown", () => {
    socket.send('car/left')
})

document.getElementById("car-right").addEventListener("mousedown", () => {
    socket.send('car/right')
})

document.getElementById("car-down").addEventListener("mousedown", () => {
    socket.send('car/down')
})
