import streamlit as st
import datetime as dt

st.set_page_config(page_title="Calculadora de Juros")

st.title("Calculdora de Juros")
hoje = dt.datetime.now()
hoje = hoje.strftime(r"%d/%m/%Y")
st.write(f'Hoje é {hoje}')


col1, col2, col3 = st.columns(3)
with col1:

    valor_original = st.number_input(label="Valor Original")
    vencimento = st.date_input("Vencimento",format="DD/MM/YYYY")
    vencimento = vencimento.strftime(r"%d/%m/%y")
    

    # Calculando diferença das datas
    dia = dt.datetime.now()
    dia_hoje = dia.strftime(r'%d/%m/%y')    
    d1 = dt.datetime.strptime(vencimento, r'%d/%m/%y')
    d2 = dt.datetime.strptime(dia_hoje, r'%d/%m/%y')
    dias = abs((d2 - d1).days)

    dias_vencidos = st.write(f'Título a {dias} dias vencidos')


    with st.form('Juros'):

        st.write('Calculando Juros')

        # Juros Mora
        opcoes = st.selectbox(label='Escolha a forma de calcular o juros mora', options=['R$','%'])  
        valor_juros = st.number_input('Valor: ')
        bttCalcular = st.form_submit_button('Calcular')  
        valor_juros_mora = 0
        if bttCalcular:
            if opcoes == 'R$':
                 valor_juros_mora = dias * valor_juros
            else:
                valor_juros_mora = ((valor_juros/100) * valor_original)* dias    
            resultado_juros_mora = st.text_input('Juros Mora: ', value= valor_juros_mora)   

        # Multa

        multa = st.number_input('Multa')
        total_juros = multa + valor_juros_mora
        st.write('Total de Juros')
        text_total_juros = st.header(total_juros)

        novo_valor_boleto = total_juros + valor_original
    st.write('Valor do boleto atualizado')
    st.title(novo_valor_boleto)

    

            







    


   
    


    










