// Gets container that holds article divs
const article_container = document.getElementById('article-container');

// Gets articles for a specific tag or all articles
function get_articles(tag=null) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     let articles = JSON.parse(this.responseText);
     for (let article of articles) {
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
  art.innerHTML = article;
  art.classList.add('article');
  // cat.addEventListener('click', () => {
  //   window.localStorage.setItem('article', article);
  //   window.location.href = "articles.html";
  // })
  article_container.appendChild(art);
}

get_articles();
