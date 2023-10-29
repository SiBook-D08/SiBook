
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
                    <strong> <p class="card-text">Penulis: ${author}</p> </strong>
                    <p class="card-text">${book.fields.description.slice(0,100)}</p>
                </div>

                <div class="modal fade" id="exampleModal${book.pk}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Favoritkan Buku</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form id="form${book.pk}" onsubmit="return false;">
                                    <div class="mb-3">
                                        <label for="alasan${book.pk}" class="col-form-label">Apa alasan kamu memfavoritkan buku ini?</label>
                                        <input type="text" class="form-control" id="alasan${book.pk}" name="alasan" required></input>
                                    </div>
                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Batalkan</button>
                                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal" onclick=addToFavorited(${book.pk})>Favoritkan</button>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="card-footer"> <button class="text-search" data-bs-toggle="modal" data-bs-target="#exampleModal${book.pk}">Tambahkan ke Favorit</button> </div>
                
            </div>
        </div>`
    })
    document.getElementById("product_cards").innerHTML = htmlString
}

async function showFavoritedBooks(books){
    let htmlString = ""

    if (books.length == 0){
        htmlString = '<strong> <p style="text-align: center;"> Kamu belum memiliki buku favorit ＞︿＜ </p> </strong>'
    }

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

        htmlString += `\n
        <div class="col-lg-4 col-md-6 mb-4">
            <div id="${bookData.pk}" class="card h-100" style="border: 2px solid #003300;">
                <div class="card-header favorited d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0" ">${bookData.fields.title}</h5>
                </div>
                <div class="card-body favorited rounded-lg">	
                    <p class="card-text">Alasan kamu memfavoritkan buku ini:</p> 
                    <strong> <p class="card-text">${book.fields.alasan}</p> </strong>
                </div>
                <div class="card-footer d-flex justify-content-between align-items-center ">
                    <button class="text-search" onclick=removeFromFavorited(${book.pk})>Hapus dari Favorit</button>
                </div>
            </div>
        </div>`
    }
    document.getElementById("favorited_book_cards").innerHTML = htmlString
}

async function addToFavorited(id){
    const alasan = document.getElementById('alasan' + id).value;
    if (!alasan) {
        alert('Alasan wajib diisi!');
        return;
    }

    const formData = new FormData();
    formData.append('alasan', alasan);

    fetch(`add-to-favorited/${id}/`, {
        method: 'POST',
        body: formData,
    }).then(await getFavoritedBooks()).then(showFavoritedBooks(await getFavoritedBooks()))
    refreshEveryBook()
    document.getElementById('favorited_book_cards').scrollIntoView({behavior: "smooth"});
}

async function removeFromFavorited(id){
    await fetch(`remove-from-favorited/${id}/`, {
        method: 'POST',
    })
    showFavoritedBooks(await getFavoritedBooks())
    refreshEveryBook()
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

async function refreshEveryBook(){
    refreshBooks()
    refreshFavoritedBooks()
}

document.getElementById('scrollToBooks').addEventListener('click', function() {
    document.getElementById('product_cards').scrollIntoView({behavior: "smooth"});
});

async function searchProducts(event) {
    event.preventDefault();
    const searchInput = document.getElementById('searchInput').value;

    //jika tidak ada yang dicheck, maka searchCategory = 'title'
    let                                                         searchCategory = 'title';
    if (document.getElementById('searchAuthor').checked)        searchCategory = 'author';
    else if (document.getElementById('searchNumPages').checked) searchCategory = 'numPages';
    
    const products = await getBooks();
    let filteredProducts = products.filter(product => {
        switch (searchCategory) {
            case 'author':
                return product.fields.author.toLowerCase().includes(searchInput.toLowerCase());
            case 'numPages':
                return product.fields.num_pages <= (+searchInput);
            case 'title':
                return product.fields.title.toLowerCase().includes(searchInput.toLowerCase());
        }
    });
    showBooks(filteredProducts);
}

const checkBoxes = ['searchTitle', 'searchAuthor', 'searchNumPages']
function handleCheckboxChange(checkboxId){//supaya pada setiap waktu, maks 1 checkbox yang nyala
    for(const checkbox of checkBoxes){
        if(checkbox !== checkboxId){
            document.getElementById(checkbox).checked = false
        }
    }
}

function settingUp(){
    document.getElementById('searchTitle').addEventListener('change', () => handleCheckboxChange('searchTitle'));
    document.getElementById('searchAuthor').addEventListener('change', () => handleCheckboxChange('searchAuthor'));
    document.getElementById('searchNumPages').addEventListener('change', () => handleCheckboxChange('searchNumPages'));
    
    document.getElementById('searchForm').addEventListener('submit', (event) => {
        event.preventDefault();  // Prevent default form submission behavior
        searchProducts(event);
    });
}
settingUp()
refreshEveryBook()