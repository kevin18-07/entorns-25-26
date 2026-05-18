# Prototip4 - Servei d’Autenticació 🔐

Aquest projecte és una API REST desenvolupada amb **Flask** que proporciona un sistema complet d’autenticació d’usuaris.  
L’arquitectura segueix un model modular basat en **DAO (Data Access Object)**, serveis de negoci i rutes separades, amb l’objectiu de mantenir el codi escalable, net i fàcil de mantenir.

---

### 📌 Característiques principals

- 🔑 Autenticació d’usuaris amb usuari/email i contrasenya  
- 🧾 Generació i validació de tokens d’accés  
- 🧱 Arquitectura modular (DAO + Services + Routes)  
- 🗄️ Integració amb base de dades  
- ✅ Validació de dades amb esquemes  
- 🧪 Tests unitaris per verificar funcionalitats crítiques  
- 🔐 Gestió de variables d’entorn amb `.env`  

---

### 🧱 Estructura del Projecte

```
Prototip4
├── src
│   ├── app.py                          # Punt d’entrada de l’aplicació Flask
│   ├── config.py                       # Configuració de l’aplicació
│   ├── db.py                           # Connexió i configuració de la base de dades
│   ├── Dao
│   │   └── user_dao.py                 # Data Access Object per a la gestió d’usuaris
│   ├── modelos
│   │   └── user.py                     # Model d’usuari que representa l’entitat usuari
│   ├── servicios
│   │   └── authentication_service.py   # Servei per gestionar la lògica d’autenticació
│   ├── rutas
│   │   └── authentication.py           # Rutes d’autenticació, incloent /login
│   ├── esquemas
│   │   └── user_schema.py              # Esquema de validació i serialització de dades d’usuari
│   └── funciones
│       └── token.py                    # Funcions utilitàries per a la gestió de tokens
├── tests
│   └── test_auth.py                    # Tests unitaris de la funcionalitat d’autenticació
├── requirements.txt                    # Dependències del projecte
├── .env                                # Variables d’entorn amb informació sensible
└── README.md                           # Documentació del projecte
```

## Instruccions de configuració

1. **Clonar el repositori**:

git clone <repository-url>
cd Prototip4


2. **Crear un entorn virtual**:

python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate


3. **Instal·lar dependències**:

pip install -r requirements.txt


4. **Configurar variables d’entorn**:
Crea un fitxer `.env` al directori arrel i afegeix les credencials de la base de dades i les claus secretes.

5. **Executar l’aplicació**:

python src/app.py


## Ús

- L’API proporciona un endpoint `/login` per a l’autenticació d’usuaris.
- Envia una petició POST amb `username` (o email) i `password` al cos de la petició per autenticar usuaris.

## Tests

Executa els tests unitaris per comprovar que la funcionalitat d’autenticació funciona correctament:


python -m unittest discover -s tests


## Llicència

Aquest projecte està llicenciat sota la llicència MIT.