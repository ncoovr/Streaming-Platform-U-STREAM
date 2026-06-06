const videoContainer = document.getElementById('video-container');
let allVideos = [];

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

async function fetchVideos() {
    try {
        const response = await fetch('http://localhost:8000/videos');
        let videos = await response.json();
        
        videos = shuffleArray(videos);
        
        allVideos = videos;
        renderVideos(videos);
    } catch (error) {
        console.error("Error:", error);
    }
}

function filterArtist(category) {
    const buttons = document.querySelectorAll('.nav_button');
    buttons.forEach(button => {
        if (button.dataset.category === category) {
            button.classList.add('active');
        } else {
            button.classList.remove('active');
        }
    });
    const filtered = category === 'home'
        ? allVideos
        : allVideos.filter(video => video.categoria === category);
    renderVideos(filtered);
}

function renderVideos(videos) {
    videoContainer.replaceChildren();

    videos.forEach(video => {
        const article = document.createElement('article');
        article.className = 'video_card';
        article.onclick = () => {
            window.location.href = `stream.html?id=${video.id}`;
        };

        const thumb = document.createElement('img');
        thumb.className = 'video_thumb';
        thumb.alt = video.titulo;
        thumb.loading = 'lazy';
        thumb.src = video.poster;

        const infoSection = document.createElement('section');
        infoSection.className = 'video_info';

        const h2 = document.createElement('h2');
        h2.textContent = video.titulo;

        const span = document.createElement('span');
        span.className = 'category_tag';
        span.textContent = video.categoria ? video.categoria.replace(/_/g, ' ') : '';

        infoSection.appendChild(h2);
        infoSection.appendChild(span);

        article.appendChild(thumb);
        article.appendChild(infoSection);

        videoContainer.appendChild(article);
    });
}

document.addEventListener('DOMContentLoaded', fetchVideos);