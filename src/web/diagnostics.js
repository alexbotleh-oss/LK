/* B77 Application Diagnostic — observation only.
 * No business decisions, no scanner replacement, no UI replacement.
 */
(function (global) {
  "use strict";

  const KEY = "b77_runtime_diagnostics_v1";
  const MAX = 500;
  let installed = false;
  const events = [];

  function now() { return new Date().toISOString(); }

  function push(area, event, data) {
    const item = {
      t: now(),
      area: String(area || "app"),
      event: String(event || "event"),
      data: data == null ? null : data
    };
    events.push(item);
    if (events.length > MAX) events.splice(0, events.length - MAX);
    try { localStorage.setItem(KEY, JSON.stringify(events)); } catch (_) {}
    return item;
  }

  function snapshot() {
    const screens = Array.from(document.querySelectorAll(".screen")).map(function (el) {
      const cs = getComputedStyle(el);
      return {
        id: el.id || "",
        active: el.classList.contains("active"),
        opacity: cs.opacity,
        pointerEvents: cs.pointerEvents,
        display: cs.display,
        visibility: cs.visibility
      };
    });

    return {
      t: now(),
      href: location.href,
      readyState: document.readyState,
      secureContext: !!global.isSecureContext,
      mediaDevices: !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia),
      barcodeDetector: typeof global.BarcodeDetector === "function",
      screens: screens
    };
  }

  function install() {
    if (installed) return;
    installed = true;

    try {
      const saved = JSON.parse(localStorage.getItem(KEY) || "[]");
      if (Array.isArray(saved)) events.push.apply(events, saved.slice(-MAX));
    } catch (_) {}

    global.addEventListener("error", function (e) {
      push("runtime", "error", {
        message: e.message || "",
        source: e.filename || "",
        line: e.lineno || 0,
        column: e.colno || 0
      });
    });

    global.addEventListener("unhandledrejection", function (e) {
      push("runtime", "unhandledrejection", {
        reason: String(e.reason && e.reason.stack || e.reason || "")
      });
    });

    document.addEventListener("visibilitychange", function () {
      push("lifecycle", "visibilitychange", { hidden: document.hidden });
    });

    push("boot", "installed", snapshot());
  }

  function event(area, name, data) {
    return push(area, name, data);
  }

  function cameraState(state, data) {
    return push("scanner.camera", state, data);
  }

  function scannerEvent(name, data) {
    return push("scanner", name, data);
  }

  function getReport() {
    return {
      schema: "b77-runtime-diagnostic-1",
      generated_at: now(),
      snapshot: snapshot(),
      events: events.slice()
    };
  }

  function download() {
    const blob = new Blob([JSON.stringify(getReport(), null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "B77_runtime_diagnostic_" + new Date().toISOString().replace(/[:.]/g, "-") + ".json";
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
  }

  global.B77Diag = {
    install: install,
    event: event,
    cameraState: cameraState,
    scannerEvent: scannerEvent,
    snapshot: snapshot,
    report: getReport,
    download: download
  };
})(window);
