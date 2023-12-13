## Product Service

### Endpoint

| HTTP Method |           Path           | Description                  |
|-------------|:------------------------:|------------------------------|
| GET         | /products/{product_code} | Retrieves a specific product |


### Mocked Values

| Product Code     | Status Code | Delay |
|------------------|:-----------:|:-----:|
| second-breakfast |     200     | 200ms |
| lembas-bread     |     200     |  8s   |
| eowyns-soup      |     500     | 200ms |


**NOTE**: Status code and delay are hardcoded per product code to simulate faults.
