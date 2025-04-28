// frontend/js/app.js

document.getElementById("scanBtn").addEventListener("click", async () => {
    const res = await fetch("/scan"); // <-- use relative URL now
    const data = await res.json();
    const results = document.getElementById("results");
    results.innerHTML = "";
    data.hosts.forEach(host => {
        const li = document.createElement("li");
        li.textContent = host;
        results.appendChild(li);
    });
});
