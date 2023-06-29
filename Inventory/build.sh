cd "$(dirname "$0")"


function doIt {
    COMPOSE_DOCKER_CLI_BUILD=0 docker compose -p test2 -f docker-compose.yml up -d --build
}
doIt
