## User Service

### Endpoint

| HTTP Method |       Path       | Description               |
|-------------|:----------------:|---------------------------|
| GET         | /users/{user_id} | Retrieves a specific user |

### Mocked Values

| User ID      |      Status Code       | Delay |
|--------------|:----------------------:|:-----:|
| abc123       | Alternates 200 and 500 | 300ms |
| def456       |          200           | 300ms |


**NOTE**: Status code and delay are hardcoded per user id to simulate faults.
