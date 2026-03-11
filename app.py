from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    empresa = {
        "nome": "GameFix Reparos Técnicos",
        "endereco": "Avenida dos Games, 1000, Bairro Console, São Paulo - SP",
        "email": "contato@gamefixrepairs.com",
        "whatsapp": "5511987654321",
        "horario": "Seg a Sex: 09h às 18h | Sábados: 09h às 13h"
    }

    consoles = [
        {
            "nome": "PlayStation 2/3", 
            "imagem": "images/ps.png", 
            "info": "Troca de leitores, rebaling, prevenção das luzes amarelas/vermelhas, manutenção preveniva do aparelho e etc."
        },
        {
            "nome": "PlayStation 4/5", 
            "imagem": "images/Ps5.png", 
            "info": "Manutenção corretiva, rebaling, Metal Líquido (PS5), HDMI e upgrade SSD e etc."
        },
        {
            "nome": "Xbox 360", 
            "imagem": "images/xbox.png", 
            "info": "Prevenção de 3RL, troca de leitor e HD, reparo de drives e coreção da luz vermelha e etc."
        },
        {
            "nome": "Xbox One / S ", 
            "imagem": "images/ONE.png", 
            "info": "Reparo de fonte interna, troca de HD por SSD e limpeza térmica, manutenção preventiva e etc."
        },
        {
            "nome": "Xbox Series S / X", 
            "imagem": "images/x.png", 
            "info": "Manutenção de fluxo de ar e reparo de portas HDMI 2.1 e etc."
        },
        {
            "nome": "PC Gamer", 
            "imagem": "images/PC.png", 
            "info": "Montagem, cable management (organização dos cabos) e otimização de performance, troca de memória, upgrade de SSD e etc."
        },
    ]
    
    faq = [
        {"p": "Quanto tempo demora o reparo?", "r": "O prazo depende da situação do console e do tipo de defeito. Após a avaliação técnica, passamos uma estimativa precisa."},
        {"p": "Tenho garantia?", "r": "Sim! Todos os nossos reparos têm garantia para sua total segurança."},
        {"p": "Vocês buscam o console?", "r": "No momento não realizamos retirada. Mas se quiser fazer o serviço conosco, podemos combinar o envio com segurança."},
        {
            "p": "Sobre a GameFix (Endereço e Contatos)", 
            "r": f"📍 {empresa['endereco']} | 📧 {empresa['email']} | 🕒 {empresa['horario']}"
        }
    ]
    
    return render_template('index.html', consoles=consoles, faq=faq, empresa=empresa)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')