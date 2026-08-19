function addEnglishFlag() {
  document.querySelectorAll(".md-header__inner").forEach((header) => {
    // Desktop flag
    if (!header.querySelector(".md-header__flag")) {
      const search = header.querySelector('[data-md-component="search"]');

      const link = document.createElement("a");
      link.href = "/english";
      link.className = "md-header__button md-icon md-header__flag";
      link.setAttribute("aria-label", "English");
      link.title = "English";
      link.textContent = "🇬🇧";

      if (search) {
        search.insertAdjacentElement("afterend", link);
      } else {
        header.appendChild(link);
      }
    }
  });

  // Mobile navigation flag
  document.querySelectorAll(".md-nav--primary").forEach((nav) => {
    const list = nav.querySelector(".md-nav__list");

    if (!list || list.querySelector(".md-nav__english")) return;

    const li = document.createElement("li");
    li.className = "md-nav__item md-nav__english";

    const link = document.createElement("a");
    link.href = "/english";
    link.className = "md-nav__link";
    link.setAttribute("aria-label", "English");
    link.textContent = "🇬🇧  English";

    li.appendChild(link);
    list.appendChild(li);
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(addEnglishFlag);
} else {
  document.addEventListener("DOMContentLoaded", addEnglishFlag);
}
