const API = "http://localhost:8080/games";

// =====================
// CARGAR TODOS
// =====================
async function loadGames() {
  const res = await fetch(API);
  const games = await res.json();

  const list = document.getElementById("gamesList");
  list.innerHTML = "";

  games.forEach(game => {
    const li = document.createElement("li");

    li.innerHTML = `
      <span>${game.name}</span>
      <div>
        <button onclick="deleteGame(${game.id})">❌</button>
      </div>
    `;

    list.appendChild(li);
  });
}

// =====================
// CREAR
// =====================
async function createGame() {
  const input = document.getElementById("name");
  const name = input.value;

  if (!name) return;

  await fetch(API, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ name })
  });

  input.value = "";
  loadGames();
}

// =====================
// BORRAR
// =====================
async function deleteGame(id) {
  await fetch(`${API}/${id}`, {
    method: "DELETE"
  });

  loadGames();
}

// cargar al inicio
loadGames();