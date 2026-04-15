# Descripción de Caso de Uso

## [UC2]
## Ver hijos del usuario (View Children)

---

## Descripción
El usuario (Tutor o Cuidador) que ya ha iniciado sesión accede a la opción “Ver hijos” desde el menú principal de la aplicación de consola. El sistema comprueba que el usuario esté autenticado y, si es válido, recupera la lista de hijos asociados a dicho usuario mediante el DAO. Finalmente, muestra los datos de los hijos por pantalla.

---

## Actores
- Usuario (Tutor / Cuidador)
- Sistema Cliente (ViewConsole)
- DaoUserClient

---

## Precondiciones
- El usuario debe estar autenticado correctamente (login previo realizado).
- Debe existir una sesión activa (`self.user != None`).
- El usuario debe tener hijos asociados en la base de datos.

---

## Postcondiciones
- Se muestra la lista de hijos del usuario en pantalla.
- Si no hay hijos, se informa al usuario.
- El sistema no modifica datos, solo consulta información.

---

## Secuencia Normal

| # | Acción (actor) | Reacción (sistema) |
|---|----------------|-------------------|
| 1 | El usuario selecciona la opción “Ver hijos” en el menú | El sistema ejecuta `viewShowChildren()` |
| 2 | — | El sistema comprueba si el usuario está logueado (`self.user`) |
| 3 | Usuario autenticado | El sistema llama a `dao.get_children(username)` |
| 4 | — | El DAO consulta los hijos asociados al usuario |
| 5 | — | El sistema recibe la lista de hijos |
| 6 | — | El sistema muestra los hijos en pantalla con sus datos |

---

## Alternativas

### 2.1 Usuario no autenticado
El sistema detecta que no hay sesión activa y muestra el mensaje:
- “Debes estar logueado primero”
- El caso de uso finaliza.

### 2.2 Usuario sin hijos asignados
El sistema no encuentra hijos asociados y muestra:
- “No se encontraron hijos”

---

## Excepciones

| # | Acción (actor) | Reacción (sistema) |
|---|----------------|-------------------|
| p | Error en DAO o conexión | El sistema muestra mensaje de error de consulta |
| q | Datos corruptos o vacíos | El sistema muestra “No se encontraron hijos” |

---

## Rendimiento
La consulta de hijos debe realizarse en un máximo de 2 segundos.

---

## Frecuencia
Este caso de uso se ejecuta de forma media 5-20 veces por usuario activo al día.

---

## Importancia
importante

---

## Urgencia
puede esperar

---

## Comentarios
- El acceso depende de que el usuario esté autenticado previamente.
- La obtención de hijos se realiza a través de `DaoUserClient.get_children()`.
- Es una operación de solo lectura (no modifica datos).