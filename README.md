WebShacs Tweet

A Django-based, Twitter-like web app built to demonstrate authentication, posting tweets, and basic admin controls. This repository is part of my hiring portfolio — you can run it locally to review functionality.

🔎 Project summary

Django web app for posting and viewing short messages (tweets).

Includes user registration, login, tweet creation, and an admin interface for managing users & tweets.

Intended for recruiter/demo use — not currently hosted.

📁 Repository layout (actual)
webshacs-tweet/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── webtweetapp/           # main Django app (templates, views, models)
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   └── ...
├── project_name/          # Django settings package
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── screenshots/
│   ├── logiin register.png
│   ├── home.png
│   ├── reg.png
│   ├── controlled.png
│   └── admin.png
└── ...                    # other apps or config


Update the folder names above if your project uses different app/package names.

🖼 Screenshots

Login page
![Login Page](
<img width="1897" height="1022" alt="logiin register" src="https://github.com/user-attachments/assets/6a3eada9-426c-4e03-8f57-253b97c785e5" />

Home feed (tweets)

<img width="1902" height="1070" alt="home" src="https://github.com/user-attachments/assets/029e01b0-b405-4dac-ae73-ac1995bcf96e" />

Register page
<img width="1903" height="963" alt="reg" src="https://github.com/user-attachments/assets/6c2a6a5f-511c-4aea-af5e-b8b3cc0be676" />


Admin — Users list

<img width="1440" height="960" alt="admin" src="https://github.com/user-attachments/assets/14cb104f-6a11-4520-91cd-dbc7804c78d5" />

Admin — Dashboard / Recent actions

<img width="1913" height="967" alt="controlled" src="https://github.com/user-attachments/assets/ca6804f3-eef6-489d-9f33-ea8fb14ad18e" />

⚙️ Quick local setup (recommended for reviewers)

These commands assume you have Python 3.10+ and Git installed.

Clone the repo:

git clone https://github.com/your-username/webshacs-tweet.git
cd webshacs-tweet


Create and activate a virtual environment:

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Create .env from example and set necessary variables:

cp .env.example .env
# Edit .env and set SECRET_KEY, DEBUG=True (for local review), and DB settings if needed


Minimum .env keys:

SECRET_KEY=some-secret-key-for-local
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3   # recommended for reviewers


Apply migrations:

python manage.py migrate


(Optional) Create a superuser for admin:

python manage.py createsuperuser


Collect static files (if needed):

python manage.py collectstatic --noinput


Run the development server:

python manage.py runserver


Open http://127.0.0.1:8000/webtweetapp/ (or root depending on your URLs) to view the app.
