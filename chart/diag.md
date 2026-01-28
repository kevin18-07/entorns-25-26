classDiagram
 
    class Usuari {
        - nom: String
        - email: String
        - contrasenya: String
        + registrar(): void
        + iniciarSessio(): void
    }


    class Client {
        + comprarEntrada(e: Entrada): void
        + consultarEntrades(): List~Entrada~
        + buscarEsdeveniments(keyword: String): List~Esdeveniment~
    }


    class Administrador {
        + crearEsdeveniment(e: Esdeveniment): void
        + modificarEsdeveniment(e: Esdeveniment): void
        + eliminarEsdeveniment(e: Esdeveniment): void
    }

    class Esdeveniment {
        - nom: String
        - descripcio: String
        - data: Date
        - ubicacio: String
        - entradesDisponibles: int
        + afegirEntrada(e: Entrada): void
        + eliminarEntrada(e: Entrada): void
        + obtenirEntradesDisponibles(): List~Entrada~
    }

    class Entrada {
        - preu: float
        - estat: String "Disponible/Venuda"
        + marcarVenuda(): void
        + mostrarInfo(): String
        + canviarEstat(estat: String): void
    }

    class Pagament {
        - import: float
        - dataPagament: Date
        - metode: String
        + processarPagament(): boolean
        + mostrarDetalls(): String
        + associarEntrada(e: Entrada): void
    }

    Usuari <|-- Client
    Usuari <|-- Administrador

    Client "1" -- "*" Entrada : compra
    Administrador "1" -- "*" Esdeveniment : gestiona
    Esdeveniment "1" -- "*" Entrada : conté
    Entrada "1" -- "1" Esdeveniment : pertany
    Pagament "1" -- "*" Entrada : cobreix