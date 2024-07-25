telugu_to_english = {
    "హలో": "Hello",
    "స్వాగతం": "Welcome",
    "బియ్యం": "Rice",
    "పల్లీ": "Leaf",
    "పెద్ద": "Big",
    "చిన్న": "Small",
    "నలుపు": "Black",
    "తెల్ల": "White",
    "పండుగ": "Festival",
    "పుస్తకం": "Book",
    "కుటుంబం": "Family",
    "పాఠశాల": "School",
    "గాడి": "Car",
    "సముద్రం": "Sea",
    "గుడి": "House",
    "ఆహారం": "Food",
    "ప్రాణం": "Life",
    "సౌందర్యం": "Beauty",
    "ఆరోగ్యం": "Health",
    "అతడు": "He",
    "అవాడు": "She",
    "అది": "It",
    "నేను": "I",
    "అది": "It",
    "జనం": "People",
    "జన్మదినం": "Birthday",
    "పశువు": "Animal",
    "ఆడి": "Dog",
    "పిల్లి": "Cat",
    "గుర్రం": "Horse",
    "పక్షి": "Bird",
    "ఆడి": "Cow",
    "హలోమీరుఎలా": "Hello, meeru ela unnaru?",
    "నేనుసంతోషంగాఉన్నాను": "i am happy",
    "సంతోషంగా": "happy",
    "పక్షి": "Bird",
    "ఆడి": "Cow",
    "వస్తున్నాను": "Coming",
    "పరిపక్కంగా": "Very",
    "ఉన్నాడు": "Is",
    "మారుతి": "Maruti",
    "విద్యార్థి": "Student",
    "రోజులు": "Every day",
    "పని": "Working",
    "అందరికి": "Everyone",
    "ఇష్టమైన": "Favorite",
    "చదువుతుంది": "Reads",
    "నేను ఇంటికి వస్తున్నాను": "I am coming home",
    "అతను చాలా పరిపక్కంగా ఉన్నాడు": "He is very kind",
     "విద్య": "Knowledge",
    "విద్యార్థి": "Student",
    "గురువు": "Teacher",
    "కళ": "Art",
    "సాహిత్యం": "Literature",
    "సినిమా": "Movie",
    "సంగీతం": "Music",
    "నాట్యం": "Dance",
    "రంగం": "Stage",
    "దేశం": "Country",
    "రాజ్యం": "State",
    "ప్రాంతం": "Region",
    "నగరం": "City",
    "గ్రామం": "Village",
    "జలం": "Water",
    "అగ్ని": "Fire",
    "వాయు": "Air",
    "భూమి": "Earth",
    "దీపం": "Lamp",
    "పర్వం": "Festival",
    "ఉద్యానం": "Garden",
    "విమానం": "Aeroplane",
    "రథం": "Chariot",
    "బ్యాగ్": "Bag",
    "ఆరోగ్యం": "Health",
    "మంచి": "Good",
    "మంచి ఉత్తమ": "Excellent",
    "మోసం": "Lie",
    "దుర్బుద్ధి": "Stupidity",
    "అవగాహన": "Understanding",
    "ప్రేమ": "Love",
    "అంగస్థులు": "Parts of body",
    "విషయం": "Subject",
    "బుధ్ధి": "Intelligence",
    "పండితుడు": "Scholar",
    "స్థాయి": "Permanent",
    "అస్థాయి": "Temporary",
    "క్షమాపణ": "Apology",
    "గుర్తించడం": "Remembering",
    "గుర్తు": "Mark",
    "మోసం": "Lie",
    "అసలు": "Truth",
    "దోషం": "Mistake",
    "ఉత్తమ": "Best",
    "అంతమని": "Endless",
    "పరిశుద్ధం": "Pure",
    "బహుశాఖ": "Branch",
    "రోజువారికి": "Daily",
    "ప్రతి": "Every",
    "సన్నిహిత": "Near",
    "దూరం": "Far",
    "సాక్షి": "Witness",
    "దోషము": "Fault",
    "పడుపు": "Fall",
    "పలువు": "Defeat",
    "గెలుపు": "Victory",
    "అక్రమ": "Unlawful",
    "విధిగా": "By chance",
    "కదిలిపోవడం": "Disappear",
    "ఆయినా": "But",

}

def translate_telugu_to_english(text):
    words = text.split()
    translated_words = [telugu_to_english.get(word, word) for word in words]
    return ' '.join(translated_words)

telugu_text = input("Enter the Telugu text: ")


english_translation = translate_telugu_to_english(telugu_text)
print("English Translation:", english_translation)