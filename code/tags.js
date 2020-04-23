// Gets container that holds tag divs
const tag_container = document.getElementById('tag-container');

// Gets tags for a specific category or all tags
function get_tags(category=null) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     let tags = JSON.parse(this.responseText);
     for (let tag of tags) {
       display_tag(tag);
     }
   }
  };
  let url = category ? `http://127.0.0.1:5000/tags/${category}` : `http://127.0.0.1:5000/tags`;
  xhttp.open("GET", url);
  xhttp.send();
}

// Appending a div for each tag for display on index.html
function display_tag(tag) {
  const t = document.createElement('span');
  t.innerHTML = tag;
  t.classList.add('tag');
  t.addEventListener('click', () => {
    window.localStorage.setItem('tag', tag);
    window.location.href = "articles.html";
  })
  tag_container.appendChild(t);
}

let category = window.localStorage.getItem('category');

// Adding category title
let title = document.getElementById('title-tag');
title.innerHTML = 'all tags for: ' + category;

get_tags(category);
