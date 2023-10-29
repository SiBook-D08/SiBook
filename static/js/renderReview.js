async function displayReviews(reviews) {
    let htmlString = "";
    for (const rev of reviews) {
        const idBook = rev.fields.book
        const idUser = rev.fields.user
        const bookResponse = await fetch(`get-book-data/${idBook}/`);
        const userResponse = await fetch(`get-user-data/${idUser}/`);
        const bookData = (await bookResponse.json())[0];
        const userData = (await userResponse.json())[0];
        htmlString += `
            <div style="margin-bottom: 3%;">
                <div class="tabs">
                    <div class="left-tab">${bookData.fields.title}</div>
                    <div class="tab-divider"></div>
                    <div class="right-tab">${rev.fields.review_date}</div>
                </div>
                <div class="tab-content">
                    <p> ✾ From : ${userData.fields.username}</p>
                    <div style="margin-left: 1%;"><p>${rev.fields.review}</p></div>
                </div>
            </div>
        `;
    }

    document.getElementById("reviewCard").innerHTML = htmlString;
}

async function getReviews() {
    return fetch("get-reviews/").then((res) => res.json())
}
async function getReviewsExperimental(){
    return fetch("get-reviews-experimental/").then((res) => res.json())
}
async function refreshReviews(){
    const reviews = await getReviews()
    displayReviews(reviews)
}
async function refreshReviews() {
    const selectElement = document.getElementById("sort-select");
    const selectedValue = selectElement.value;
    const reviews = await getReviews();

    if (selectedValue === "oldest") {
        // Sort reviews by review_date in ascending order (oldest first)
        reviews.sort((a, b) => new Date(a.fields.review_date) - new Date(b.fields.review_date));
    } else {
        // Default sorting: Sort reviews by review_date in descending order (newest first)
        reviews.sort((a, b) => new Date(b.fields.review_date) - new Date(a.fields.review_date));
    }

    displayReviews(reviews);
}

async function searchProducts(event) {
    event.preventDefault();
    const searchInput = document.getElementById('searchInput').value;

    
    let searchCategory = 'title';
    
    //need to
    const reviews = await getReviews();
    const filteredReviews = await Promise.all(
        reviews.map(async (rev) => {
            const idBook = rev.fields.book;
            const bookResponse = await fetch(`get-book-data/${idBook}/`);
            const bookData = (await bookResponse.json())[0];

            if (bookData.fields.title.toLowerCase().includes(searchInput.toLowerCase())) {
                return rev;
            }
        })
    );

    displayReviews(filteredReviews.filter(Boolean)); // Filter out undefined entries
}


function settingUp(){
    document.getElementById('searchForm').addEventListener('submit', (event) => {
        event.preventDefault();  // Prevent default form submission behavior
        searchProducts(event);
    });
}
settingUp()

document.getElementById("sort-select").addEventListener("change", refreshReviews);

refreshReviews()




