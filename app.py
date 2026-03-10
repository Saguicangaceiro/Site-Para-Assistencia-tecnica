from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dados da empresa para o FAQ e Rodapé
    empresa = {
        "nome": "GameFix Reparos Técnicos",
        "endereco": "Avenida dos Games, 1000, Bairro Console, São Paulo - SP",
        "email": "contato@gamefixrepairs.com",
        "whatsapp": "5511987654321",
        "horario": "Seg a Sex: 09h às 18h | Sábados: 09h às 13h"
    }

    consoles = [
        {"nome": "PlayStation 2/3", "icone": "🎮", "info": "Troca de lentes, capacitores e prevenção de luzes amarelas/vermelhas."},
        {"nome": "PlayStation 4/5", "icone": "💎", "info": "Limpeza completa, Metal Líquido (PS5), HDMI e upgrade SSD."},
        {"nome": "Xbox 360", "icone": "🟢", "info": "Prevenção de 3RL, troca de leitor e reparo de drives."},
        {"nome": "Xbox One / S / X", "icone": "🎮", "info": "Reparo de fonte interna, troca de HD por SSD e limpeza térmica."},
        {"nome": "Xbox Series S / X", "icone": "🚀", "info": "Manutenção de fluxo de ar e reparo de portas HDMI 2.1."},
        {"nome": "PC Gamer", "icone": "🖥️", "info": "Montagem, cable management e otimização de performance."}
    ]
    
    faq = [
        {"p": "Quanto tempo demora o reparo?", "r": "O prazo depende da situação do console e do tipo de defeito. Após a avaliação técnica, passamos uma estimativa precisa."},
        {"p": "Tenho garantia?", "r": "Sim! Todos os nossos reparos têm garantia para sua total segurança."},
        {"p": "Vocês buscam o console?", "r": "No momento não realizamos retirada. Mas se quiser fazer o serviço conosco, podemos combinar o envio com segurança."},
    ]
    
    return render_template('index.html', consoles=consoles, faq=faq, empresa=empresa)

if __name__ == '__main__':
    app.run(debug=True)