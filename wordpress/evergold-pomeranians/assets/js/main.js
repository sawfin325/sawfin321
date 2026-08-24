(function () {
  const toggle = document.querySelector(".menu-toggle");
  const year = document.getElementById("year");
  const puppySelect = document.getElementById("inquiry-puppy") || document.getElementById("order-puppy");
  const wa = document.getElementById("order-whatsapp");
  const mail = document.getElementById("order-email");
  const waNumber = (window.evergoldOrder && evergoldOrder.wa) || "17432593337";
  const email = (window.evergoldOrder && evergoldOrder.email) || "miaspomeranian@gmail.com";

  if (toggle) {
    toggle.addEventListener("click", function () {
      document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", document.body.classList.contains("nav-open"));
    });
  }

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  const inquirySent = document.getElementById("inquiry-sent");
  if (inquirySent && new URLSearchParams(window.location.search).get("inquiry") === "sent") {
    inquirySent.hidden = false;
  }

  function messageFor(puppy) {
    return (
      "Hello Evergold, I would like to order " +
      puppy +
      ". Please send the latest video, the health packet, and reservation steps."
    );
  }

  function setOrderLinks(puppy) {
    const text = messageFor(puppy);
    if (wa) {
      wa.href = "https://wa.me/" + waNumber + "?text=" + encodeURIComponent(text);
    }
    if (mail) {
      mail.href =
        "mailto:" +
        email +
        "?subject=" +
        encodeURIComponent("Puppy order: " + puppy) +
        "&body=" +
        encodeURIComponent(text);
    }
  }

  if (puppySelect && (wa || mail)) {
    const params = new URLSearchParams(window.location.search);
    const wanted = (params.get("puppy") || "").toLowerCase();
    if (wanted) {
      Array.from(puppySelect.options).forEach(function (opt) {
        if (opt.value.toLowerCase() === wanted || opt.text.toLowerCase().indexOf(wanted) === 0) {
          puppySelect.value = opt.value;
        }
      });
    }
    const apply = function () {
      setOrderLinks(puppySelect.value || "a Pomeranian puppy");
    };
    puppySelect.addEventListener("change", apply);
    apply();
  }
})();
