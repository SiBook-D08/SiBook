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
        const errorMsg = document.getElementById("error-message");
        const successMsg = document.getElementById("success-message");
        const fullMsg = document.getElementById("full-message");
        const alrExistsMsg = document.getElementById("alr-exists-message")
        if (obj.status === "valid") {
            errorMsg.classList.add("hidden");
            fullMsg.classList.add("hidden");
            alrExistsMsg.classList.add("hidden");
            successMsg.classList.remove("hidden");
        } else if (obj.status === "invalid") {
            successMsg.classList.add("hidden");
            fullMsg.classList.add("hidden");
            alrExistsMsg.classList.add("hidden");
            errorMsg.classList.remove("hidden");
        } else if (obj.status === "full") {
            errorMsg.classList.add("hidden");
            successMsg.classList.add("hidden");
            alrExistsMsg.classList.add("hidden");
            fullMsg.classList.remove("hidden");
        } else if (obj.status === "alrExists") {
            errorMsg.classList.add("hidden");
            successMsg.classList.add("hidden");
            fullMsg.classList.add("hidden");
            alrExistsMsg.classList.remove("hidden");
        }
    });
    formElement.reset();
}
