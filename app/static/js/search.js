if (!socket) {
    var socket = io();
}

console.log('load')

socket.on('users', function(users) {
    // Vidage du "cache"
    var parent = document.getElementById("recherche-user");
    var first = parent.firstElementChild;
    while (first) {
        first.remove();
        first = parent.firstElementChild;
    }

    for (i = 0; i < users.length; i++) {
        var a = document.createElement("a");
        var img = document.createElement("img");
        img.src = users[i]["avatar"];
        img.className = "recherche-photo";

        a.textContent = users[i]["username"];
        a.href = `p/${users[i]["id"]}`
        a.appendChild(img);
        parent.appendChild(a);
    }
})

recherche = document.getElementById('recherche-user-input');
recherche.addEventListener("keyup", function(e) {
    socket.emit('search_users', {
        query: e.target.value,
    });
});