fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(response => response.json())
.then(data => {
    const characterName = data.name;
    //select id = character
    const id_character = document.querySelector('#character');
    id_character.textContent = characterName;
})
