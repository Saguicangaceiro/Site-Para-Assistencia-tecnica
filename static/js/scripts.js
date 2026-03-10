// Função do Accordion FAQ
function toggleFaq(element) {
    const answer = element.nextElementSibling;
    const arrow = element.querySelector('.arrow');
    
    // Alterna a classe active
    answer.classList.toggle('active');
    
    // Muda o ícone
    if (answer.classList.contains('active')) {
        arrow.innerText = "-";
    } else {
        arrow.innerText = "+";
    }
}

// Botão do WhatsApp
document.getElementById('btnWhatsapp').onclick = function() {
    const telefone = "5511999999999"; // Substitua pelo seu número
    const texto = encodeURIComponent("Olá! Vi o site da GameFix e gostaria de um orçamento para o meu console.");
    window.open(`https://wa.me/${telefone}?text=${texto}`, '_blank');
};