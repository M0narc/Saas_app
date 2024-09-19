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
- Create the staticfiles/vendors folders and put the min.css there and min.js
- after that configure your settings.py file
- then do `python manage.py collectstatic` in the src folder
- do NOT forget to add the paths to your `local-cdn` and `staticfiles/vendor`
  to your `.gitignore`

# goal
- to learn how to create a reusable SaaS fundation

# to create inside the folder you are in.
- django-admin startproject cfehome.

# TODO
 - read about context processors

 - install Tailwind and Flowbite using NPM, removing the CDN imports