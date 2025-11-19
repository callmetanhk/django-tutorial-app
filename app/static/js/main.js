const API_BASE = "http://localhost:8000";


async function register() {
const data = {
username: document.getElementById('regUsername').value,
email: document.getElementById('regEmail').value,
password: document.getElementById('regPassword').value,
};


await fetch(`${API_BASE}/register/`, {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(data)
});


alert("Đăng ký thành công!");
window.location.href = "login.html";
}


async function login() {
const data = {
username: document.getElementById('logUsername').value,
password: document.getElementById('logPassword').value,
};


const res = await fetch(`${API_BASE}/login/`, {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(data)
});


const json = await res.json();


if (json.access) {
localStorage.setItem("access", json.access);
localStorage.setItem("refresh", json.refresh);
window.location.href = "home.html";
} else {
alert("Sai tài khoản hoặc mật khẩu!");
}
}


async function logout() {
const refresh = localStorage.getItem("refresh");


await fetch(`${API_BASE}/logout/`, {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({ refresh })
});


localStorage.clear();
alert("Đăng xuất thành công!");
window.location.href = "login.html";
}