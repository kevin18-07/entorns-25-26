flowchart LR

subgraph Sistema["Sistema TapatApp"]

UC1["Login (username/email + password)"]
UC2["Validar credenciales"]
UC3["Generar token"]

UC4["Consultar hijos asignados"]
UC5["Ver datos del niño"]
UC6["Ver taps del niño"]

UC7["Validar token"]
UC8["Obtener roles de usuario"]

end

Tutor(("Tutor")) --> UC1
Tutor(("Tutor")) --> UC4
Tutor(("Tutor")) --> UC5
Tutor(("Tutor")) --> UC6

Cuidador(("Cuidador")) --> UC1
Cuidador(("Cuidador")) --> UC4
Cuidador(("Cuidador")) --> UC5

UC1 --> UC2
UC2 --> UC3

UC4 --> UC7
UC5 --> UC7
UC6 --> UC7

UC4 --> UC8

UC5 --> UC6 