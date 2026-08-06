import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Space Shooter",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Space Shooter")
st.caption("Controls: **WASD** or **Arrow Keys** to move | **Spacebar** to shoot | **R** to restart after Game Over")

game_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #0b0d17;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            overflow: hidden;
        }
        #gameCanvas {
            border: 2px solid #4a4e69;
            box-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
            border-radius: 8px;
            background: #05050d;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="600" height="600"></canvas>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        let score = 0;
        let lives = 3;
        let gameOver = false;
        let gameStarted = false;
        let frameCount = 0;

        const keys = {
            ArrowLeft: false,
            ArrowRight: false,
            ArrowUp: false,
            ArrowDown: false,
            KeyA: false,
            KeyD: false,
            KeyW: false,
            KeyS: false,
            Space: false
        };

        window.addEventListener("keydown", (e) => {
            if (e.code in keys) {
                keys[e.code] = true;
                if (e.code === "Space" || e.code.startsWith("Arrow")) {
                    e.preventDefault();
                }
            }
            if (gameOver && e.code === "KeyR") {
                resetGame();
            }
            if (!gameStarted && e.code === "Space") {
                gameStarted = true;
            }
        });

        window.addEventListener("keyup", (e) => {
            if (e.code in keys) {
                keys[e.code] = false;
            }
        });

        const player = {
            x: canvas.width / 2 - 20,
            y: canvas.height - 70,
            width: 40,
            height: 40,
            speed: 5,
            lastShot: 0,
            shootDelay: 10
        };

        let bullets = [];
        let enemies = [];
        let particles = [];
        let stars = [];

        for (let i = 0; i < 80; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 2 + 0.5,
                speed: Math.random() * 1.5 + 0.5
            });
        }

        function resetGame() {
            score = 0;
            lives = 3;
            gameOver = false;
            gameStarted = true;
            bullets = [];
            enemies = [];
            particles = [];
            player.x = canvas.width / 2 - 20;
            player.y = canvas.height - 70;
        }

        function createExplosion(x, y, color, count = 15) {
            for (let i = 0; i < count; i++) {
                particles.push({
                    x: x,
                    y: y,
                    vx: (Math.random() - 0.5) * 6,
                    vy: (Math.random() - 0.5) * 6,
                    size: Math.random() * 3 + 1,
                    color: color,
                    life: 30
                });
            }
        }

        function update() {
            frameCount++;

            stars.forEach(star => {
                star.y += star.speed;
                if (star.y > canvas.height) {
                    star.y = 0;
                    star.x = Math.random() * canvas.width;
                }
            });

            if (!gameStarted || gameOver) return;

            if ((keys.ArrowLeft || keys.KeyA) && player.x > 0) {
                player.x -= player.speed;
            }
            if ((keys.ArrowRight || keys.KeyD) && player.x < canvas.width - player.width) {
                player.x += player.speed;
            }
            if ((keys.ArrowUp || keys.KeyW) && player.y > 0) {
                player.y -= player.speed;
            }
            if ((keys.Arrow
