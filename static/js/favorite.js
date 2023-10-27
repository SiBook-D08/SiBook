async function showBooks(books){
    let htmlString = ""
    books.forEach((book, index) =>{
        let author = book.fields.author
        const koma = author.indexOf(",");
        if (koma !== -1){
            author=author.substring(0,koma) + ",et al.";
        }
        htmlString += `\n
        <div class="col-lg-4 col-md-6 mb-4">
            <div id="${book.pk}" class="card h-100">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0" ">${book.fields.title}</h5>
                </div>
                <div class="card-body rounded-lg">
                    <p class="card-text">Penulis: ${author}</p>
                    <p class="card-text">${book.fields.description.slice(0,100)}</p>
                </div>
                <div class="card-footer d-flex justify-content-between align-items-center ">
                    <button onclick=addToFavorited(${book.pk})>Favoritkan</button>
                </div>
            </div>
        </div>`
    })
    document.getElementById("book_cards").innerHTML = htmlString
}

async function showFavoritedBooks(books){
    let htmlString = ""
    for(const book of books){
        const bookID = book.fields.book
        const userID = book.fields.user
        const bookResponse = await fetch(`get-book-data/${bookID}/`);
        const userResponse = await fetch(`get-user-data/${userID}/`);
        const bookData = (await bookResponse.json())[0];
        const userData = (await userResponse.json())[0];
        let author= bookData.fields.author;
        const koma = author.indexOf(",");

        if (koma !== -1){
            author=author.substring(0,koma) + ",et al.";
        }

        htmlString += `\n<div class="col-lg-4 col-md-6 mb-4">
            <div id="${bookData.pk}" class="card h-100">
                <div class="card-header-favorited d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0" style="background-color:red; border-radius: 5px;"> UNAVAILABLE</h5>
                </div>
                <div class="card-body-favorited rounded-lg" style="text-align:center;">	
                    <strong> <p class="card-text">Peminjam: ${userData.fields.username}</p> </strong>
                    <strong> <p class="card-text">${bookData.fields.title}</p> </strong>
                    <strong> <p class="card-text">by: ${author}</p> </strong>
                </div>
                <div class = card-footer-favorited > </div>
            </div>
        </div>`
    }
    document.getElementById("cards_favorited_book").innerHTML = htmlString
}

async function addToFavorited(id){
    fetch(`add-to-favorited/${id}/`, {
        method: 'POST',
    }).then(await getFavoritedBooks()).then(showFavoritedBooks(await getFavoritedBooks()))
}

async function removeFromFavorited(id) {
    fetch(`remove-from-favorited/${id}/`, {
        method: 'POST',
    }).then(await getFavoritedBooks()).then(showFavoritedBooks(await getFavoritedBooks()))
    
}

async function getBooks() { 
    return fetch("get-books/").then((res) => res.json()) 
}

async function getFavoritedBooks() { 
    return fetch("get-favorited-books/").then((res) => res.json()) 
}

async function refreshBooks(){
    const books = await getBooks()
    showBooks(books)
}

async function refreshFavoritedBooks(){
    const books = await getFavoritedBooks()
    showFavoritedBooks(books)
}

async function refreshEveryProduct(){
    refreshBooks()
    refreshFavoritedBooks()
}

refreshEveryProduct()