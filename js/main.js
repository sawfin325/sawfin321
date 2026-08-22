(function () {
  const toggle = document.querySelector(".menu-toggle");
  const year = document.getElementById("year");
  const form = document.getElementById("contact-form");
  const note = document.querySelector(".form-note");

  if (toggle) {
    toggle.addEventListener("click", function () {
      document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", document.body.classList.contains("nav-open"));
    });
  }

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  if (form && note) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      form.reset();
      note.style.display = "block";
    });
  }
})();
