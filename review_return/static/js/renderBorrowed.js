async function displayProductsBorrowed(products){
    let htmlString = ""
    if (products.length === 0) {
        htmlString = '<h1 class="noBorrowed">You haven\'t borrowed any books.</h1>';}

    else{
    for(const product of products){
        const idBook = product.fields.book
        const idUser = product.fields.user
        const bookResponse = await fetch(`get-book-data/${idBook}/`);
        const userResponse = await fetch(`get-user-data/${idUser}/`);
        const bookData = (await bookResponse.json())[0];
        const userData = (await userResponse.json())[0];
        htmlString += `\n<div class="col-lg-3 col-md-6 mb-4">
            <div id="${bookData.pk}" class="card h-100">
                <div class="card-header-borrowed d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0">${bookData.fields.title}</h5>
                </div>
                <div class="card-body rounded-lg">
                    <div class="inside-card">
                    <img src="${bookData.fields.img_url}" style="width: 120px; height: 160px; object-fit: cover; margin-left: 4%; border-radius: 10px;">
                    <div class="content-inside-card">
                    <p class="text-muted small" style="margin-top: 10px;">Id: ${bookData.pk}</p>
                    <p class="text-muted small">Peminjam: ${userData.fields.username}</p>
                    <p class="text-muted small">Penulis: ${bookData.fields.author}</p>
                    <p class="text-muted small">Banyak Halaman: ${bookData.fields.num_pages}</p>
                    </div>
                    </div>
					
                </div>
        
                <div class="card-footer">
                    <div style="width: 25%; margin: 0 auto;">
                    <button class="open-button" id="open-button">Return</button>
                        <dialog class="review-modal" id="modal">
                            <h2>Return "${bookData.fields.title}" ?</h2>
                            <br>
                            <form class="giveback-form" method="dialog">
                                <input type="hidden" name="user" value="${idUser}">
                                <input type="hidden" name="book" value="${bookData.pk}">
                                <textarea class="inpText" cols="50" rows="4" placeholder="Write your review of the book" background-colour: #f0ecce3></textarea>
                                <button class="close-button" id="close-button">Close</button>
                                <button class="return-button" type="submit">Return Book</button>
                            </form>
                        </dialog>
                    </div>
                </div>
            </div>
        </div>`
    }}
    document.getElementById("product_cards_borrowed").innerHTML = htmlString
}

async function getProducts() {
    return fetch("get-books/").then((res) => res.json())
}
async function getProductsBorrowed() {
    return fetch("get-books-borrowed/").then((res) => res.json())
}

async function refreshProductsBorrowed(){
    const products = await getProductsBorrowed()
    displayProductsBorrowed(products)
}
async function returnBook(id){
    let url="just-return-book/0/";
    url=url.replace('0',id);
    const response =await fetch(url,{
        method: "POST",
    });
    if(response.ok){
        refreshProductsBorrowed();
    }
}

async function reviewBook(bookId,userId,review){
    let formData = new FormData();
    formData.append('user', userId);
    formData.append('book', bookId);
    formData.append('review', review);

    const response = await fetch("add-review/", {
        method: "POST",
        body: formData
    });

    if(response.ok){
        refreshProductsBorrowed();
    }
    return false;

}





document.getElementById("product_cards_borrowed").addEventListener("click", function(event) {
    if (event.target.matches(".open-button")) {
        event.target.nextElementSibling.showModal();
    }else if (event.target.matches(".close-button")) {
        event.target.closest(".review-modal").close();
    }else if (event.target.matches(".return-button")) {
        let textField = event.target.closest(".review-modal").querySelector(".inpText");
        let bookId = event.target.closest(".review-modal").querySelector("input[name='book']").value;
        let userId = event.target.closest(".review-modal").querySelector("input[name='user']").value;
        let review = textField.value.trim();
        if (review === '') {
            // If the description is empty, call the just_return view
            returnBook(bookId)
        }
        else{
            reviewBook(bookId,userId,review)
        }
    }
});

 

refreshProductsBorrowed()