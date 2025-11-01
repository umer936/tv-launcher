new QWebChannel(qt.webChannelTransport, function(channel) {
    window.backend = channel.objects.backend;

    // Load apps grid
    fetch('../apps.json')
        .then(res => res.json())
        .then(apps => {
            const grid = document.getElementById('grid');
            apps.forEach((a, index) => {
                // Convert app name to safe filename
                const iconName = a.name.replace(/ /g, "_") + ".png";
                const tile = document.createElement('div');
                tile.className = 'tile';
                tile.setAttribute('tabindex', index + 1); // make focusable
                tile.innerHTML = `<img src="../icons/${iconName}" onerror="this.src='../icons/default.png'"><span>${a.name}</span>`;
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

document.addEventListener('keydown', (e) => {
    const tiles = Array.from(document.querySelectorAll('.tile'));
    const cols = 4; // number of tiles per row, adjust to your grid
    let currentIndex = tiles.findIndex(tile => tile === document.activeElement);

    if (currentIndex === -1) {
        // If nothing is focused, focus the first tile
        tiles[0]?.focus();
        return;
    }

    switch (e.key) {
        case 'ArrowRight':
            if (currentIndex < tiles.length - 1) tiles[currentIndex + 1].focus();
            break;
        case 'ArrowLeft':
            if (currentIndex > 0) tiles[currentIndex - 1].focus();
            break;
        case 'ArrowDown':
            if (currentIndex + cols < tiles.length) tiles[currentIndex + cols].focus();
            break;
        case 'ArrowUp':
            if (currentIndex - cols >= 0) tiles[currentIndex - cols].focus();
            break;
        case 'Enter':
            document.activeElement.click();
            break;
    }
});


