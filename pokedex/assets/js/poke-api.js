const pokeApi = {}

pokeApi.getPokemons = (offset = 0, limit = 10) => {
    const url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=10'
    
    return fetch(url) // o fetch serve para fazer a requisição a API 
        .then((response) => response.json()) /* O fetch nos retorna uma promise, essa promise é uma requisição http o que 
        demora para ser feita, o que chamamos de processamento asincrono, o metodo .then server para aguardar e receber essa resposta o response. o .catch
        serve para manipular o fracasso em caso de erro. o .finally faz algo quando a função é terminada. isso é a interface de uma promise
        parecida com uma estrutura de tratamento de erro com o try catch finally */
        .then((jsonBody) => jsonBody.results)
        .catch((error) => console.error(error))
}