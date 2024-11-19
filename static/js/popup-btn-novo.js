// Selecionar o botão "Novo" e o popup
const btnNovo = document.querySelector('#btn-novo'); // Botão que ativa o popup
const popupNovo = document.querySelector('#popup-btn-novo'); // Popup a ser exibido

// Função para alternar a visibilidade do popup
btnNovo.addEventListener('click', () => {
    // Alterna entre exibir (block) e ocultar (none) o popup
    popupNovo.style.display = popupNovo.style.display === 'none' || popupNovo.style.display === '' ? 'block' : 'none';
});

// Fechar o popup ao clicar fora dele
document.addEventListener('click', (event) => {
    // Se o clique não foi no popup nem no botão "Novo", o popup é fechado
    if (!popupNovo.contains(event.target) && event.target !== btnNovo) {
        popupNovo.style.display = 'none';
    }
});
