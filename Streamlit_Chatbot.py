#streamlit run chatbot.py

# Laden der notwendigen Bibliotheken
import streamlit as st
from transformers import pipeline
import time

# Titel der Seite festlegen
st.set_page_config(page_title="Streamlit - Chatbot")

# Auswahl des Huggingface Modells
# Modell: https://huggingface.co/deutsche-telekom/bert-multi-english-german-squad2
model_name = "deutsche-telekom/bert-multi-english-german-squad2"

# Pipeline für Antwort definieren
nlp = pipeline('question-answering', # Task festlegen
               model=model_name, # zu nutzendes Modell übergeben
               tokenizer=model_name) # Tokenizer für das Modell
#-------------------------------------------------------------------------------------------------------

# Antwort aus Frage zu einem bestimmten Text erhalten
def get_prediction(text, question, model):    
    QA_input = {'question': f'{question}', 'context':  f'{text}'} # Eingabedaten übergeben
    res = model(QA_input) # Antwort von Modell erhalten
    return res["answer"] # Zurückgeben der erhaltenen Antwort

# Chat löschen
def reset_conversation():
  st.session_state.messages = []

# Textfeld leeren
def reset_text():
    st.session_state.text = ""
    
#-------------------------------------------------------------------------------------------------------

# Überschrift der Seite
st.title('Simple Streamlit App | Q&A-Chatbot')
# Linie einziehen
st.divider()

#-------------------------------------------------------------------------------------------------------

# Übeschrift für Textfeld
st.subheader("Text to analyse")
# Textfeld anlegen
txt = st.text_area("This model is bilingual (ger/en)", # Label des Textfelds
                   placeholder="insert text..." , # Platzhalter für Text
                   help="Model: Bilingual English + German SQuAD2.0 ", # Informationen zum Modell anzeigen
                   key="text") # eindeutigen Key festlegen

# Länge des Texts anzeigen
st.write(f'{len(txt)} character')
# Knopf zum Löschen des Texts anlegen
st.button("delete text", # Text des Knopfes
          on_click=reset_text, # auszuführende Funktion bei Click
          type="primary") # Knopftyp festlegen
# Linie einziehen
st.divider()

#-------------------------------------------------------------------------------------------------------

# Überschrift für Q&A Chat
st.subheader("Q&A")
# Knopf zum Löschen des Chats
st.button('delete chat', # Text des Knopfes
          on_click=reset_conversation, # auszuführende Funktion bei Click 
          type="primary") # Knopftyp festlegen

# Versuche folgendes
try:
    # Anzeigen der Chat Historie
    for message in st.session_state.messages:
        # Für jede Nachricht Rolle und Nachricht anzeigen
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
# bei Attributerror tue folgendes
except AttributeError:
    # Initialisieren der Nachrichten Items
    st.session_state.messages = []

# Prüfen ob Eingabe im Prompt erfolgt ist 
if prompt := st.chat_input("ask a question..."):
    # User Nachricht zur Historie hinzufügen und user Avatar verwenden
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Anzeigen der Usernachricht im Chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Anzeigen der Modellantwort im Chat und ai Avatar verwenden
    with st.chat_message("ai"):
        # leeren Container als Platzhalter für Antwort initialisieren
        message_placeholder = st.empty()
        # leeren Antwortstring initialisieren
        full_response = ""
        # Antwort aus Text, Eingabe und dem Modell erzeugen
        assistant_response = get_prediction(txt, prompt, nlp)
        # Schrittweise Antwort simulieren um Modell menschlicher zu machen
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # blinkenden cursor einfügen, um Tippen zu simulieren
            message_placeholder.markdown(full_response + "▌")
        # Gesamte Antwort übergeben
        message_placeholder.markdown(full_response)
    # Modellantwort zur Historie hinzufügen und ai Avatar verwenden
    st.session_state.messages.append({"role": "ai", "content": full_response})