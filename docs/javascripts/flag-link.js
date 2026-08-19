function addEnglishFlag() {
  document.querySelectorAll(".md-header__inner").forEach((header) => {
    if (header.querySelector(".md-header__flag")) return; // already added

    const search = header.querySelector('[data-md-component="search"]');

    const link = document.createElement("a");
    link.href = "/english.html";
    link.className = "md-header__button md-icon md-header__flag";
    link.setAttribute("aria-label", "English");
    link.title = "English";
    link.textContent = "🇬🇧";

    if (search) {
      search.insertAdjacentElement("afterend", link);
    } else {
      header.appendChild(link);
    }
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(addEnglishFlag);
} else {
  document.addEventListener("DOMContentLoaded", addEnglishFlag);
}
