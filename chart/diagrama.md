flowchart LR

    subgraph Bloc_Servidor [Bloc Servidor]
        WebService["webService<br/>(getUserByName)"]
        DaoServer["Dao<br/>(getUserByName)"]
        DataUsers["List Data Users"]
    end

    Vista --> DaoClient
    DaoClient -- HTTP --> WebService
    WebService --> DaoServer
    DaoServer --> DataUsers
