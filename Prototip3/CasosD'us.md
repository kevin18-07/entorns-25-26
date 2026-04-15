# Descripción de Caso de Uso

## [UC1]
## Login de usuario

---

## Descripción
El usuario (Tutor o Cuidador) accede al sistema TapatApp introduciendo su username o email junto con su contraseña. El sistema valida las credenciales en la base de datos y, si son correctas, genera un token de autenticación que permitirá acceder a recursos protegidos como hijos (children) y taps.

---

## Actores
- Tutor  
- Cuidador  
- Sistema (Servidor + BBDD)

---

## Precondiciones
- El usuario está registrado en el sistema.
- Existe conexión entre cliente, servidor y base de datos.
- La base de datos contiene los usuarios registrados.

---

## Postcondiciones
- Usuario autenticado correctamente.
- Token generado y asociado al usuario.
- El token queda disponible para futuras peticiones protegidas.

---

## Secuencia Normal

| # | Acción (actor) | Reacción (sistema) |
|---|----------------|-------------------|
| 1 | El usuario introduce username/email y password | El sistema recibe la petición POST /login |
| 2 | Envía credenciales al servidor | El sistema busca el usuario en la base de datos (UserDAO.login) |
| 3 | — | El sistema valida username/email y password |
| 4 | — | Si es correcto, genera un token de autenticación |
| 5 | — | El sistema devuelve HTTP 200 con datos del usuario + token |
| 6 | El usuario guarda el token | El sistema deja el usuario autenticado |

---

## Alternativas

### 2.1 Login con email
El sistema valida el email como identificador y continúa el flujo normal.

### 2.2 Login con username
El sistema valida el username como identificador y continúa el flujo normal.

---

## Excepciones

| # | Acción (actor) | Reacción (sistema) |
|---|----------------|-------------------|
| p | Usuario introduce credenciales incorrectas | El sistema devuelve HTTP 401 Unauthorized |
| q | Usuario no introduce datos | El sistema devuelve HTTP 400 Bad Request |

---

## Rendimiento
El sistema debe completar el proceso de login en un máximo de **2 segundos**.

---

## Frecuencia
Este caso de uso se ejecuta aproximadamente **50-200 veces al día** por usuario activo.

---

## Importancia
vital

---

## Urgencia
inmediatamente

---

## Comentarios
- El token se utiliza para acceder a `/child` y `/taps`.
- Se recomienda en futuras versiones el uso de hashing de contraseñas.
- El sistema permite login con username o email.