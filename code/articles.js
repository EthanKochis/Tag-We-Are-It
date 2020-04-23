// Gets container that holds article divs
const article_container = document.getElementById('article-container');

// Gets articles for a specific tag or all articles
function get_articles(tag=null) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     let articles = JSON.parse(this.responseText);
     for (let article of articles) {
       console.log(article);
       display_article(article);
     }
   }
  };
  let url = tag ? `http://127.0.0.1:5000/articles/${tag}` : `http://127.0.0.1:5000/articles`;
  xhttp.open("GET", url);
  xhttp.send();
}


// Appending a div for each article for display on articles.html
function display_article(article) {
  const art = document.createElement('div');
  const title = document.createElement('div');
  const author = document.createElement('div');
  title.innerHTML = article[0];
  author.innerHTML = `Written by: ${article[1]}`;
  art.classList.add('article');
  art.appendChild(title);
  art.appendChild(author);
  // cat.addEventListener('click', () => {
  //   window.localStorage.setItem('article', article);
  //   window.location.href = "articles.html";
  // })
  article_container.appendChild(art);
}

let tag = window.localStorage.getItem('tag');

// Adding tag title
let title = document.getElementById('title-article');
title.innerHTML = 'all articles for tag: ' + tag;

get_articles(tag);
