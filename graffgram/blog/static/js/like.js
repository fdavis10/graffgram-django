document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".like-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();  
            let postId = this.getAttribute("data-post-id");
            let likeIcon = this.querySelector("ion-icon");
            let likeCount = document.getElementById(`like-count-${postId}`);

            fetch(`/post/${postId}/like/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "X-Requested-With": "XMLHttpRequest"
                }
            })
            .then(response => response.json())
            .then(data => {
                likeCount.textContent = data.likes_count;

                if (data.liked) {
                    likeIcon.classList.remove("unliked");
                    likeIcon.classList.add("liked");
                } else {
                    likeIcon.classList.remove("liked");
                    likeIcon.classList.add("unliked");
                }
            })
            .catch(error => console.error("Ошибка:", error));
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        document.cookie.split(";").forEach(cookie => {
            let trimmed = cookie.trim();
            if (trimmed.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(trimmed.substring(name.length + 1));
            }
        });
    }
    return cookieValue;
}
