sequenceDiagram
    box rgba(173, 216, 230, 0.5) Entorno Cliente
        participant Client
    end

    box rgba(144, 238, 144, 0.3) Entorno Servidor
        participant Server
        participant BBDD
    end

    Client->>Server: Request HTTPS login (POST username/password)
    Server->>BBDD: Generate token for user and store in User table
    Server->>Client: If login OK, return HTTPS response (JSON) user info + token

    Client->>Server: Request HTTPS child data (Header: TokenUser)
    Server->>BBDD: Validate TokenUser in database
    Server->>Client: If token valid, return children info (JSON)

    Client->>Server: Request HTTPS child data (Header: TokenUserB)
    Server->>BBDD: TokenUserB does not exist in database
    Server->>Client: HTTP response: Authentication error