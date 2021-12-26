var socket = io();

var settings = {
    'currentselect': '',
};

var cache = [];
var cachenodes = {};

var selectLatest = false;

socket.on('connect', function() {
    E = document.getElementById('selectedUser')
    var first = E.firstElementChild;
    while (first) {
        first.remove();
        first = E.firstElementChild;
    }
    F = document.getElementById('msgList')
    var first = F.firstElementChild;
    while (first) {
        first.remove();
        first = F.firstElementChild;
    }
    G = document.getElementById('userList')
    var first = G.firstElementChild;
    while (first) {
        first.remove();
        first = G.firstElementChild;
    }
    socket.emit('chats', {
        "id": "all",
    });
});

socket.on('message', function(m) {
    console.log("message");
    if (settings.currentselect != m.receiver && settings.currentselect != m.sender) {
        return
    };

    L = document.getElementById('msgList')

    var node = document.createElement("li");
    var avatar = document.createElement("div");
    var span = document.createElement("span");
    var img = document.createElement("img");
    var content = document.createElement("div");

    if (m.self) {
        avatar.className = "message-data text-end";
        content.className = "message other-message float-right";
    } else {
        avatar.className = "message-data";
        content.className = "message my-message";
    }

    node.className = "clearfix";
    span.className = "message-data-time";
    span.textContent = `${m.time}, ${m.date}`;
    img.src = "/r/a/" + m.sender;
    img.alt = "avatar";
    content.textContent = m.content;

    avatar.appendChild(span);
    avatar.appendChild(img);
    node.appendChild(avatar);
    node.appendChild(content);
    L.appendChild(node);

    L = document.getElementById('chat-history');
    L.scrollTop = L.scrollHeight;
});

socket.on('contact', function(m) {
    if (cache.includes(m.id)) {
        if (selectLatest) {
            changeSelected(m, cachenodes[m.id]);
        }
        return
    }
    cache.push(m.id)

    L = document.getElementById('userList');

    var node = document.createElement("li");
    var img = document.createElement("img");
    var abt = document.createElement("div");
    var name = document.createElement("div");

    node.className = "clearfix";
    if (settings.currentselect == '' || selectLatest) {
        changeSelected(m, node)
        socket.emit('chats', {
            "id": m.id,
        });
    }
    node.onclick = function() {
        changeSelected(m, node)
        socket.emit('chats', {
            "id": m.id,
        });
    }
    img.src = m.avatar_url;
    img.alt = "Avatar";
    abt.className = "about";
    name.className = "name";
    name.textContent = m.username;

    abt.appendChild(name);
    node.appendChild(img);
    node.appendChild(abt);
    L.appendChild(node);
    cachenodes[m.id] = node;
});

function changeSelected(user, node) {
    if (settings.selectednode) {
        settings.selectednode.className = "clearfix";
    }

    settings.selectednode = node;
    node.className = "clearfix active";
    settings.currentselect = user.id;

    console.log("changing")
    E = document.getElementById('selectedUser')
    var first = E.firstElementChild;
    while (first) {
        first.remove();
        first = E.firstElementChild;
    }
    F = document.getElementById('msgList')
    var first = F.firstElementChild;
    while (first) {
        first.remove();
        first = F.firstElementChild;
    }

    var img = document.createElement("img");
    var abt = document.createElement("div");
    var name = document.createElement("h6");

    img.src = user.avatar_url
    img.alt = "Avatar"
    abt.className = "chat-about"
    name.className = "m-b-0"
    name.textContent = user.username

    abt.appendChild(name)
    E.appendChild(img)
    E.appendChild(abt)
};

chat = document.getElementById('chat-send');
chat.addEventListener("keyup", function(e) {
    if (e.keyCode == 13) {
        socket.emit('message', {
            content: e.target.value,
            target: settings.currentselect
        });
        console.log(settings.currentselect)
    }
});

function openChat() {
    document.getElementById("chat").style.display = "block";
    document.getElementById("openChat").style.display = "none";
}

function closeChat() {
    document.getElementById("chat").style.display = "none";
    document.getElementById("openChat").style.display = "block";
}

function requestID(e) {
    selectLatest = true
    socket.emit('contact', {
        id: e,
    });
    openChat()
    socket.emit('chats', {
        "id": e,
    });
}

document.getElementById("chat").style.display = "none";