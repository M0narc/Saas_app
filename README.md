# Saas_app
Building fundations for Software as a Service business using Django, Stripe, Neon PostgreSQL, TailwindCSS, GitHub Actions.
Railway: https://railway.app/dashboard

go to `https://saasapp-production-6fcd.up.railway.app/`
a quick guide
`https://www.codingforentrepreneurs.com/blog/deploy-django-on-railway-with-this-dockerfile`

for the .env
`https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-key`
and creating new django secret keys, if you want to change it every month.

also for .env
`https://console.neon.tech/app/projects`
you can get the connection string there...

# dotenv
DJANGO_DEBUG= 0 o 1 # modify in railway
DJANGO_SECRET_KEY='' # line 7  or `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
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
- Make sure that the django-all-auth-ui is installed for it's own style

# Login
- We are using AllAuth for login, using the emails as primary(at first it will be username and email)
check the docs
`https://docs.allauth.org/en/latest/account/views.html`

- `https://github.com/danihodovic/django-allauth-ui`

# django commands
  - Why do we use a django manage.py command and not just a python module? well, as soon as you make it a command, you have access to everything inside settings.py.

# MUST RUN
  - python manage.py vendor_static_pull
  - python manage.py collectstatic (read Frontend section)
  
# goal
- to learn how to create a reusable SaaS fundation

# to create inside the folder you are in.
- django-admin startproject cfehome.

# User Email
- you used pampita email.
- you can test it with `python manage.py sendtestemail --admin`

# Implemnented AllAuth for authentication
- If you want to see all the new urls
  just turn the settings.py
  TEMPLATE section to False, navigate to some url and watch all the paths
- `https://docs.allauth.org/en/latest/`
- `https://github.com/danihodovic/django-allauth-u`

# TODO
 - read about context processors

 - install Tailwind and Flowbite using NPM, removing the CDN imports

 - make VENDOR_STATICFILES in management a .json some other time. this is a 1 point

 - change whitenoise for Django-storage or S3  (after further research I might have to switch it to django-storage)
   Might look for D-S on dropbox since it sounds funny, no realiable, but funny.

- another time we need to use our own custom domain name for gmails

- implement in the allauth/layouts base.html the navbar and footer, you can import the link from our original base
into the header and the script too, if it's not already there

- `src/templates/base/messages.html` use the messages framework from django to let the user he loged in or out
`https://docs.djangoproject.com/en/5.1/ref/contrib/messages/`

  {% include 'base/messages.html' with messages=messages %} 
  remember that piece of code.

- Read `https://docs.djangoproject.com/en/dev/topics/email/#file-backend`

- TEST WITH A NEW EMAIL AND CHECK EMAIL VERIFICATION