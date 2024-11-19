// Selecionar todos os itens do menu
const menuItems = document.querySelectorAll('.item-menu');

// Função para ativar o item clicado
function selectLink() {
    // Remove a classe 'ativo' de todos os itens
    menuItems.forEach((item) => {
        item.classList.remove('ativo');
    });

    // Adiciona a classe 'ativo' ao item clicado
    this.classList.add('ativo');
}

// Adiciona o evento de clique a cada item do menu
menuItems.forEach((item) => {
    item.addEventListener('click', selectLink);
});

var btnExp = document.querySelector('#btn-exp');
var menuSide = document.querySelector('.menu-lateral')

btnExp.addEventListener('click',function(){
    menuSide.classList.toggle('expandir')
})






