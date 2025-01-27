document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.like-button').forEach(button => {
        button.addEventListener('click', function () {
            const id = this.dataset.id;
            const type = this.dataset.type;
            const url = `/${type}s/${id}/like/`;

            fetch(url, { method: 'GET' })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.liked) {
                        this.textContent = `Unlike (${data.like_count})`;
                    } else {
                        this.textContent = `Like (${data.like_count})`;
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });
});
