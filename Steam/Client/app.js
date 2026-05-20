
const API = "http://127.0.0.1:5000";

// =====================
// AUTH
// =====================
let currentUser = null;

async function login() {
  const username = document.getElementById("user").value;
  const password = document.getElementById("pass").value;

  try {
    const res = await fetch(`${API}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (data.coderesponse === "1") {
      currentUser = data.data;

      document.getElementById("authScreen").style.display = "none";
      document.getElementById("launcher").classList.remove("hidden");

      loadGames();
    } else {
      document.getElementById("authMsg").innerText = "❌ Login incorrecto";
    }

  } catch (err) {
    console.error(err);
    document.getElementById("authMsg").innerText = "❌ Error conexión backend";
  }
}

async function signup() {
  const username = document.getElementById("user").value;
  const password = document.getElementById("pass").value;

  try {
    const res = await fetch(`${API}/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    document.getElementById("authMsg").innerText = data.msg;

  } catch (err) {
    console.error(err);
    document.getElementById("authMsg").innerText = "❌ Error register backend";
  }
}

// =====================
// GAMES
// =====================
let games = [];
let currentGenre = "all";
let search = "";

async function loadGames() {
  const res = await fetch(`${API}/games`);
  const data = await res.json();

  games = data.data || [];
  render();
}

const container = document.getElementById("games");

function render() {

  let filtered = games;

  if (currentGenre !== "all") {
    filtered = filtered.filter(g => g.genre === currentGenre);
  }

  if (search) {
    filtered = filtered.filter(g =>
      g.title.toLowerCase().includes(search)
    );
  }

  container.innerHTML = "";

  filtered.forEach(g => {
    const div = document.createElement("div");
    div.className = "game";

    div.innerHTML = `
      <h3>${g.title}</h3>
      <p>${g.price} €</p>
    `;

    div.onclick = () => openGame(g.id, g.title);
    container.appendChild(div);
  });
}

// =====================
// SEARCH
// =====================
document.getElementById("search").addEventListener("input", e => {
  search = e.target.value.toLowerCase();
  render();
});

// =====================
// FILTERS
// =====================
document.querySelectorAll(".genre").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".genre").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    currentGenre = btn.dataset.genre;
    render();
  });
});

// =====================
// GAME SCREEN
// =====================
function openGame(id, name) {
  document.getElementById("launcher").style.display = "none";
  document.getElementById("gameScreen").style.display = "block";
  document.getElementById("title").innerText = name;

  startGame(id);
}

function back() {
  document.getElementById("launcher").style.display = "flex";
  document.getElementById("gameScreen").style.display = "none";
}

// =====================
// CANVAS
// =====================
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight - 50;
}
window.addEventListener("resize", resize);
resize();

function startGame(id) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = "white";
  ctx.font = "30px Arial";

  if (id === "snake") ctx.fillText("🐍 Snake", 100, 100);
  if (id === "pong") ctx.fillText("🧱 Pong", 100, 100);
  if (id === "flappy") ctx.fillText("🐦 Flappy", 100, 100);
  if (id === "clicker") ctx.fillText("🎯 Clicker", 100, 100);
}