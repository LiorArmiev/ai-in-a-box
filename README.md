# ai-in-a-box
# this is a demo project created for the AI in a Box webinar
# it consist of the next items:
#
# Cogntitive Services:
#   | 
#   |- LUIS - with demo some NLP examples
#   |
#   |- Text Analytics 
#   
#
# Azure:
#   |
#   |- Azure Function - with a test demo http trigger
#            The function will get the Name parameter with the query for the Text Analytics cognitive service
#            when running its checking the query against the Text Analytics local container and saves the result in the SQL Edge container
#            and print the result.
#
# Docker:
#   |
#   |- docker-compose.yml
#   ------| 
#         |-  nginx  - as a load balancer
#         |
#         |- SQLEgde - as SQL database
#         | 
#         |- 2 Luis instances
#         |
#         |- Text analytics
#
# for the project to work changes need to be done in the docker-compose.yml with new keys and urls
# in the new database you need to create under the master a table called Inventory
# craete LUIS and Text Analytics cognitive services
#
# Good lack 