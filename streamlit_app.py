import streamlit as st
import json

st.title("🎉 Freundschaftsquiz spielen")

# Eingabe des Quiz-Codes
quiz_id = st.text_input("Gib den Quiz-Code ein:")

if quiz_id:
    try:
        # Lade die gespeicherte Quiz-Datei basierend auf dem Code
        with open(f"quiz_{quiz_id}.json", "r", encoding="utf-8") as f:
            quiz_data = json.load(f)

        st.success("Quiz geladen! Viel Spaß!")

        score = 0
        answers = []

        # Fragen anzeigen
        for i, q in enumerate(quiz_data):
            st.subheader(f"Frage {i+1}: {q['question']}")
            answer = st.radio("Wähle deine Antwort:", q["options"], key=f"play_q{i}")
            answers.append(answer)
            if answer == q["correct"]:
                score += 1

        # Ergebnis anzeigen
        if st.button("Quiz abschließen"):
            st.success(f"Du hast {score} von {len(quiz_data)} Fragen richtig beantwortet!")

    except FileNotFoundError:
        st.error("Quiz nicht gefunden. Bitte überprüfe den Code.")
