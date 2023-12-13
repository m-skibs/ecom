## Order Service


    | HTTP Method |  Path   | Description         |
    |:-----------:|:-------:|---------------------|
    |    POST     | /orders | Creates a new order |

    *Body Schema*
    ```json
    {
        "user_id": "STRING",
        "product_code": "STRING"
    }
    ```

    *Order Schema*

    | Attribute         | Type     | Description                                     |
    |-------------------|----------|-------------------------------------------------|
    | id                | STRING   | Order identifier                                |
    | user_id           | STRING   | User Identifier                                 |
    | product_code      | STRING   | Product Identifier                              |
    | customer_fullname | STRING   | A combination of the user's first and last name |
    | product_name      | STRING   | Name of the product                             |
    | total_amount      | FLOAT    | Price of the product                            |
    | created_at        | DATETIME | Date and time when the order was created        |


    | Exchange |  Routing Key  |
    |:--------:|:-------------:|
    |  orders  | created_order |

    *Message Schema*
    ```json
    {
        "producer": "STRING",
        "sent_at": "DATETIME",
        "type": "STRING",
        "payload": {
            "order": {
                "order_id": "STRING",
                "customer_fullname": "STRING",
                "product_name": "STRING",
                "total_amount": "FLOAT",
                "created_at": "DATETIME"
            }
        }
    }
    ```

