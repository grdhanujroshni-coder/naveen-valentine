from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>For Naveen 💖</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                background: linear-gradient(to bottom, #fbc2eb, #a6c1ee);
                color: white;
                overflow-x: hidden;
            }

            .container {
                margin-top: 80px;
            }

            h1 {
                font-size: 3em;
                font-weight: 300;
            }

            button {
                padding: 12px 25px;
                margin: 15px;
                font-size: 16px;
                border: none;
                border-radius: 30px;
                cursor: pointer;
                background: white;
                color: #ff6fa5;
                transition: 0.3s;
            }

            button:hover {
                transform: scale(1.1);
            }

            #hidden-message {
                display: none;
                margin-top: 30px;
                font-size: 20px;
            }

            .heart {
                position: fixed;
                bottom: -10px;
                font-size: 20px;
                animation: floatUp 6s linear infinite;
            }

            @keyframes floatUp {
                0% { transform: translateY(0); opacity: 1; }
                100% { transform: translateY(-100vh); opacity: 0; }
            }

            .modal {
                display: none;
                position: fixed;
                width: 100%;
                height: 100%;
                background: rgba(255,182,193,0.4);
                backdrop-filter: blur(5px);
            }

            .modal-content {
                background: white;
                color: #ff6fa5;
                margin: 10% auto;
                padding: 30px;
                border-radius: 20px;
                width: 70%;
            }

            .close {
                float: right;
                font-size: 25px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <h1>Naveen 💖</h1>
            <h2>Happy Valentine's Day</h2>
            <p>You are my calm, my happiness, and my forever.</p>

            <h3>Will you be my forever Valentine?</h3>

            <button onclick="sayYes()">Yes, always 💕</button>
            <button id="noBtn" onmouseover="moveButton()">No 🙈</button>

            <div id="hidden-message">
                <h3>I knew it 💞</h3>
                <button onclick="openLetter()">Read My Heart 💌</button>
            </div>
        </div>

        <div id="letterModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeLetter()">&times;</span>
                <h2>To My Naveen ❤️</h2>
                <p>
                Loving you is the softest and most beautiful thing in my life.
                You make everything brighter just by being you.
                I choose you today, tomorrow, and always.
                </p>
            </div>
        </div>

        <audio id="music" loop>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
        </audio>

        <script>
            function sayYes() {
                document.getElementById("hidden-message").style.display = "block";
                document.getElementById("music").play();
            }

            function moveButton() {
                const btn = document.getElementById("noBtn");
                btn.style.position = "absolute";
                btn.style.left = Math.random() * 80 + "%";
                btn.style.top = Math.random() * 80 + "%";
            }

            function openLetter() {
                document.getElementById("letterModal").style.display = "block";
            }

            function closeLetter() {
                document.getElementById("letterModal").style.display = "none";
            }

            setInterval(() => {
                const heart = document.createElement("div");
                heart.classList.add("heart");
                heart.innerHTML = "💗";
                heart.style.left = Math.random() * 100 + "vw";
                heart.style.fontSize = (Math.random() * 15 + 15) + "px";
                document.body.appendChild(heart);

                setTimeout(() => heart.remove(), 6000);
            }, 500);
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()

