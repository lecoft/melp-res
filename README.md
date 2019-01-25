# Melp Restaurants REST API

REST API with all the data inside the csv Restaurants file.

## API Usage

For the restaurants list
```
https://melp-res-eugenio-andreu.herokuapp.com/api/v1/restaurants/
```

For a specific restaurant
```
https://melp-res-eugenio-andreu.herokuapp.com/api/v1/restaurants/{id}
```

## Statics EndPoint

This endpoint, takes the parameters: latitude, longitude and radius.
```
https://melp-res-eugenio-andreu.herokuapp.com/api/v1/restaurants/statics?latitude=x&longitude=y&radius=z
```

Returns a JSON with the following data:

* **count:** - *Count of restaurants that fall inside the circle with center [x,y] and radius z.*
* **avg:** - *Average rating of restaurant inside the circle.*
* **std:** - *Standard derivation of rating of restaurants inside the circle.*

## Postman Collection example

```
https://www.getpostman.com/collections/c02a7785aa954915d9f4
```

## Author

**Eugenio Andreu**