### Cleaning up docker

When we are creating and utilizing new images that means that there are alot of containers which are dangling ( not images but containers which have no associated named image since we have updated the local image with new version thus overriding the existing version / tag ) We should be able to remove these intermidate docker. Unfortunately there is no nice way 

#### Cleaning up the dangling containers 

       # Assuming all the named images have format "id:tag" 
       docker rm $(docker ps -a --format 'table {{.ID}}\t{{.Image}}' |grep -v ":" | awk '{print $1}')

Explanation 
        hello_world/ $ docker ps -a --format 'table {{.ID}}\t{{.Image}}'
        CONTAINER ID        IMAGE
        50d3380c5eb5        62d6e50f6ed1
        5f05091d68d0        sequenceiq/spark:latest
        9433dd342fc4        alpine:latest
        
####  Cleaning up dangling images
This operation will not do anything if the above operation is not carried out 

        docker images prune 
      

Please let me know if there is better way. 
