(function () {
    var STORAGE_KEY = "aniref-theme";
    var root = document.documentElement;

    function systemIsDark() {
        return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    }

    var toggle = document.querySelector("[data-theme-toggle]");
    if (toggle) {
        toggle.addEventListener("click", function () {
            var current = root.getAttribute("data-theme") || (systemIsDark() ? "dark" : "light");
            var next = current === "dark" ? "light" : "dark";
            root.setAttribute("data-theme", next);
            try { localStorage.setItem(STORAGE_KEY, next); } catch (e) {}
        });
    }

    var menuButton = document.querySelector("[data-menu-toggle]");
    var links = document.getElementById("nav-links");
    if (menuButton && links) {
        menuButton.addEventListener("click", function () {
            var open = links.classList.toggle("open");
            menuButton.setAttribute("aria-expanded", open ? "true" : "false");
        });
    }

    var year = document.querySelector("[data-year]");
    if (year) year.textContent = new Date().getFullYear();
})();
