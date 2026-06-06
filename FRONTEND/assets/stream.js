const urlParams = new URLSearchParams(window.location.search);
const videoId = urlParams.get('id');

const videoElement = document.getElementById('main-video');
const titleElement = document.getElementById('video-title');
const categoryElement = document.getElementById('video-category');
const commentsList = document.getElementById('comments-list');
const commentForm = document.getElementById('comment-form');

async function loadVideoDetails() {
    if (!videoId) return;

    const response = await fetch(`http://localhost:8000/videos/${videoId}`);
    const video = await response.json();
    
    titleElement.textContent = video.titulo;
    categoryElement.textContent = video.categoria ? video.categoria.replace(/_/g, ' ') : "";
    videoElement.src = video.source;

    loadComments();
    loadRecommended(video.categoria);
}

async function loadRecommended(categoria) {
    try {
        const response = await fetch(`http://localhost:8000/videos/recomendaciones/${categoria}`);
        let recommendations = await response.json();
        recommendations = recommendations.filter(item => item.id !== Number(videoId));
        renderRecommended(recommendations);
    } catch (error) {
        console.error(error);
    }
}

function renderRecommended(videos) {
    const recommendedList = document.getElementById('recommended-list');
    if (!recommendedList) return;
    
    recommendedList.replaceChildren();

    videos.forEach(video => {
        const card = document.createElement('div');
        card.className = 'recommendation_item';
        card.onclick = () => {
            window.location.href = `stream.html?id=${video.id}`;
        };

        const thumb = document.createElement('img');
        thumb.className = 'recommendation_thumb';
        thumb.alt = video.titulo;
        thumb.src = video.poster;

        const textContainer = document.createElement('div');
        textContainer.className = 'recommendation_text';
        
        const h4 = document.createElement('h4');
        h4.textContent = video.titulo;
        
        const span = document.createElement('span');
        span.textContent = video.categoria ? video.categoria.replace(/_/g, ' ') : '';

        textContainer.appendChild(h4);
        textContainer.appendChild(span);

        card.appendChild(thumb);
        card.appendChild(textContainer);
        recommendedList.appendChild(card);
    });
}

async function loadComments() {
    const response = await fetch(`http://localhost:8000/videos/${videoId}/comments`);
    const comments = await response.json();
    
    commentsList.replaceChildren();
    
    if (comments.length === 0) {
        const p = document.createElement('p');
        p.textContent = 'No hay comentarios aún.';
        commentsList.appendChild(p);
        return;
    }

    comments.forEach(comment => {
        const div = document.createElement('div');
        div.className = 'comment-item';
        
        const p = document.createElement('p');
        p.textContent = comment.texto;
        
        div.appendChild(p);
        commentsList.appendChild(div);
    });
}

commentForm.onsubmit = async (e) => {
    e.preventDefault();
    const input = document.getElementById('comment-text');
    const texto = input.value;

    await fetch('http://localhost:8000/comments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            texto: texto,
            video_id: parseInt(videoId)
        })
    });

    input.value = '';
    loadComments();
};

document.addEventListener('DOMContentLoaded', loadVideoDetails);