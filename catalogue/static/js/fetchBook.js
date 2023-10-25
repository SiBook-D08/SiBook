
async function fetchByLink(linkAPI, authorName){
	const response = await fetch(linkAPI);
    const data = await response.json();
    
    if (!data.items) {
        console.error('No items found in the response');
        return;
    }
	
    for (const item of data.items) {
		const bookInfo = item.volumeInfo;
		const postData = {
			title: bookInfo.title,
			author: typeof bookInfo.authors === 'undefined' ? 'Raditya Dika, Najwa Shihab' : bookInfo.authors.join(', '),
			description: bookInfo.description || "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
			num_pages: bookInfo.pageCount,
			img_url: typeof bookInfo.imageLinks === 'undefined' ? "https://books.google.com/books/content?id=SXGCEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api" : bookInfo.imageLinks.smallThumbnail ,
			avaliable: true,
		};
		
		// console.log(bookInfo.title,bookInfo.description)
		await fetch("add-new-data/", {
			method: 'POST',
			headers: {
			},
			body: JSON.stringify(postData)
		});
    }
}

async function fetchAllBook() {
    const listAuthor = ['christopher', 'naomi', 'keyes', 'rowling', 'raditya', 'najwa', 'tere', 'andrea', 'king', 'crichton', 'riordan', 'jason', 'siahaan', 'adam', 'jhon', 'budi', 'asep', 'adrian']
    for(const nama of listAuthor){
        fetchByLink(`https://www.googleapis.com/books/v1/volumes?q=inauthor:${nama}&`, nama)
    }
}

fetchAllBook()