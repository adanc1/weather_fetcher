Prerequisites
1. Docker
2. Docker Compose
3. (Optional) Python 3.10+ for local testing

Setup Steps
1. Clone the repository
```cmd
git clone https://github.com/adanc1/weather_fetcher.git
cd weather_fetcher
```
2. Configure environment variables. You can create a token on https://openweathermap.org/
```.env
API_KEY=your_api_key_here
```
3. Run setup script
```cmd
bash bin/setup.sh
docker compose up
```
4. Access Airflow UI 
- Go to http://localhost:8080
- Username: admin
- Password: admin
