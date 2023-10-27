async function displayProducts(products){
    let htmlString = ""
    products.forEach((product, index) =>{
        let author = product.fields.author
        const koma = author.indexOf(",");
        if (koma !== -1){
            console.log(koma);
            author=author.substring(0,koma) + ",et al.";
        }
        htmlString += `\n<div class="col-lg-4 col-md-6 mb-4">
            <div id="${product.pk}" class="card h-100">
                <div class="card-header d-flex justify-content-center align-items-center" style="text-align: center;">
                    <h5 class="card-title mb-0" style="color: white; background-color: rgb(8, 169, 8); border-radius: 5px;">AVAILABLE</h5>
                </div>
                <div class="card-body rounded-lg" style="text-align:center">
                    <strong> <p class="card-text">${product.fields.title}</p> </strong>
                    <strong> <p class="card-text">by: ${author}</p> </strong>
                </div>
                <div class="card-footer d-flex justify-content-between align-items-center ">
                    <button onclick=addToCart(${product.pk})>Masukkan Keranjang</button>
                </div>
            </div>
        </div>`
    })
    document.getElementById("product_cards").innerHTML = htmlString
}

async function getProducts() { return fetch("get-books/").then((res) => res.json()) }

async function refreshProducts(){
    const products = await getProducts()
    displayProducts(products)
}

async function refreshEveryProduct(){
    refreshProducts()
    refreshProductsBorrowed()
}

refreshEveryProduct()