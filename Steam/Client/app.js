const API = "http://127.0.0.1:5000";

// =====================
// CREATE GAME BUTTON CONTROL
// =====================

function hideCreateButton() {
  const btn = document.getElementById("createGameBtn");
  if (btn) btn.style.display = "none";
}

function showCreateButton() {
  const btn = document.getElementById("createGameBtn");
  if (btn) btn.style.display = "block";
}

window.onload = () => {
  hideCreateButton();
};

// =====================
// AUTH
// =====================
let currentUser = null;

async function login() {
  const username = document.getElementById("user").value;
  const password = document.getElementById("pass").value;

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
    document.getElementById("createGameBtn").style.display = "block";

    render();

    // 🔥 MOSTRAR BOTÓN CREAR JUEGO
    showCreateButton();

  } else {
    document.getElementById("authMsg").innerText = "❌ Login incorrecto";
  }
}

async function signup() {
  const username = document.getElementById("user").value;
  const password = document.getElementById("pass").value;

  const res = await fetch(`${API}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const data = await res.json();
  document.getElementById("authMsg").innerText = data.msg;
}

// =====================
// GAMES
// =====================
const games = [
  { id: "snake", title: "🐍 Snake", genre: "clasicos", description: "Come sin chocarte." },
  { id: "pong", title: "🧱 Pong", genre: "clasicos", description: "Tenis retro." },
  { id: "flappy", title: "🐦 Flappy Bird", genre: "arcade", description: "Evita tubos." },
  { id: "clicker", title: "🎯 Clicker", genre: "arcade", description: "Haz clicks." },
  { id: "tetris", title: "🟪 Tetris", genre: "clasicos", description: "Encaja bloques." }
];

let selectedGame = null;
let currentGenre = "all";
let search = "";

const container = document.getElementById("games");

// =====================
// RENDER STORE
// =====================
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
      <p>${g.genre}</p>
    `;

    div.onclick = () => showGame(g);

    container.appendChild(div);
  });
}

// =====================
// GAME DETAIL
// =====================
function showGame(game) {
  selectedGame = game;

  container.innerHTML = `
    <div class="game-detail">
      <h2>${game.title}</h2>
      <p>${game.description}</p>

      <button onclick="playGame()">▶ Jugar</button>
      <button onclick="render()">⬅ Volver</button>
    </div>
  `;
}

