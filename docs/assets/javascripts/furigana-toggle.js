/**
 * furigana-toggle.js
 *
 * Adds a floating button to toggle furigana (ruby text) visibility.
 * Preference is persisted in localStorage.
 */
(function () {
  "use strict";

  const STORAGE_KEY = "kanji-roots-furigana-hidden";
  const HIDE_CLASS = "furigana-hidden";

  function getPref() {
    return localStorage.getItem(STORAGE_KEY) === "true";
  }

  function setPref(hidden) {
    localStorage.setItem(STORAGE_KEY, hidden ? "true" : "false");
  }

  function applyState(hidden) {
    document.body.classList.toggle(HIDE_CLASS, hidden);
  }

  function toggle() {
    const now = document.body.classList.contains(HIDE_CLASS);
    applyState(!now);
    setPref(!now);
    updateLabel();
  }

  function updateLabel() {
    const hidden = document.body.classList.contains(HIDE_CLASS);
    btn.textContent = hidden ? "Show あ" : "Hide あ";
  }

  const btn = document.createElement("button");
  btn.className = "furigana-toggle";
  btn.setAttribute("aria-label", "Toggle furigana");
  btn.setAttribute("title", "Show / hide furigana readings");
  btn.addEventListener("click", toggle);

  function init() {
    document.body.appendChild(btn);
    applyState(getPref());
    updateLabel();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
