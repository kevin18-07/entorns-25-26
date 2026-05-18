# Prototip4 - Servei d’Autenticació 🔐

Aquest projecte és una API REST desenvolupada amb **Flask** que proporciona un sistema complet d’autenticació d’usuaris.  
L’arquitectura segueix un model modular basat en **DAO (Data Access Object)**, serveis de negoci i rutes separades, amb l’objectiu de mantenir el codi escalable, net i fàcil de mantenir.

---

# 📌 Característiques principals

- 🔑 Autenticació d’usuaris amb usuari/email i contrasenya
- 🧾 Generació i validació de tokens d’accés
- 🧱 Arquitectura modular (DAO + Services + Routes)
- 🗄️ Integració amb base de dades
- ✅ Validació de dades amb esquemes
- 🧪 Tests unitaris per verificar funcionalitats crítiques
- 🔐 Gestió de variables d’entorn amb `.env`

---

# 🧱 Estructura del Projecte


Prototip4
├── src
│ ├── app.py # Punt d’entrada de l’aplicació Flask
│ ├── config.py # Configuració de l’aplicació
│ ├── db.py # Connexió i configuració de la base de dades
│ ├── Dao
│ │ └── user_dao.py # Data Access Object per a la gestió d’usuaris
│ ├── modelos
│ │ └── user.py # Model d’usuari que representa l’entitat usuari
│ ├── servicios
│ │ └── authentication_service.py # Servei per gestionar la lògica d’autenticació
│ ├── rutas
│ │ └── authentication.py # Rutes d’autenticació, incloent /login
│ ├── esquemas
│ │ └── user_schema.py # Esquema de validació i serialització de dades d’usuari
│ └── funciones
│ └── token.py # Funcions utilitàries per a la gestió de tokens
├── tests
│ └── test_auth.py # Tests unitaris de la funcionalitat d’autenticació
├── requirements.txt # Dependències del projecte
├── .env # Variables d’entorn amb informació sensible
└── README.md # Documentació del projecte


---

# ⚙️ Instal·lació i configuració

## 1. Clonar el repositori

```bash
git clone <repository-url>
cd Prototip4
2. Crear un entorn virtual

És recomanable utilitzar un entorn virtual per evitar conflictes de dependències:

python -m venv venv
Activar-lo:
Linux / MacOS
source venv/bin/activate
Windows
venv\Scripts\activate
3. Instal·lar dependències
pip install -r requirements.txt
4. Configurar variables d’entorn

Crea un fitxer .env a l’arrel del projecte:

SECRET_KEY=la_teva_clau_secreta
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=password
DB_NAME=prototip4
JWT_SECRET=una_clau_per_tokens

⚠️ No pugis mai aquest fitxer a repositoris públics.

5. Executar l’aplicació
python src/app.py

L’aplicació s’executarà habitualment a:

http://127.0.0.1:5000
🚀 Ús de l’API
🔐 Endpoint de login
POST /login
Body (JSON)
{
  "username": "usuari@example.com",
  "password": "123456"
}
Resposta correcta
{
  "message": "Login correcte",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6..."
}
Resposta d’error
{
  "error": "Credencials incorrectes"
}
🔐 Seguretat
Hashing de contrasenyes
Tokens JWT per autenticació
Variables sensibles en .env
Separació de capes per evitar exposició de dades
🧪 Tests
Executar tests
python -m unittest discover -s tests
Cobertura de tests
Login correcte
Login incorrecte
Validació de token
📦 Dependències
Flask
PyJWT
python-dotenv
bcrypt (si s’utilitza hashing)
📁 Bones pràctiques
Separació per capes (DAO / Services / Routes)
Codi modular
Validació d’entrada
Configuració externa amb .env
Tests automatitzats
📄 Llicència

Aquest projecte està sota llicència MIT.