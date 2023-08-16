#!/bin/bash

print_help() {
        # Help function
        echo 'Please exec script with args : '${0}' -a service_name'
        echo 'Example                      : '${0}' -a get_data -> redeploy only this get_data service'
        echo 'Deploy the full stack        : '${0}' -a all -> redeploy all services'
        exit 0
}

unset service
service_list=("db" "get_data" "myadmin")

docker_deployment_service_in_list(){
    redeploy_ok=false    
    for x in  ${service_list[@]}; do
        if [ $x = $service ]; then
            docker_deployment_one_service
            redeploy_ok=true        
        fi        
    done     

    if $redeploy_ok; then   
        echo "Done"
    else
        echo "Service $service is not in docker-compose.yml file. Available services are :"
        display_service_list        
    fi
}
display_service_list(){
    for str in ${service_list[@]}; do
        echo $str
    done
}
docker_deployment_one_service() {        
    container_name="container_"$service    
    echo "Stop container: $container_name"
    docker stop $container_name
    docker compose up --build -d $service    
    docker ps -a
}

docker_complet_deployment(){
    #sudo docker-compose build --no-cache backend && sudo docker-compose up
    docker compose down
    #docker-compose build && sudo docker-compose up
    #docker compose up --build -d
    docker compose up --build
}


while getopts "a:h" opt;do
        case "$opt" in
                h | help)
                        print_help
                        exit 0
                        ;;
                a | action)
                        service=$OPTARG
                        ;;
        esac
done
shift $((OPTIND-1))

if [ -z "${service}" ]; then
        print_help
        exit 1
fi

if [[ ${service} == "all" ]]; then
        docker_complet_deployment        
else
        docker_deployment_service_in_list 
fi
