CREATE DATABASE IF NOT EXISTS steam_clone;
USE steam_clone;

-- =========================
-- 👤 USERS
-- =========================
CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- 🎮 GAMES
-- =========================
CREATE TABLE Game (
    id VARCHAR(50) PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    price FLOAT DEFAULT 0,
    developer VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- 📚 LIBRARY (Juegos comprados)
-- =========================
CREATE TABLE Library (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    game_id VARCHAR(50) NOT NULL,
    installed BOOLEAN DEFAULT FALSE,
    play_time INT DEFAULT 0, -- minutos jugados

    FOREIGN KEY (user_id) REFERENCES User(id)
        ON DELETE CASCADE,

    FOREIGN KEY (game_id) REFERENCES Game(id)
        ON DELETE CASCADE
);

-- =========================
-- 💰 PURCHASES (compras tipo Steam)
-- =========================
CREATE TABLE Purchase (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    game_id VARCHAR(50) NOT NULL,
    price FLOAT NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (game_id) REFERENCES Game(id)
);

-- =========================
-- 👥 FRIENDS (amigos estilo Steam)
-- =========================
CREATE TABLE Friends (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    friend_id INT NOT NULL,
    status ENUM('pending', 'accepted') DEFAULT 'pending',

    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (friend_id) REFERENCES User(id)
);

-- =========================
-- ⭐ REVIEWS (reseñas de juegos)
-- =========================
CREATE TABLE Review (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    game_id VARCHAR(50) NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 10),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (game_id) REFERENCES Game(id)
);

CREATE TABLE logros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_juego INT,
    titulo VARCHAR(100),
    descripcion VARCHAR(255),
    puntos INT,
    FOREIGN KEY (id_juego) REFERENCES juegos(id) ON DELETE CASCADE
);

CREATE TABLE logros_usuarios (
    id_usuario INT,
    id_logro INT,
    fecha_desbloqueo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_usuario, id_logro),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_logro) REFERENCES logros(id)
);
