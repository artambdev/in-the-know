const deleteModal = new bootstrap.Modal(document.getElementById("delete-modal"));
const deleteButtons = document.getElementsByClassName("delete-button");
const deleteConfirm = document.getElementById("delete-confirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let postSlug = e.target.getAttribute("post_slug");
      deleteConfirm.href = `/${postSlug}/delete/`;
      deleteModal.show();
    });
}