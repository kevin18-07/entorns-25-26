package dao

import model.Game

class GameDao {

    private val games = mutableListOf<Game>()
    private var currentId = 1

    fun getAll(): List<Game> {
        return games
    }

    fun getById(id: Int): Game? {
        return games.find { it.id == id }
    }

    fun create(game: Game): Game {
        val newGame = game.copy(id = currentId++)
        games.add(newGame)
        return newGame
    }

    fun update(id: Int, game: Game): Boolean {
        val index = games.indexOfFirst { it.id == id }
        if (index == -1) return false

        games[index] = game.copy(id = id)
        return true
    }

    fun delete(id: Int): Boolean {
        return games.removeIf { it.id == id }
    }
}