import os
import pandas as pd
import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
columns_names = ["Details","Posting Date","Description","Amount", "Type", "Balance","Check or Slip #","Desires"]
df = pd.read_csv("bank_statements.CSV",names=columns_names)
model = genai.GenerativeModel("gemini-2.0-flash")


try:
    for index, row in df.iterrows():
        if str(row.get("Details")) == "DEBIT":
            response = model.generate_content(
                "Is this a want or a need or depends for the following debit charge? Respond with only saying 'need' or 'want'.: " + str(
                    row.get("Description"))).text
            df.at[index, "Desires"] = response
except Exception as e:
    print("Quota Reached")

money = float(input("How much money do you have: "))
ques = input("What is your question: ")

print(model.generate_content(f"Based on  bank statements details {df["Details", 5]} and price {df["Amount"],5}, Can this user purchase this item given the current balance: {money}").text)







