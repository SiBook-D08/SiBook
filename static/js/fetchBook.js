
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
			author: authorName,
			description: bookInfo.description.slice(0,100),
			num_pages: bookInfo.pageCount,
			avaliable: true,
		};
		
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