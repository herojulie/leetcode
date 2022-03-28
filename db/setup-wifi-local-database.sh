# Installing Postgres and starting a service so it always runs in the background
brew install postgresql
brew services start postgresql

createdb fleet_wifi_email
psql -d fleet_wifi_email -c "ALTER DATABASE fleet_wifi_email OWNER TO admin_user"
psql -d fleet_wifi_email -c "GRANT CREATE ON DATABASE fleet_wifi_email TO admin_user"

createuser wifi_email_signup_user
psql -d fleet_wifi_email -c "ALTER USER wifi_email_signup_user WITH PASSWORD 'password';"


[dev]
WIFI_EMAIL_SIGNUP_REPO_DATABASE=fleet_wifi_email_signup
WIFI_EMAIL_SIGNUP_REPO_DATABASE_ADMIN_PASSWORD=forever39Toolg
WIFI_EMAIL_SIGNUP_REPO_HOST=fleet-behavior-dev.c3abeltjlgc1.us-east-1.rds.amazonaws.com
WIFI_EMAIL_SIGNUP_REPO_USERNAME=wifi_email_signup_user
WIFI_EMAIL_SIGNUP_REPO_PASSWORD=news52tRap

[prod]
WIFI_EMAIL_SIGNUP_REPO_DATABASE=fleet_wifi_email_signup
WIFI_EMAIL_SIGNUP_REPO_DATABASE_ADMIN_PASSWORD=what95NoQuesTion
WIFI_EMAIL_SIGNUP_REPO_HOST=fleet.cnjjbvy9gths.us-east-1.rds.amazonaws.com
WIFI_EMAIL_SIGNUP_REPO_USERNAME=wifi_email_signup_user
WIFI_EMAIL_SIGNUP_REPO_PASSWORD=mean32sAlt


WIFI_EMAIL_SIGNUP_REPO_DATABASE={{ wifi_email_signup_repo_database }}
WIFI_EMAIL_SIGNUP_REPO_DATABASE_ADMIN_PASSWORD={{ wifi_email_signup_repo_admin_password }}
WIFI_EMAIL_SIGNUP_REPO_HOST={{ wifi_email_signup_repo_host }}
WIFI_EMAIL_SIGNUP_REPO_USERNAME={{ wifi_email_signup_repo_username }}
WIFI_EMAIL_SIGNUP_REPO_PASSWORD={{ wifi_email_signup_repo_password }}


ansible-vault encrypt_string --vault-id .vault.password.txt --name 'wifi_email_signup_repo_admin_password' 'forever39Toolg'

psql --host="fleet-behavior-dev.c3abeltjlgc1.us-east-1.rds.amazonaws.com" --username=streetfleet_user -d fleet_behavior_dev