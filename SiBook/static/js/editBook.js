function editBuku(){
    const form = document.getElementById('edit-book-form')
    form.addEventListener('submit', async(e) => {
        e.preventDefault()
        const formData = new FormData(form)
        const jsonData = {}
        const response = (await fetch(`get-current-user/`))
        const userEdit = (await response.json())[0]
        formData.forEach((value, key) =>{
            if(key !== "csrfmiddlewaretoken"){
                jsonData[key] = value
            }
        })
        document.getElementById("edit-book-form").reset();
        fetch(`edit-book/`, {
            method: 'POST',
            body: JSON.stringify(jsonData)
        })
        .then(response => {
            if(response.status === 402)alert('Id tidak sesuai >:(')
        })
        .then(() => {
            const idBook = jsonData['idBook']
            const description = jsonData['description']
            const descCard = document.getElementById(`description-card-${idBook}`)
            const descModal = document.getElementById(`description-modal-${idBook}`)
            const userDesc = document.getElementById(`user-${idBook}`)
            descCard.innerHTML = description.slice(0,100)
            descModal.innerHTML = description
            userDesc.innerHTML = `Last Edited User: ${userEdit.fields.username}`
        })
    })
}

editBuku()