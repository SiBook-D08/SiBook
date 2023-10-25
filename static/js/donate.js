function donateAjaxPost(e) {
    e.preventDefault();
    const formElement = document.getElementById("donate-form");
    fetch("add-book-ajax/", {
        method: "POST",
        body: new FormData(formElement),
    })
    .then(async (res) => {
        if (res.status === 302) {
            window.location.href = "/login/";
            return;
        }
        const obj = await res.json();
        if (obj.isValid) {
            document.getElementById("error-message").classList.add("hidden");
            document.getElementById("success-message").classList.remove("hidden");
        } else {
            document.getElementById("success-message").classList.add("hidden");
            document.getElementById("error-message").classList.remove("hidden");
        }
    });
    formElement.reset();
}
