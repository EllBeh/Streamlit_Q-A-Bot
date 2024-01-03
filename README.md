# Q&A-Bot mit Streamlit
Dieses kleine Code-Snippet demonstriert wie mit wenig Code und einfachen Mitteln bereits ein akzeptabler Q&A-Bot aufgebaut werden kann. Hierfür wird das Streamlit Modul verwendet, womit eine simple grafische Oberfläche erzeugt wird. Das Modell des Q&A-Bots ist das [Bilingual English + German SQuAD2]([https://www.google.com](https://huggingface.co/deutsche-telekom/bert-multi-english-german-squad2)https://huggingface.co/deutsche-telekom/bert-multi-english-german-squad2 "Hugging Face") der deutschen Telekom.

Die Funktionsweise des Q&A-Vorgangs ist hierbei denkbar einfach. Beginnend mit der Übergabe eines Texts an das Modell, können anschließend Fragen über den Text gestellt werden. Über den Delete-Button ist es möglich den Text zu löschen und einen neuen Text für das Q&A zu übergeben.  

___
## Schaltplan
![Screenshot](https://github.com/EllBeh/Streamlit_Q-A-Bot/blob/main/Images/screenshot.png)
