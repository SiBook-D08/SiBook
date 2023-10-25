async function displayProducts(products){
    let htmlString = ""
    products.forEach((product, index) =>{
        console.log(product.fields.title, product.fields.description)
        htmlString += `\n<div class="col-lg-4 col-md-6 mb-4">
            <div id="${product.pk}" class="card h-100 ${index === products.length - 1 ? `last-product` : ``}">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0">${product.fields.title}</h5>
                </div>
                <div class="card-body rounded-lg">
                    <p class="text-muted small">Penulis: ${product.fields.author}</p>
                    <p class="text-muted small card-text">${product.fields.description.slice(0,100)}</p>
                </div>

                <div class="modal fade" id="exampleModal${product.pk}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Book Information</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="row">
                                    <div class="col-md-6">
                                        <img src="${product.fields.img_url}" alt="Book Image" class="img-fluid">
                                    </div>
                                    <div class="col-md-6">
                                        <ul class="list-group">
                                            <li class="list-group-item"><strong>Title:</strong> <span id="bookTitle">${product.fields.title}</span></li>
                                            <li class="list-group-item"><strong>Author:</strong> <span id="bookAuthor">${product.fields.author}</span></li>
                                            <li class="list-group-item"><strong>Page Number:</strong> <span id="bookPageNumber">${product.fields.num_pages}e</span></li>
                                            <li class="list-group-item"><strong>Description:</strong> <span id="bookDescription">${product.fields.description}</span></li>
                                            <li class="list-group-item"><strong>Id:</strong> <span id="bookId">${product.pk}</span></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="card-footer"> <button data-bs-toggle="modal" data-bs-target="#exampleModal${product.pk}">See More</button> </div>
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