

                         CELERY WITH DJANGO TO SEND EMAIL


OVERVIEW

        This django project demonstrate how to use celry with django to send emails

SETUP

        * Install django, celery,  redis
        * Add configrations to 
                    settings.py -> celery settings, email settings 
        * Create files 
                    celery.py, __init__.py, tasks.py
        * To celery to work
                    call task function in views.py 

HOW TO RUN

        * Run django server
    
        * Run celery worker
    
            celery -A celery_project.celery worker -l info



