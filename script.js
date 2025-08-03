async function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class='user-msg'>You: ${userInput}</div>`;

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();
    chatBox.innerHTML += `<div class='bot-msg'>Bot: ${data.response}</div>`;

    // 🔊 Play bot reply sound
    document.getElementById("bot-sound").play();

    document.getElementById("user-input").value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}

// 🌈 Toggle Theme
function toggleTheme() {
    const body = document.body;

    if (body.classList.contains("lavender")) {
        body.classList.remove("lavender");
        body.classList.add("dark");
        localStorage.setItem("theme", "dark");
    } else if (body.classList.contains("dark")) {
        body.classList.remove("dark");
        localStorage.setItem("theme", "pink");
    } else {
        body.classList.add("lavender");
        localStorage.setItem("theme", "lavender");
    }
}

// 🧠 Load theme from localStorage
function loadTheme() {
    const theme = localStorage.getItem("theme");
    if (theme) document.body.classList.add(theme);
}
