# Docker + Flask + MongoDB

Uma api simples usando Flask e MongoDB  


## Referências

Referência principal: https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html  

## Endpoints

- List Users[GET]:(https://flask-mongodb-api.herokuapp.com/users/)  
- Show User[GET]:(https://flask-mongodb-api.herokuapp.com/users/humberto)  
- Create User[POST]:(https://flask-mongodb-api.herokuapp.com/users/)  
>Request(username é único)  
```json
{
	"name": "Algum Berto",
	"username": "algumberto"
}
```  
- Update User[PUT]:(https://flask-mongodb-api.herokuapp.com/users/humberto)  
>Request  
```json
{
	"name": "Outro Berto"
}
```  
- Delete User[DELETE]:(https://flask-mongodb-api.herokuapp.com/users/humberto)  