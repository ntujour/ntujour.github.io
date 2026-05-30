/**
 * Homepage 2x2 grid flip card slideshow
 */
(function () {
    var slideshow = document.getElementById('hero-slideshow');
    if (!slideshow) return;

    // Collect all image sources pre-rendered inside the container
    var imgs = slideshow.querySelectorAll('img');
    var imagePool = [];
    for (var i = 0; i < imgs.length; i++) {
        var src = imgs[i].getAttribute('src');
        if (src && imagePool.indexOf(src) === -1) {
            imagePool.push(src);
        }
    }

    // Fallback if no images found
    if (imagePool.length === 0) {
        imagePool = [
            'images/hero/hero-1.png',
            'images/hero/hero-4.png',
            'images/hero/hero-5.png',
            'images/hero/hero-6.png',
            'images/hero/hero-7.jpg',
            'images/hero/hero-8.jpg'
        ];
    }

    // If we have fewer than 4 images, duplicate them to fill the pool
    while (imagePool.length < 4) {
        imagePool = imagePool.concat(imagePool);
    }

    // Create the grid HTML
    var gridHtml = '<div class="hero-flip-grid">';
    for (var j = 0; j < 4; j++) {
        var initialImg = imagePool[j];
        gridHtml += 
            '<div class="hero-flip-card" id="hero-flip-card-' + j + '">' +
            '  <div class="hero-flip-inner">' +
            '    <div class="hero-flip-front">' +
            '      <img src="' + initialImg + '" alt="Hero Image">' +
            '    </div>' +
            '    <div class="hero-flip-back">' +
            '      <img src="" alt="Hero Image">' +
            '    </div>' +
            '  </div>' +
            '</div>';
    }
    gridHtml += '</div>';

    // Clear the slideshow and insert the grid
    slideshow.innerHTML = gridHtml;

    // Track state of each card
    var cardsState = [];
    for (var k = 0; k < 4; k++) {
        cardsState.push({
            element: document.getElementById('hero-flip-card-' + k),
            visibleFace: 'front',
            currentImg: imagePool[k]
        });
    }

    // Helper to flip a random card
    function flipRandomCard() {
        // Pick a random card slot (0 to 3)
        var cardIdx = Math.floor(Math.random() * 4);
        var state = cardsState[cardIdx];

        // Gather all images currently visible on any card to avoid duplicates
        var visibleImages = cardsState.map(function (c) { return c.currentImg; });

        // Find an image in the pool that is not currently visible
        var availablePool = imagePool.filter(function (img) {
            return visibleImages.indexOf(img) === -1;
        });

        // If no unique images, pick any image different from the card's current image
        if (availablePool.length === 0) {
            availablePool = imagePool.filter(function (img) {
                return img !== state.currentImg;
            });
        }

        if (availablePool.length === 0) return; // No alternative image

        var newImg = availablePool[Math.floor(Math.random() * availablePool.length)];

        // Set the image on the hidden face and flip
        if (state.visibleFace === 'front') {
            var backImg = state.element.querySelector('.hero-flip-back img');
            backImg.src = newImg;
            state.element.classList.add('flipped');
            state.visibleFace = 'back';
        } else {
            var frontImg = state.element.querySelector('.hero-flip-front img');
            frontImg.src = newImg;
            state.element.classList.remove('flipped');
            state.visibleFace = 'front';
        }
        state.currentImg = newImg;
    }

    // Start rotation interval (flip one card every 3 seconds)
    setInterval(flipRandomCard, 3000);
})();
