new QWebChannel(qt.webChannelTransport, function(channel) {
    window.backend = channel.objects.backend;

    // Load apps grid
    fetch('../apps.json')
        .then(res => res.json())
        .then(apps => {
            const grid = document.getElementById('grid');
            apps.forEach(a => {
                // Convert app name to safe filename
                const iconName = a.name.replace(/ /g, "_") + ".png";
                const tile = document.createElement('div');
                tile.className = 'tile';
                tile.innerHTML = `<img src="../icons/${iconName}"><span>${a.name}</span>`;
                tile.onclick = () => backend.launch(a.name);
                grid.appendChild(tile);
            });
        });

    // Menu toggle
    const menuButton = document.getElementById('menu-button');
    const menu = document.getElementById('menu');

    menuButton.onclick = () => {
        menu.classList.toggle('show');
    };

    // Menu actions
    document.getElementById('close-app').onclick = () => backend.closeApp();

    document.getElementById('wol-pc').onclick = () => {
        const mac = prompt("Enter PC MAC address:");
        if(mac) backend.wakePC(mac);
    };

    document.getElementById('shutdown-pi').onclick = () => {
        if(confirm("Are you sure you want to shutdown the Raspberry Pi?")) {
            backend.shutdownPi();
        }
    };

    document.getElementById('reboot-pi').onclick = () => {
        if(confirm("Are you sure you want to reboot the Raspberry Pi?")) {
            backend.rebootPi();
        }
    };
});

