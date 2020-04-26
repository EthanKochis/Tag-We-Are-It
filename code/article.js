// Gets article
function get_articles(title=null) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let article = JSON.parse(this.responseText);
      display_article(article);
   }
  };
  xhttp.open("GET", `http://127.0.0.1:5000/article/${title.replace("?", "%3F")}`);
  xhttp.send();
}

function display_article(article) {
  const title = document.getElementById('article-title');
  title.innerHTML = article[0];
  const author = document.getElementById('article-author');
  author.innerHTML = article[1];
  const date = document.getElementById('article-date');
  date.innerHTML = article[2];
  const body = document.getElementById('article-body');
  body.innerHTML = article[3];
}

let title = window.localStorage.getItem('title');

get_articles(title);
