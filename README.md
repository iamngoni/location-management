# Econet Technical Assessment

- REST API for  a small location management service

## Google Drive Recording Link
[Click Here](https://drive.google.com/file/d/10Q-jwoRTYQODGmyPqs2iwQF9JW5WlLi3/view?usp=sharing)

## Relevant Endpoints
- [Create Shop Under Area](http://127.0.0.1:8000/api/1.0/areas/<area_id>/shops)
```bash
curl --location 'http://127.0.0.1:8000/api/1.0/areas/area_jPxrCuJsiXzGGM0m8WqrV3k5yRwIp0/shops' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Rimbi"
}'
```
- [Retrieve All Shops Under Area](http://127.0.0.1:8000/api/1.0/areas/<area_id>/shops)
```bash
curl --location 'http://127.0.0.1:8000/api/1.0/areas/area_jPxrCuJsiXzGGM0m8WqrV3k5yRwIp0/shops'
```

### Extra Endpoints
- Create Area
- List Areas
- View Area By ID
- Update Area
- Create Shop
- List Shops
- View Shop By ID
- Update Shop

> Endpoints that return any list of items is paginated

## ER Diagram

![ER Diagram](./ER.png)

## Deployment For Testing
### Manual
Create a virtual environment for the service

### 
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations && python manage.py migrate
python manage.py runserver 8000
```

### Docker
Use the docker-compose file to build the image

```bash
docker-compose up -d
```

## Running Tests
```bash
python manage.py test
```
