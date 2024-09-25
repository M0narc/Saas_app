# Saas_app
Building fundations for Software as a Service business using Django, Stripe, Neon PostgreSQL, TailwindCSS, GitHub Actions.
Railway: https://railway.app/dashboard

go to `https://saasapp-production-6fcd.up.railway.app/`
a quick guide
`https://www.codingforentrepreneurs.com/blog/deploy-django-on-railway-with-this-dockerfil`

for the .env
`https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-ke`
and creating new django secret keys, if you want to change it every month.

also for .env
`https://console.neon.tech/app/projects`
you can get the connection string there...

# dotenv
DJANGO_DEBUG= 0 o 1 # modify in railway
DJANGO_SECRET_KEY='' # line 7
DATABASE_URL="" # line 14

# Frotend
- Vendor CDN (Content delivery network for prototyping this)
- TailwindCSS
- Flowbite
- Create the staticfiles/vendors folders and put the min.css there and min.js (or run the `python manage.py vendor_static_pull` command)
- after that configure your settings.py file
- then do `python manage.py collectstatic` in the src folder
- do NOT forget to add the paths to your `local-cdn` and `staticfiles/vendor`
  to your `.gitignore` if for some reason you didn' pull it in the git clone of this repo.
- Whitenoise for content storage for prod, at least short term.

# django commands
  - Why do we use a django manage.py command and not just a python module? well, as soon as you make it a command, you have access to everything inside settings.py.

# MUST RUN
  - python manage.py vendor_static_pull
  - python manage.py collectstatic (read Frontend section)
  
# goal
- to learn how to create a reusable SaaS fundation

# to create inside the folder you are in.
- django-admin startproject cfehome.

# TODO
 - read about context processors

 - install Tailwind and Flowbite using NPM, removing the CDN imports

 - make VENDOR_STATICFILES in management a .json some other time. this is a 1 point

 - change whitenoise for Django-storage or S3  (after further research I might have to switch it to django-storage)
   Might look for D-S on dropbox since it sounds funny, no realiable, but funny.