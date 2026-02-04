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

# Prototip 2

###Diagrama de classses
Fem diagrama de classes del **Server**
WebService, Dao's , ADT(Abstract data Class) User, Child, Tap ... 
**Client**
### END-Point
Definir els End pointsnecesaris per implementar el prototip 2
