import requests
url = "https://lewiskimaru-helloworld.hf.space/translate_detect/"
data = {
    "userinput": "Mark está de viaje de negocios en Barcelona. Hoy tuvo un día libre y salió a visitar la ciudad. Primero, caminó por La Rambla, la calle más famosa de Barcelona, llena de gente, tiendas y restaurantes. Se dirigió al Barrio Gótico, uno de los sitios más antiguos y bellos de la ciudad. En la Plaza Sant Jaume observó dos de los edificios más importantes: El Palacio de la Generalitat de Catalunya y el Ayuntamiento. Volvió a La Rambla. Mark tenía hambre y se detuvo a comer unas tapas y beber una cerveza. Continuó hasta la grande y hermosa Plaza de Catalunya. Avanzó por el Paseo de Gràcia hasta llegar a un edificios fuera de lo común Casa Batlló y luego a Casa Milà, diseños del arquitecto Antoni Gaudí. Quiso saber más sobre este famoso arquitecto y se dirigió al Park Güell, donde tomó muchas fotografías.El día se acababa pero antes de volver al hotel, Mark tomó un taxi hacia la Fuente Mágica y disfrutó de un espectáculo de agua y luces.Mark quedó sorprendido con esta gran ciudad y sintió que le faltó tiempo para conocer más lugares interesantes. Se prometió regresar para tomar unas vacaciones con su familia.",
    "target_lang": "eng_Latn",
}
response = requests.post(url, json=data)
result = response.json()
print(result)

source_language = result['source_language']
print("Source Language:", source_language)

translation = result['translated_text']
print("Translated text:", translation)

"""
url = "https://lewiskimaru-helloworld.hf.space/translate_enter/"
data = {
    "userinput": "hello world",
    "source_lang": "eng_Latn",
    "target_lang": "swh_Latn",
}
response = requests.post(url, json=data)
result = response.json()
print(result)
"""