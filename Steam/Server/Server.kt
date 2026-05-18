import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.routing.*
import io.ktor.server.response.*
import io.ktor.server.request.*
import io.ktor.serialization.kotlinx.json.*
import io.ktor.server.plugins.contentnegotiation.*
import kotlinx.serialization.Serializable

import dao.GameDao
import model.Game

val dao = GameDao()

fun main() {
    embeddedServer(Netty, port = 8080) {
        module()
    }.start(wait = true)
}

fun Application.module() {

    install(ContentNegotiation) {
        json()
    }

    routing {

        // =====================
        // GET ALL GAMES
        // =====================
        get("/games") {
            call.respond(dao.getAll())
        }

        // =====================
        // GET BY ID
        // =====================
        get("/games/{id}") {
            val id = call.parameters["id"]!!.toInt()
            val game = dao.getById(id)
            if (game != null)
                call.respond(game)
            else
                call.respond(mapOf("error" to "Game not found"))
        }

        // =====================
        // CREATE GAME
        // =====================
        post("/games") {
            val game = call.receive<Game>()
            val created = dao.create(game)
            call.respond(created)
        }

        // =====================
        // UPDATE GAME
        // =====================
        put("/games/{id}") {
            val id = call.parameters["id"]!!.toInt()
            val game = call.receive<Game>()

            val updated = dao.update(id, game)
            call.respond(mapOf("updated" to updated))
        }

        // =====================
        // DELETE GAME
        // =====================
        delete("/games/{id}") {
            val id = call.parameters["id"]!!.toInt()
            val deleted = dao.delete(id)
            call.respond(mapOf("deleted" to deleted))
        }
    }
}