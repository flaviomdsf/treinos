const offset = 0
const limit = 10
const url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=10'

function convertPokemonToLi(pokemon){
    return `
        <li class="pokemon">
            <span class="number">#001</span>
            <span class="name">${pokemon.name}</span>
    
            <div class="detail">
                <ol class="types">
                    <li class="type">grass</li>
                    <li class="type">poison</li>
                </ol>

                <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/1.svg" alt="${pokemon.name}">
            </div>
        </li>

    `



    /*
        <li class="pokemon ${pokemon.type}">
            <span class="number">#${pokemon.number}</span>
            <span class="name">${pokemon.name}</span>

            <div class="detail">
                <ol class="types">
                    ${pokemon.types.map((type) => `<li class="type ${type}">${type}</li>`).join('')}
                </ol>

                <img src="${pokemon.photo}"
                     alt="${pokemon.name}">
            </div>
        </li>
    */
}

const pokemonList = document.getElementById('pokemonList')
//pokemonList.innerHTML += '<li>Teste</li>'

fetch(url)
    .then((response) => response.json())
    .then((jsonBody) => jsonBody.results)
    .then((pokemons) => {
        for (let i = 0; i < pokemons.length; i++){
            const pokemon = pokemons[i];
            pokemonList.innerHTML += convertPokemonToLi(pokemon)            
        }
    })
    .catch((error) => console.log(error))


/*
fazendo o fetch declarando funciton do jeito normal
fetch(url)
    .then(function (response) {
        return response.json()
    })
    .then(function (jsonBody){
        console.log(jsonBody)
    })
    .catch(function (error){
        console.log(error)
    })
    .finally(function(){
        console.log('Requisição concluída!')
    })

*/    
//A interface de uma promise funciona como um tratamento de erro com o try, catch e finally

// posso encadear vários thens
