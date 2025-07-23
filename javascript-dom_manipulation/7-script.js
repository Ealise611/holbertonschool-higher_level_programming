fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
    //result for movies from fetch
    const movies = data.results;
    //select id = list_movies
    const movielist = document.querySelector('#list_movies');
    //add movie to li
    movies.forEach(movie => {
        const item_in_list = document.createElement('li');
        item_in_list.textContent = movie.title;
        movielist.appendChild(item_in_list);
    })
})
