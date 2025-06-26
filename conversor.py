# Importar as bibliotecas necessárias
import streamlit as st
import requests

# Título da página
st.title("Conversor de Moedas 💱")

# CSS bem bonito com gradiente e efeitos
st.markdown("""
<style>
    /* Fundo simples e elegante */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        min-height: 100vh;
    }
    
    /* Remove containers com fundo branco */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: transparent;
    }
    
    /* Estilo para títulos */
    h1 {
        color: #ffffff !important;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-bottom: 2rem;
    }
    
    /* Container dos inputs com fundo escuro elegante */
    .stSelectbox > div > div {
        background-color: rgba(30, 30, 60, 0.8) !important;
        border: 1px solid #6c5ce7 !important;
        border-radius: 10px !important;
    }
    
    .stNumberInput > div > div > input {
        background-color: rgba(30, 30, 60, 0.8) !important;
        border: 1px solid #6c5ce7 !important;
        border-radius: 10px !important;
        color: white !important;
    }
    
    /* Labels dos inputs */
    .stSelectbox > label, .stNumberInput > label {
        color: #ffffff !important;
        font-weight: bold;
    }
    
    /* Botões estilizados */
    .stButton > button {
        background: linear-gradient(45deg, #6c5ce7, #74b9ff) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 40px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(108, 92, 231, 0.4) !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(108, 92, 231, 0.6) !important;
        background: linear-gradient(45deg, #74b9ff, #6c5ce7) !important;
    }
    
    /* Mensagens de resultado */
    .stAlert {
        background-color: rgba(30, 30, 60, 0.9) !important;
        border: 1px solid #6c5ce7 !important;
        border-radius: 15px !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Container principal
with st.container():
    # Colunas para organizar o layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Seleção de moedas
        moeda_origem = st.selectbox(
            "Moeda de origem:",
            ["USD", "EUR", "BRL", "GBP", "JPY", "CAD", "AUD", "CHF"],
            index=0
        )
        
        valor = st.number_input(
            "Valor a converter:",
            min_value=0.01,
            value=1.00,
            step=0.01,
            format="%.2f"
        )
        
        moeda_destino = st.selectbox(
            "Moeda de destino:",
            ["USD", "EUR", "BRL", "GBP", "JPY", "CAD", "AUD", "CHF"],
            index=2
        )
        
        # Botão de conversão
        if st.button("💰 Converter"):
            try:
                # API gratuita para conversão de moedas
                url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
                response = requests.get(url)
                
                if response.status_code == 200:
                    data = response.json()
                    taxa = data['rates'][moeda_destino]
                    resultado = valor * taxa
                    
                    # Exibir resultado
                    st.success(f"✅ **{valor:.2f} {moeda_origem}** = **{resultado:.2f} {moeda_destino}**")
                    st.info(f"📊 Taxa de câmbio: 1 {moeda_origem} = {taxa:.4f} {moeda_destino}")
                else:
                    st.error("❌ Erro ao obter dados da API")
                    
            except Exception as e:
                st.error(f"❌ Erro: {str(e)}")

# Rodapé com estilo
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #ffffff; margin-top: 2rem;'>
    <p>🔗 Fonte usada: ExchangeRate-API</p>
</div>
""", unsafe_allow_html=True)