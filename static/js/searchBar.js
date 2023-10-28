
async function searchProducts(event) {
    event.preventDefault();
    const searchInput = document.getElementById('searchInput').value;

    //jika tidak ada yang dicheck, maka searchCategory = 'title'
    let                                                         searchCategory = 'title';
    if (document.getElementById('searchAuthor').checked)        searchCategory = 'author';
    else if (document.getElementById('searchNumPages').checked) searchCategory = 'numPages';
    
    const products = await getProducts();
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
    displayProducts(filteredProducts);
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