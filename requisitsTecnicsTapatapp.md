# Requisits tecnics tapatapp

## arquitectura
[client servidor](charts/mvc-generic.mermald)
## 1. Backend (servidor i gestio de dades)
El backend sera el cor del sistema, encarregar de gestionar dades, usuaris, i la logica del sistema

### a. requisits del servidor
-   allotjament: hosting compartit
-   base de dades: mysql o mariabd
-   sistema operatiu: windows o linux
-   webservice: RESTFul libreria Python Flask

### b. Lenguatges de Programació        
Python

### c. Seguretat
-   autenticacio i autorizacio pels usuaris
-   xifratge de dades HTTPS
-   copies de seguretat automatiques

## 2. Frontend

### a. Tipus de client
-   app mobil : android
- consola python
-   Framework Multiplataforma: Flutter (apps IOS android , web, desktop)

### b. Emmagatzematge local i sincronitzacio
-   dades guardem en local: token, nickname
-   seguretat: HTTPS, autenticacio serveis per token

### c. Gestio d'accessibilitat
-   nivells A, AA, AAA d'accessibilitat

## 3. Requisits generals 

### a. gestio d'usuari i autenticacio
-   rols d'usuari: tutor i cuidador
-   Seguretat password: md5m, sha256 o sha512

### b. requisits de infraestructura
-    Xarxa: internet
-   espai d'enmagatzematge a Servidor: 1Tb
-   APIs a tercers: no en fem servir

## 4. Requisits del proces de desenvolupament
-   IDE's: VScode Python, android studio, pycharm
-   control de versions: git, github
-   metodologia de desenvolupament: SCRUM
-   testing i proves de qualitat(QA): Test i proves unitaries
