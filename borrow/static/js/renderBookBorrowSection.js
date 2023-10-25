async function displayProductsBorrowed(products){
    let htmlString = ""
    for(const product of products){
        const idBook = product.fields.book
        const idUser = product.fields.user
        const bookResponse = await fetch(`get-book-data/${idBook}/`);
        const userResponse = await fetch(`get-user-data/${idUser}/`);
        const bookData = (await bookResponse.json())[0];
        const userData = (await userResponse.json())[0];
        
        htmlString += `\n<div class="col-lg-4 col-md-6 mb-4">
            <div id="${bookData.pk}" class="card h-100">
                <div class="card-header-borrowed d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0">${bookData.fields.title}</h5>
                </div>
                <div class="card-body-borrowed rounded-lg">
					<p class="text-muted small">Id: ${bookData.pk}</p>
                    <p class="text-muted small">Peminjam: ${userData.fields.username}</p>
                    <p class="text-muted small">Penulis: ${bookData.fields.author}</p>
                    <p class="text-muted small">Banyak Halaman: ${bookData.fields.num_pages}</p>
                    <p class="card-text">${bookData.fields.description}</p>
                </div>
                <div class = card-footer-borrowed > </div>
            </div>
        </div>`
    }
    document.getElementById("product_cards_borrowed").innerHTML = htmlString
}
async function displayProducts(products){
    let htmlString = ""
    products.forEach((product, index) =>{
        htmlString += `\n<div class="col-lg-4 col-md-6 mb-4">
            <div id="${product.pk}" class="card h-100">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0">${product.fields.title}</h5>
                </div>
                <div class="card-body rounded-lg">
					<p class="text-muted small">Id: ${product.pk}</p>
                    <p class="text-muted small">Penulis: ${product.fields.author}</p>
                    <p class="text-muted small">Banyak Halaman: ${product.fields.num_pages}</p>
                    <p class="card-text">${product.fields.description}</p>
                </div>
                <div class="card-footer d-flex justify-content-between align-items-center ">
                    <button onclick=addToCart(${product.pk})>Masukkan Keranjang</button>
                </div>
            </div>
        </div>`
    })
    document.getElementById("product_cards").innerHTML = htmlString
}
async function displayCart(products){
    let htmlString=""
    if (products==null){
        htmlString=`Belum ada buku nih di keranjang kamu :(`
    }
    else{
        for(const product of products){
            const idBook = product.fields.book
            const idUser = product.fields.user
            const bookResponse = await fetch(`get-book-data/${idBook}/`);
            const userResponse = await fetch(`get-user-data/${idUser}/`);
            const bookData = (await bookResponse.json())[0];
            const userData = (await userResponse.json())[0];
            
            htmlString += `
            <div style="text-align: center;">
                <tr style="display: flex; justify-content: space-between;"> 
                    <td style="color: #003300; font-weight: 600;"> ${bookData.fields.title} </td>
                    <td> <button class="button-search" onclick=removeFromCart(${product.pk})>Keluarkan</button> </td>
                </tr>
            </div>
            `
        }
        htmlString+=`<br><a href="" style="color: black; text-decoration: none;"> <button onclick=addToList()>Pinjam</button>`
    }
    
    if((htmlString.match(/Keluarkan/g) || []).length !== 0 && (htmlString.match(/Keluarkan/g) || []).length === (document.getElementById("cart").innerHTML.match(/Keluarkan/g) || []).length){
        alert("Udah ada!")
    }
    document.getElementById("cart").innerHTML = htmlString
}

async function getCart() { return fetch("get-cart/").then((res) => res.json()) }
async function getProducts() { return fetch("get-books/").then((res) => res.json()) }
async function getProductsBorrowed() { return fetch("get-books-borrowed/").then((res) => res.json()) }

async function refreshProducts(){
    const products = await getProducts()
    displayProducts(products)
}
async function refreshCart(){
    const products = await getCart()
    displayCart(products)
}
async function refreshEveryProduct(){
    refreshProducts()
    refreshProductsBorrowed()
}
async function refreshProductsBorrowed(){
    const products = await getProductsBorrowed()
    displayProductsBorrowed(products)
}

async function addToCart(id) {
    fetch(`add-to-cart/${id}/`, {
        method: 'POST',
    }).then(await getCart()).then(displayCart(await getCart()))
}

async function removeFromCart(id) {
    fetch(`remove-cart/${id}/`, {
        method: 'POST',
    }).then(await getCart()).then(displayCart(await getCart()))
    
}

function addToList() {
    fetch(`add-to-list/`, {
        method: 'POST',
    })
    alert("Berhasil Meminjam Buku")
    
}

refreshEveryProduct()
refreshCart()