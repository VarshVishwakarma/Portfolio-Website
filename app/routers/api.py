import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import APIRouter, Form
from pydantic import BaseModel
import random
import time

router = APIRouter()

# --- AI LOGIC (Keep existing) ---
class AIRequest(BaseModel):
    text: str

@router.post("/nlp")
async def nlp_engine(payload: AIRequest):
    time.sleep(1) 
    text = payload.text.lower()
    sentiment = "NEUTRAL"
    if any(x in text for x in ["good", "great", "amazing", "love"]): sentiment = "POSITIVE"
    if any(x in text for x in ["bad", "hate", "error", "slow"]): sentiment = "NEGATIVE"

    return {
        "status": "200 OK",
        "module": "Transformer_v4.2",
        "analysis": {
            "sentiment": sentiment,
            "confidence": random.uniform(0.85, 0.99)
        }
    }

# --- EMAIL LOGIC (Updated) ---
@router.post("/contact")
async def contact_form(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    
    # ---------------- CONFIGURATION ----------------
    MY_EMAIL = "varshv2007@gmail.com"
    MY_APP_PASSWORD = "xmyo lusj qddw hczes"  # <--- PASTE HERE
    # -----------------------------------------------

    try:
        # 1. Create the email structure
        msg = MIMEMultipart()
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL  # Send to yourself
        msg['Subject'] = f"🚀 New Portfolio Connection: {name}"
        
        # 2. Email Body
        body = f"""
        INCOMING TRANSMISSION
        --------------------------------
        NAME:    {name}
        EMAIL:   {email}
        MESSAGE: 
        {message}
        --------------------------------
        """
        msg.attach(MIMEText(body, 'plain'))

        # 3. Login and Send via Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MY_EMAIL, MY_APP_PASSWORD)
        server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {MY_EMAIL}")
        return {"status": "Transmission Successful. Uplink Established."}

    except Exception as e:
        print(f"Error sending email: {e}")
        return {"status": "Transmission Failed. Signal Lost."}