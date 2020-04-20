// Gets container that holds tag category divs
const category_container = document.getElementById('category-container');

// Gets all tag categories
function get_tag_categories() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     let categories = JSON.parse(this.responseText);
     for (let category of categories) {
       display_tag_category(category);
     }
   }
  };
  xhttp.open("GET", "http://127.0.0.1:5000/tag_categories");
  xhttp.send();
}

// Appending a div for each tag category for display on index.html
function display_tag_category(category) {
  const cat = document.createElement('span');
  cat.innerHTML = category;
  cat.classList.add('category');
  cat.addEventListener('click', () => {
    window.localStorage.setItem('category', category);
    window.location.href = "tags.html";
  })
  category_container.appendChild(cat);
}

get_tag_categories();
