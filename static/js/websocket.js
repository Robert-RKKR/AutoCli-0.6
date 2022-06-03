function collect_socket(task_type) {
    var socket = new WebSocket("ws://127.0.0.1:8000/ws/collect_data/");

    socket.onmessage = function(event) {
        var collect = event.data;
        document.querySelector("#collect_output").innerText = collect;
    }
}

function logger_socket(task_type) {
    var socket = new WebSocket("ws://127.0.0.1:8000/ws/logger/");

    socket.onmessage = function(event) {
        var collect = event.data;
        var destination = document.querySelector("#logger_output");
        var myObj = JSON.parse(collect);
        var data = Object.values(myObj);

        for(let i=0; i<data.length; i++) {
            let row = data[i];
            var container = document.createElement("li");
            container.innerText = row[2];
            destination.appendChild(container);
        }
    }
}

collect_socket()
logger_socket()
