##
An exercise to create an e-commerce website using microservice architecture. A user can place an order calling the `/orders` endpoint with a user_id_ and product_code. The request will call the user and product services respectively and will publish a message to a RabbitMQ broker while also storing the order in a MySQL database. The Wiremock setup of the product and user services sets up potential erratic behavior of the APIs. 


## Prerequisites

- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)


## Use Cases
Both [Product Service](docs/product-service.md) and [User Service](docs/user-service.md) have some faulty behavior for specific products and users. When testing the use cases below, be aware of them.
