import csv 
import json
import time
from openai import OpenAI
from threading import Thread

start = time.time()
model_name = "gpt-3.5-turbo-0125"
client = OpenAI(api_key="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")

#here we do ChatGPT validation
def validateQuestion(row,question_row,question_title,correct_answer):
  #row[question_row] is pupil's input
  #validation point is written on row[question_row+1]

  # If it is blank or empty
  if not row[question_row].strip(): #not is ! in Java  
    row[question_row + 1] = '0.00 / 1' 
    return
  
  response = client.chat.completions.create(
    model=model_name,
    response_format={ "type": "json_object" },
    messages=[ #system role tells what is chatGPT's job while assistant helps providing the answer
            {"role": "system", "content": "You are a helpful assistant designed to output JSON containing a field 'output' with a true or false value. If answer is satisfied the output will be true."},
            {"role": "assistant", "content": f"Odgovoriti sa 'true' ili 'false'. Da li je odgovor na sledeće pitanje logički ispravan?Pitanje glasi: '{question_title}'. Tačan odgovor je: {correct_answer}."},
            {"role": "user", "content": row[question_row]}
    ]
  )
  json_string=response.choices[0].message.content #we read ChatGPT response in JSON format. 
  data = json.loads(json_string) #parse the JSON string
  output_value = data['output'] #we read the value of the 'output' field
  row[question_row + 1] = '1.00 / 1' if output_value == True else '0.00 / 1'  #we calculate the point 

with open('test.csv', mode = 'r', encoding = 'utf-8', newline='') as csv_file:
  reader = csv.reader(csv_file) 
  rows = list(reader)
  #first, we gather titles of questions which are for free input
  question_titles = [
    rows[0][23], rows[0][46], rows[0][49],
    rows[0][62], rows[0][65], rows[0][68],
    rows[0][71], rows[0][74], rows[0][120]
  ]

  #for each pupil we do validation. We walide all his answers in a thread.
  for line_count, row in enumerate(rows[1:], start=1):
    threads = [
      Thread(target = validateQuestion, args=(row,23,question_titles[0],'Predstavlja dan nezavisnosti')),
      Thread(target = validateQuestion, args=(row,46,question_titles[1],'Voda, Plodno zemljište, Odbrambena pozicija, Uzvišenje, Brdo')),
      Thread(target = validateQuestion, args=(row,49,question_titles[2],'U srednjem vijeku naselja su se pravila na uzvišenjima zbog odbrane od neprijatelja a voda je bila neophodna')),
      Thread(target = validateQuestion, args=(row,62,question_titles[3],'Svaki odgovor koji sadrži broj 1903')),
      Thread(target = validateQuestion, args=(row,65,question_titles[4],'3 decenije 5 godina')),
      Thread(target = validateQuestion, args=(row,68,question_titles[5],'1 vijek, 2 decenije,7 godina')),
      Thread(target = validateQuestion, args=(row,71,question_titles[6],'Prva štampana ćirilična knjiga na Balkanu')),
      Thread(target = validateQuestion, args=(row,74,question_titles[7],'Nedostatak municije municija')),
      Thread(target = validateQuestion, args=(row,120,question_titles[8],'Fotografija iz porodičnog abuma, kućni aparati koje je prabaka koristila, pisma ili dokumenta prabake'))
    ]

    # Start all threads.
    for t in threads:
      t.start()

    # Wait for all threads to finish.
    for t in threads:
      t.join()
    
# Write the modified data back to the CSV file
with open('test.csv', 'w', encoding = 'utf-8', newline='') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerows(rows)

end = time.time()
print(f'ChatGPT validations finished in: {round(end - start,2)} seconds! File contained {line_count} responses.')