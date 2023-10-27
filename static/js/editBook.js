const form = document.getElementById('edit-book-form')
form.addEventListener('submit', (e) => {
    e.preventDefault()
    const formData = new FormData(form)
    const jsonData = {}
    formData.forEach((value, key) =>{
        if(key !== "csrfmiddlewaretoken"){
            console.log(key,value)
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
        descCard.innerHTML = description.slice(0,100)
        descModal.innerHTML = description
    })
})