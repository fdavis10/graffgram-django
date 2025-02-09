document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("comment-form").addEventListener("submit", function (event) {
        event.preventDefault(); 

        let form = this;
        let formData = new FormData(form);
        let url = form.getAttribute("action");
        let commentInput = document.getElementById("comment-content");

        fetch(url, {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                let commentsList = document.getElementById("comments-list");

                let noCommentsMessage = document.getElementById("no-comments");
                if (noCommentsMessage) {
                    noCommentsMessage.remove();
                }

                let newComment = document.createElement("div");
                newComment.classList.add("comment_detail");
                newComment.innerHTML = `
                    <p><strong>${data.author}</strong>: ${data.content}</p>
                    <span class="comment_date_detail">${data.created_at}</span>
                `;

                commentsList.prepend(newComment);

                commentInput.value = "";
            }
        })
        .catch(error => console.error("Ошибка:", error));
    });
});
