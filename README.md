🍽️ SharePlate – Food Sharing Community Platform

SharePlate is a web-based community platform that connects food donors with helpers who know and support poor or hungry people nearby.
It’s built to reduce food waste, fight hunger, and create meaningful human connections ❤️

🚀 Features

👤 User Roles – Donors (share food) and Helpers (help distribute it).
🍱 Food Listings – Post details like type, quantity, and expiry.
📍 Location Sharing – Share live pickup spots for donations.
💬 In-App Messaging – Donors and helpers can chat directly.
📸 Food Photos – Add images for clarity and trust.
🔔 Smart Notifications – Stay updated on requests and chats.
📱 Responsive UI – Clean HTML + CSS design that looks great on all devices.

🛠️ Tech Stack
Layer	Technology
Backend	Django (Python)
Frontend	HTML, CSS
Database	PostgreSQL (Render Cloud DB)
Deployment	Render (Free Hosting)
📂 Project Structure
share_plate/
│── accounts/          # Authentication, user login/register
│── donations/         # Donor details and food info
│── community/         # User connections and chat
│── templates/         # HTML templates (Home, Dashboard, etc.)
│── static/            # CSS, JS, and image assets
│── share_plate/       # Django project settings

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/yourusername/shareplate.git
cd shareplate

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Database (PostgreSQL on Render)

Copy your Render PostgreSQL connection string
(Format: postgresql://username:password@host:port/databasename)

Then update settings.py:

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://username:password@host:port/databasename',
        conn_max_age=600,
        ssl_require=True
    )
}


Install helpers:

pip install dj-database-url psycopg2-binary python-decouple

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Create Admin User
python manage.py createsuperuser

7️⃣ Start the Server
python manage.py runserver

🌐 Live Demo
   
👉 [SharePlate Live](https://shareplate-new.onrender.com)   

📸 
Page	Preview

🏠 Home Page	     <img width="1876" height="914" alt="Screenshot 2025-10-22 155052" src="https://github.com/user-attachments/assets/074e5abd-8961-477b-abd0-4919b7c7eba3" />



🔐 Login Page	     <img width="1899" height="909" alt="Screenshot 2025-10-22 155134" src="https://github.com/user-attachments/assets/0d3bef20-b4da-4bc8-acc3-e108f5d8e9da" />



📊 Dashboard	     <img width="1869" height="919" alt="Screenshot 2025-10-22 160002" src="https://github.com/user-attachments/assets/8d60fe03-9a51-41c4-b413-2cec29e7c61e" />



ℹ️ About Page	     <img width="1875" height="863" alt="Screenshot 2025-10-22 155119" src="https://github.com/user-attachments/assets/1d590e63-cac1-4e15-8d15-de5ca18946eb" />


💡 How It Works

Donors post available food info.

Helpers discover posts, contact donors, and pick up food.

Chat and location sharing make coordination easy.

Together, they reduce food waste and feed those in need 💚

🤝 Contributing

Currently, this is a closed project, but you can share ideas, report bugs, or suggest improvements by opening an issue.

📜 License

This project is proprietary.
All rights reserved. Reuse or modification requires permission.

👨‍💻 Developed by Muhammed Ajmal

🔥 Built with Django, PostgreSQL, and a whole lot of heart. 🌍
