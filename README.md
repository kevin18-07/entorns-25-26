# Entorns de desenvolupament 25-26
Entorns de Desenvolupament 25-26

## Requisits Funcionals TapatApp

[Requisits Funcionals TapatApp](requisitsFuncionalsTapatapp.md)

## Requisits Tècnics TapatApp

[Requisits Tècnics TapatApp](requisitsTecnicsTapatapp.md)


## Configuració GitHub VsCode

Aquí configurem VSCode

# Planificació Scrum

- Iteració 1: 12/11 - 17/12 (15h) - Connexió Client Server
- Iteració 2: 12/01 - 04/02 (12h) - End Points WebService, dades Tutor i Child 
- Iteració 3: 9/02 - 04/03 (10h) - Digrames classes, Login i Seguretat
- Iteració 4: 9/03 - 8/04 (11h) - Vistes Wireframes i BBDD
- Iteració 5: 13/04 - 29/04 (9h) - Pegat i Testing

[Projecte a GiutHub](https://github.com/users/kevin18-07/projects/1/views/1?layout=board)

# Prototip 1

Connectar Client / Servidor.
Consultar dades d'usuari per nom.

[Diagrama d'arquitectura prototip 1](chart/diagrama.md)

## End-Points WebService

Definició del En-point del WebService: 

URL Server desenvolupament: http://localhost:5000/

| URL | Method | Paràmetres | Descripció | Output |
|--------------|--------------|--------------|----------|----------|
| /user   | GET    | username <String> obligatori | Retornem la informació   de    | { "code_response=1, descripcio="", name="Gustavo Lloris", username="glloris",passwoprd="12345", rol="tutor", email="glloris@xtec.cat"}   |

# Entorns de desenvolupament 25-26

## Prototip 2

### Diagrama d'arquitectura

Pujar Diagrama d'arquitectura Client Server Prototip 2

### Diagrama de classes

Fer Diagrama de classes del **Server** (Mermaid)

WebService (Controlador), Dao's , ADT(Abstract data Class) User, Child, Tap ... 

**Client**

### End-Points

Definir els EndPoints necessaris per implementar el Prototip 2

#### Servei Login
End-point:  /login    
Method: POST  
Estat: Public  
Tipus petició : application/json  
Paramètres:  
- username : (string) username o email  
- password : (string)  password  

Resposta Usuari validat Ok:  
http Response Code: 200 ok  
```
{    
    "id": 1,
    "username": "mare",
    "email": "prova@gmail.com",
    "token": "token12345",
    "idrole": "2",
    "msg": "Usuari Ok"
    "coderesponse": "1"
}
```

Resposta Usuari No validat: 
http Response Code: 400 ok
```
{
     "coderesponse": "0"
     "msg": "No validat"
}
```


#### Servei Login per Token 
End-point:  /login   
Method: POST  
Estat: Public  
Tipus petició :  application/json  
Paramètres Header: 'Authorization'   : (string) token   

Resposta Usuari validat Ok:  
http Response Code: 200 ok  
```
{
    "id": 1,
    "username": "mare",
    "email": "prova@gmail.com",
    "token": "token12345",
    "idrole": "2",
    "msg": "Usuari Ok"
    "coderesponse": "1"
}
```

Resposta Usuari No validat:   
http Response Code: 400 ok  
```
{
    "coderesponse": "0"
     "msg": "No validat"
}
```


#### Servei Child
End-point:  /child    
Method: POST  
Estat: Privat (autenticació amb Token per Header)  
Tipus petició :  application/json  
Paramètres: iduser : (int) id_user  


Resposta No Child:  
```
{ 
   "msg": "1"
    "coderesponse": "1"

  [ ]
}
```

Resposta 1 Child:  
```
{ 
   "msg": "1"
    "coderesponse": "1"

  [ {
"id": 1,
    "child_name": "Carol Child",
    "sleep_average": 8,
    "treatment_id": 1,
    "time": 6

}]
}
```

Resposta Varis Child:  
```
{ 
   "msg": "2"
    "coderesponse": "1"

  [ {
"id": 1,
    "child_name": "Carol Child",
    "sleep_average": 8,
    "treatment_id": 1,
    "time": 6

},
{
    "id": 2,
    "child_name": "Jaco Child",
    "sleep_average": 10,
    "treatment_id": 2,
    "time": 6
}
]
}
``