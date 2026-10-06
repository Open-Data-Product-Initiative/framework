(() => {
  "use strict";

  const body = document.body;
  const sidebar = document.getElementById("site-navigation");
  const toggle = document.getElementById("nav-toggle");
  const closeButton = document.getElementById("nav-close");
  const backdrop = document.getElementById("nav-backdrop");
  const mobileQuery = window.matchMedia("(max-width: 991.98px)");
  let previousFocus = null;

  const focusableSelector = [
    "a[href]",
    "button:not([disabled])",
    "[tabindex]:not([tabindex='-1'])"
  ].join(",");

  function setNavigationState(open, returnFocus = false) {
    const shouldOpen = Boolean(open && mobileQuery.matches);
    body.classList.toggle("nav-open", shouldOpen);
    toggle?.setAttribute("aria-expanded", String(shouldOpen));
    sidebar?.setAttribute("aria-hidden", String(mobileQuery.matches && !shouldOpen));

    if (shouldOpen) {
      previousFocus = document.activeElement;
      closeButton?.focus();
    } else if (returnFocus && previousFocus instanceof HTMLElement) {
      previousFocus.focus();
    }
  }

  toggle?.addEventListener("click", () => setNavigationState(true));
  closeButton?.addEventListener("click", () => setNavigationState(false, true));
  backdrop?.addEventListener("click", () => setNavigationState(false, true));

  document.addEventListener("keydown", (event) => {
    if (!body.classList.contains("nav-open")) return;

    if (event.key === "Escape") {
      event.preventDefault();
      setNavigationState(false, true);
      return;
    }

    if (event.key !== "Tab" || !sidebar) return;
    const focusable = [...sidebar.querySelectorAll(focusableSelector)].filter(
      (element) => element instanceof HTMLElement && element.offsetParent !== null
    );
    if (!focusable.length) return;

    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  document.querySelectorAll(".nav-group-toggle").forEach((button) => {
    button.addEventListener("click", () => {
      const group = button.closest(".nav-group");
      const open = !group?.classList.contains("is-open");
      group?.classList.toggle("is-open", open);
      button.setAttribute("aria-expanded", String(open));
    });
  });

  document.querySelectorAll(".sidebar a[href^='#']").forEach((link) => {
    link.addEventListener("click", () => {
      if (mobileQuery.matches) setNavigationState(false);
    });
  });

  function handleViewportChange() {
    if (!mobileQuery.matches) {
      body.classList.remove("nav-open");
      sidebar?.removeAttribute("aria-hidden");
      toggle?.setAttribute("aria-expanded", "false");
    } else if (!body.classList.contains("nav-open")) {
      sidebar?.setAttribute("aria-hidden", "true");
    }
  }

  mobileQuery.addEventListener("change", handleViewportChange);
  handleViewportChange();

  const trackedSections = [...document.querySelectorAll("[data-scroll-section]")];
  const navLinks = [...document.querySelectorAll("[data-nav-target]")];

  function markCurrent(id) {
    navLinks.forEach((link) => {
      const current = link.dataset.navTarget === id;
      if (current) {
        link.setAttribute("aria-current", "location");
        const group = link.closest(".nav-group");
        if (group) {
          group.classList.add("is-open");
          group.querySelector(".nav-group-toggle")?.setAttribute("aria-expanded", "true");
        }
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  if ("IntersectionObserver" in window && trackedSections.length) {
    const visible = new Map();
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) visible.set(entry.target.id, entry.boundingClientRect.top);
          else visible.delete(entry.target.id);
        });

        const nearest = [...visible.entries()].sort((a, b) => Math.abs(a[1]) - Math.abs(b[1]))[0];
        if (nearest) markCurrent(nearest[0]);
      },
      { rootMargin: "-15% 0px -70% 0px", threshold: [0, 0.01] }
    );
    trackedSections.forEach((section) => observer.observe(section));
  }

  const initialTarget = window.location.hash.slice(1) || "overview";
  markCurrent(initialTarget);
})();
