# Consulta de Informações do Endereço com API

Depois de comprar um curso na Udemy sobre [REST APIs com Python e Flask](https://www.udemy.com/course/rest-apis-com-python-e-flask/), devidi estudá-lo depois de terminar alguns outros, porém, tentado e ansiso para aprender logo, decidi dar uma olhada no assunto. Acabei me deparando com [um vídeo no Youtube](https://www.youtube.com/watch?v=SKlF2PmIkrU&t=618s) e decidi botar em prática para já criar uma maturidade inicial. Eis que surge esse mini projeto.

<div align="center">
  <img width="700" alt="cabeçalho 1" src="https://user-images.githubusercontent.com/97196457/155744948-985a00bb-a721-4db3-934d-4bb218e0bd87.png">
</div>

É um projeto simples, em que o usuário digita um CEP, o programa faz a validação, consome uma API e retorna algumas informações como o endereço e a localidade/UF:

<div align="center">  
  <img width="700" alt="resultado 1" src="https://user-images.githubusercontent.com/97196457/155745294-2118d04a-a146-4d6a-b982-4b1d7c45ea24.png">
</div>

## API usada
Foi usada a API do [ViaCEP](https://viacep.com.br). Em que é um webservice gratuito e de alto desempenho para consultar Códigos de Endereçamento Postal (CEP) do Brasil. Em que apenas precisamos requisitar a url "viacep.com.br/ws/**{cep_escolhido}**/json/" com o CEP para ser consultado na área indicada.

<div align="center">  
  <img width="1796" alt="viacep 1" src="https://user-images.githubusercontent.com/97196457/155747208-65c97985-b73a-46ca-b59b-7dcfe5594cab.png">
</div>

## Outros planos e ideias
Apesar de ter feito um projeto simples, conhecer um pouco mais sobre como consumir APIs abriu bastante a minha mente no sentido das ideias e possibilidades de projeto. Um exemplo é esse projeto, que pensei em incrementar com outras duas APIs:
- 1° incremento com API: por meio das informações da API do ViaCEP, conseguir extrair dados sobre a localidade e apresentar alguns dados estatísticos por meio da API do [IBGE](https://servicodados.ibge.gov.br/api/docs).
- 2° incremento com API: com a [API do Google Maps](https://developers.google.com/maps/documentation/maps-static/overview), conseguir uma imagem do Google Maps da localidade do CEP consultado. 

<div align="center">
  <img width="300" alt="resultado 1" src="https://user-images.githubusercontent.com/97196457/155748858-a7a0bf30-48ca-4a4e-ab2e-663ed1abe2bf.png">
</div>

Fiquei muito tentado a adicionar esses recursos, porém, deixei um pouco o meu lado perfeccionista e finalizei esse mini projeto. Pode ser que futuramente eu venha melhorar mais esse projeto.

## Ferramentas utilizadas
- PyCharm (Python IDE);
- Git/GitHub.

#

<div align="center">
  <img width="300" alt="resultado 1" src="https://user-images.githubusercontent.com/97196457/155749337-8003fb3a-a183-4aef-899d-fb3f561fa765.png">
</div>

#

<a href="#top">Back to top</a>
