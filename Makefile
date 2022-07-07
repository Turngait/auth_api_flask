start_prod:
	echo 'Prodaction mode starting'
	docker-compose -f docker-compose.prod.yaml up -d

start_dev:
	echo 'Development mode starting'
	docker-compose -f docker-compose.yaml up

backup_db:
	cp -r ./db ./db_copy

init:
	cp .env.example .env
	docker-compose -f build
