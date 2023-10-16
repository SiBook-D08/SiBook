async function displayProducts(products){
    let htmlString = ""
    products.forEach((product, index) =>{
        htmlString += `\n<div class="col-lg-4 col-md-6 mb-4">
            <div id="${product.pk}" class="card h-100 ${index === products.length - 1 ? `last-product` : ``}">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0">${product.fields.title}</h5>
                </div>
                <div class="card-body rounded-lg">
					<p class="text-muted small">Id: ${product.pk}</p>
                    <p class="text-muted small">Penulis: ${product.fields.author}</p>
                    <p class="text-muted small">Banyak Halaman: ${product.fields.num_pages}</p>
                    <p class="card-text">${product.fields.description}</p>
                </div>
            </div>
        </div>`
    })
    document.getElementById("product_cards").innerHTML = htmlString
}

async function getProducts() {
    return fetch("get-books/").then((res) => res.json())
}

async function refreshProducts(){
    const products = await getProducts()
    displayProducts(products)
}

refreshProducts()