function playGame() {
  document.getElementById("launcher").style.display = "none";
  document.getElementById("gameScreen").style.display = "block";

  document.getElementById("title").innerText = selectedGame.title;

  startGame(selectedGame.id);
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

// =====================
// LOOP CONTROL
// =====================
let loopId = null;

// =====================
// GAME STATE
// =====================

// Snake
let snake, dir, food, tick;

// Pong
let ball, p1, p2, scoreL, scoreR;

// Flappy
let birdY, birdV, pipes;

// Clicker
let clicks;

// Tetris
let tY;

// =====================
// START GAME
// =====================
function startGame(id) {

  cancelAnimationFrame(loopId);

  snake = [{ x: 200, y: 200 }];
  dir = "right";
  food = random();
  tick = 0;

  ball = { x: 300, y: 200, vx: 5, vy: 3 };
  p1 = 200;
  p2 = 200;
  scoreL = 0;
  scoreR = 0;

  birdY = 200;
  birdV = 0;
  pipes = [{ x: 600, h: 150 }];

  clicks = 0;
  tY = 0;

  document.onkeydown = (e) => {

    if (id === "snake") {
      if (e.key === "ArrowUp") dir = "up";
      if (e.key === "ArrowDown") dir = "down";
      if (e.key === "ArrowLeft") dir = "left";
      if (e.key === "ArrowRight") dir = "right";
    }

    if (e.key === "w") p1 -= 20;
    if (e.key === "s") p1 += 20;
    if (e.key === "ArrowUp") p2 -= 20;
    if (e.key === "ArrowDown") p2 += 20;

    if (id === "flappy") birdV = -8;

    if (id === "clicker") clicks++;
  };

  canvas.onclick = () => {
    if (id === "clicker") clicks++;
  };

  loop(id);
}

// =====================
// LOOP
// =====================
function loop(id) {

  loopId = requestAnimationFrame(() => loop(id));

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  if (id === "snake") {

    tick++;

    if (tick % 6 === 0) {

      let head = { ...snake[0] };

      if (dir === "right") head.x += 10;
      if (dir === "left") head.x -= 10;
      if (dir === "up") head.y -= 10;
      if (dir === "down") head.y += 10;

      if (
        head.x < 0 || head.x > canvas.width ||
        head.y < 0 || head.y > canvas.height
      ) {
        alert("💀 GAME OVER");
        back();
        return;
      }

      snake.unshift(head);

      if (head.x === food.x && head.y === food.y) {
        food = random();
      } else {
        snake.pop();
      }
    }

    ctx.fillStyle = "lime";
    snake.forEach(s => ctx.fillRect(s.x, s.y, 10, 10));

    ctx.fillStyle = "red";
    ctx.fillRect(food.x, food.y, 10, 10);
  }

  if (id === "pong") {

    ball.x += ball.vx;
    ball.y += ball.vy;

    if (ball.y < 0 || ball.y > canvas.height) ball.vy *= -1;

    if (ball.x < 20 && ball.y > p1 && ball.y < p1 + 100) ball.vx *= -1;
    if (ball.x > canvas.width - 20 && ball.y > p2 && ball.y < p2 + 100) ball.vx *= -1;

    if (ball.x < 0) {
      scoreR++;
      resetBall();
    }

    if (ball.x > canvas.width) {
      scoreL++;
      resetBall();
    }

    ctx.fillStyle = "white";
    ctx.fillRect(10, p1, 10, 100);
    ctx.fillRect(canvas.width - 20, p2, 10, 100);
    ctx.fillRect(ball.x, ball.y, 10, 10);

    ctx.fillText(scoreL + " - " + scoreR, canvas.width / 2, 50);
  }

  if (id === "flappy") {

    birdV += 0.5;
    birdY += birdV;

    pipes.forEach(p => {
      p.x -= 3;

      ctx.fillStyle = "green";
      ctx.fillRect(p.x, 0, 50, p.h);
      ctx.fillRect(p.x, p.h + 150, 50, canvas.height);
    });

    if (pipes[pipes.length - 1].x < 300) {
      pipes.push({ x: 600, h: Math.random() * 200 });
    }

    ctx.fillStyle = "yellow";
    ctx.fillRect(100, birdY, 20, 20);
  }

  if (id === "clicker") {
    ctx.fillStyle = "white";
    ctx.font = "30px Arial";
    ctx.fillText("Clicks: " + clicks, 100, 100);
  }

  if (id === "tetris") {
    ctx.fillStyle = "cyan";
    ctx.fillRect(200, tY, 20, 20);
    tY += 3;
    if (tY > canvas.height) tY = 0;
  }
}

// =====================
// UTIL
// =====================
function random() {
  return {
    x: Math.floor(Math.random() * 50) * 10,
    y: Math.floor(Math.random() * 50) * 10
  };
}

// =====================
// BACK
// =====================
function back() {
  cancelAnimationFrame(loopId);

  document.getElementById("launcher").style.display = "flex";
  document.getElementById("gameScreen").style.display = "none";

  document.onkeydown = null;
}

// =====================
// CREATE GAME SYSTEM
// =====================

let modal;
let createBtn;
let submitBtn;
let closeBtn;

// ocultar botón hasta login
window.onload = () => {
  const btn = document.getElementById("createGameBtn");
  if (btn) btn.style.display = "none";

  modal = document.getElementById("createGameModal");
  createBtn = document.getElementById("createGameBtn");
  submitBtn = document.getElementById("submitGameBtn");
  closeBtn = document.getElementById("closeModalBtn");

  if (createBtn) {
    createBtn.onclick = () => {
      modal.classList.remove("hidden");
    };
  }

  if (closeBtn) {
    closeBtn.onclick = () => {
      modal.classList.add("hidden");
    };
  }

  if (submitBtn) {
    submitBtn.onclick = () => {

      const name = document.getElementById("gameName").value;
      const type = document.getElementById("gameType").value;

      if (!name || !type) {
        alert("Rellena todos los campos");
        return;
      }

      games.push({
        id: name.toLowerCase().replace(/\s/g, ""),
        title: "🆕 " + name,
        genre: type,
        description: "Juego creado por usuario"
      });

      render();

      modal.classList.add("hidden");

      document.getElementById("gameName").value = "";
      document.getElementById("gameType").value = "";

      alert("Formulario rellenado ✔");
    };
  }
};
// INIT
render();
