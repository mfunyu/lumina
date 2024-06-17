build:
	docker-compose build

run:
	docker-compose up

db_upgrade:
	docker-compose exec -T server flask db upgrade

.PHONY:
setup:
	cp .github/hooks/pre-commit .git/hooks/pre-commit
	cp .env.example .env
	cp api/.env.example api/.env
	cp front/.env.example front/.env