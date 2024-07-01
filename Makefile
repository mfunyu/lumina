all:
	docker-compose -f docker-compose-prod.yml build --no-cache
	docker-compose -f docker-compose-prod.yml up -d
	$(MAKE) db_upgrade

build:
	docker-compose build

run:
	docker-compose up

db_upgrade:
	docker-compose exec -T server flask db upgrade

stop:
	docker-compose down

.PHONY:
setup:
	cp .env.example .env
	cp api/.env.example api/.env
	cp front/.env.example front/.env

setup-dev: setup
	cp .github/hooks/pre-commit .git/hooks/pre-commit
