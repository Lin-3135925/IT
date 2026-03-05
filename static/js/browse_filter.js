window.BROWSE_FILTER_LOADED = true;
console.log("[browse_filter] script loaded");

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#filter-form");
  const container = document.querySelector("#listing-container");
  if (!form || !container) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const params = new URLSearchParams(new FormData(form));
    const url = "/browse/partial/?" + params.toString();

    try {
      const res = await fetch(url, { headers: { "X-Requested-With": "XMLHttpRequest" } });
      if (!res.ok) throw new Error("HTTP " + res.status);

      const html = await res.text();
      container.innerHTML = html;
      console.log("[browse_filter] updated listings via AJAX");
    } catch (err) {
      console.log("[browse_filter] AJAX failed, fallback to normal submit", err);
      form.submit(); // fallback
    }
  });
});