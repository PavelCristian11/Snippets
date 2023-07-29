function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}
//
const authorSelectNode= document.getElementById("author_select")
authorSelectNode.addEventListener('change', getOption)
function getOption(e){
    const authorSelect = e.target.value
    //
    url = "api/books" 
    if (authorSelect != 'Select Author' ){
        first_name = authorSelect.split(" ")[0]
        last_name = authorSelect.split(" ")[1]
        
        url = url + '?First name=' + first_name + '&Last name=' + last_name

    //
    }
    list_group = document.getElementById('books_list')
    removeAllChildNodes(list_group)
    //
    const publish_year_select = document.getElementById('publish_year_select')
    removeAllChildNodes(publish_year_select)
    //
    fetch(url)
        .then(r => r.json())
        .then(data =>{
            // console.log(data)
            const first_option = document.createElement('option')
            first_option.text = 'Select Publish year'
            first_option.selected = "selected"
            publish_year_select.appendChild(first_option)
            //
            data.forEach(book_selected =>{
                //
                const book_option = document.createElement('a')
                book_option.textContent = book_selected.book_name
                book_option.setAttribute('class', "list-group-item list-group-item-action")
                list_group.appendChild(book_option)
                //
                const year_option = document.createElement('option')
                // console.log(book_selected.year)
                year_option.text = book_selected.year
                year_option.value = book_selected.year
                publish_year_select.appendChild(year_option)


            })
        })
        .catch(error => console.log(error))
    }

//
const publish_year_select = document.getElementById("publish_year_select")
publish_year_select.addEventListener('change', getYearOption)
function getYearOption(e){
    const authorSelect = document.getElementById("author_select").value
    url = "api/books" 
    year = e.target.value
    if (authorSelect != 'Select Author' && year !='Select Publish year'){
        first_name = authorSelect.split(" ")[0]
        last_name = authorSelect.split(" ")[1]
        //
        url = url + '?First name=' + first_name + '&Last name=' + last_name + '&year=' + year  
    }
    else if (year !='Select Publish year') {
        url = url + '?year=' + year
    }
    else if (year == 'Select Publish year' && authorSelect != 'Select Author') {
        first_name = authorSelect.split(" ")[0]
        last_name = authorSelect.split(" ")[1]
        //
        url = url + '?First name=' + first_name + '&Last name=' + last_name 
    }
    //
    list_group = document.getElementById('books_list')
    removeAllChildNodes(list_group)
    //
    fetch(url)
        .then(r => r.json())
        .then(data =>{
            // console.log(data)
            //
            data.forEach(book_selected =>{
                //
                const book_option = document.createElement('a')
                book_option.textContent = book_selected.book_name
                book_option.setAttribute('class', "list-group-item list-group-item-action")
                list_group.appendChild(book_option)
                //
            })
        })
        .catch(error => console.log(error))
    }

