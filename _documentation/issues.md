## django_admin_log error

Sometimes when starting out you might find an error:

The above exception (insert or update on table "django_admin_log" violates foreign key constraint "django_admin_log_user_id_c564eba6_fk_auth_user_id" DETAIL: Key (user_id)=(1) is not present in table "auth_user". ) was the direct cause of the following exception.

Steps:

1. drop the table from postgres

DROP table django_admin_log;

2. Then recreate table using these command.

python manage.py migrate admin zero --fake

python manage.py migrate

The admin table will now be reverted back to it's initial state.
