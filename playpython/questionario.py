import pandas as pd

# Carica il file CSV
df = pd.read_csv('questionario.csv')

# Statistiche sull'età
age_stats = df['What is your age?'].describe()
print("Statistiche sull'età:")
print(age_stats)
print()

# Conteggio delle risposte per ogni nazione
country_counts = df['In which country are you based?'].value_counts()
print("Conteggio delle risposte per ogni nazione:")
print(country_counts)
print()

# Statistiche sull'esperienza giornalistica
experience_stats = df['How many years of experience in journalism do you have'].describe()
print("Statistiche sull'esperienza giornalistica:")
print(experience_stats)
print()

# Argomenti trattati dai partecipanti che lavorano in redazione
topics_worked = df['Which of the following best describes your role in the newsroom?'].value_counts()
print("Argomenti trattati dai partecipanti che lavorano in redazione:")
print(topics_worked)
print()

# Argomenti trattati dai partecipanti ancora studenti
topics_students = df['What is the discipline of your *previous* or current degree? ([see here for classification](https://en.wikipedia.org/wiki/Outline_of_academic_disciplines))'].value_counts()
print("Argomenti trattati dai partecipanti ancora studenti:")
print(topics_students)
print()

# Software utilizzati e desiderio di apprendimento
software_cols = ['Data processing with spreadsheets', 'Data Scraping', 'Using Open Data Portals', 'Data cleaning',
                 'Statistics', 'Static Data Visualization', 'Interactive Data Visualization', 'Maps',
                 'Excel or Google Sheets', 'OpenRefine', 'Flourish', 'Datawrapper', 'RawGraphs', 'Infogram',
                 'ArcGIS Online', 'Python', 'R', 'HTML & CSS', 'GitHub', 'Javascript for Data (e.g., D3js)']

software_experience = df[software_cols].mean()
software_desire = df[software_cols + ['How many hours per week could you dedicate to a learning project?']].mean()

print("Media dell'esperienza nell'uso dei software:")
print(software_experience)
print()

print("Media del desiderio di apprendimento dei software:")
print(software_desire)

