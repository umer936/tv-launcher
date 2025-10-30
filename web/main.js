new QWebChannel(qt.webChannelTransport, function(channel) {
    window.backend = channel.objects.backend;

    fetch('../apps.json')
        .then(res => res.json())
        .then(apps => {
            const grid = document.getElementById('grid');
            apps.forEach(a => {
                const tile = document.createElement('div');
                tile.className = 'tile';
                tile.innerHTML = `<img src="../icons/${a.icon.split('/').pop()}"><span>${a.name}</span>`;
                tile.onclick = () => backend.launch(a.name);
                grid.appendChild(tile);
            });
        });
});

