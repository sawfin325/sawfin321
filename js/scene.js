function mountScene() {
  if (document.getElementById("bg-3d")) return;
  const root = document.createElement("div");
  root.id = "bg-3d";
  root.setAttribute("aria-hidden", "true");
  root.innerHTML = `
    <canvas></canvas>
    <div class="bg-sculpt bg-sculpt-l"></div>
    <div class="bg-sculpt bg-sculpt-r"></div>
    <div class="bg-sculpt bg-sculpt-c"></div>
    <div class="bg-vignette"></div>
  `;
  document.body.prepend(root);
  const canvas = root.querySelector("canvas");
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduced) {
    document.body.classList.add("bg-static");
    return;
  }
  startAtelierScene(canvas);
}

function startAtelierScene(canvas) {
  const ctx = canvas.getContext("2d", { alpha: true });
  const rings = [
    { R: 220, r: 18, ax: 1.05, ay: 0.35, az: 0, sx: 0.22, sy: 0.18, sz: 0.31, x: -280, y: 40, z: 80, gold: 0 },
    { R: 160, r: 12, ax: 0.7, ay: 1.2, az: 0.4, sx: -0.16, sy: 0.24, sz: -0.2, x: 310, y: -70, z: 40, gold: 1 },
    { R: 110, r: 9, ax: 1.4, ay: 0.2, az: 0.8, sx: 0.28, sy: -0.14, sz: 0.19, x: 40, y: 180, z: 120, gold: 0 },
    { R: 90, r: 8, ax: 0.4, ay: 0.9, az: 0.2, sx: -0.21, sy: 0.11, sz: 0.27, x: -340, y: -160, z: 20, gold: 1 },
  ];
  const discs = [
    { x: 260, y: 140, z: 90, r: 46, spin: 0, vs: 0.008 },
    { x: -220, y: -90, z: 50, r: 34, spin: 1.2, vs: -0.01 },
  ];
  const dust = Array.from({ length: 90 }, (_, i) => ({
    x: (Math.random() - 0.5) * 900,
    y: (Math.random() - 0.5) * 700,
    z: Math.random() * 400 - 80,
    s: 0.8 + Math.random() * 2.2,
    v: 0.15 + Math.random() * 0.45,
  }));
  let w = 0, h = 0, dpr = 1, mx = 0, my = 0, tx = 0, ty = 0, t = 0, running = true;

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 1.6);
    w = window.innerWidth;
    h = window.innerHeight;
    canvas.width = Math.floor(w * dpr);
    canvas.height = Math.floor(h * dpr);
    canvas.style.width = w + "px";
    canvas.style.height = h + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function rot(x, y, z, ax, ay, az) {
    let y1 = y * Math.cos(ax) - z * Math.sin(ax);
    let z1 = y * Math.sin(ax) + z * Math.cos(ax);
    y = y1; z = z1;
    let x1 = x * Math.cos(ay) + z * Math.sin(ay);
    z1 = -x * Math.sin(ay) + z * Math.cos(ay);
    x = x1; z = z1;
    x1 = x * Math.cos(az) - y * Math.sin(az);
    y1 = x * Math.sin(az) + y * Math.cos(az);
    return { x: x1, y: y1, z: z1 };
  }

  function project(p, ox, oy) {
    const z = p.z + 520;
    const f = 620 / Math.max(120, z);
    return { x: ox + p.x * f, y: oy + p.y * f, f, z: p.z };
  }

  function gold(i, a) {
    return i
      ? `rgba(246, 226, 122, ${a})`
      : `rgba(201, 162, 39, ${a})`;
  }

  function drawRing(ring, cx, cy) {
    const steps = 96;
    ctx.beginPath();
    let started = false;
    for (let i = 0; i <= steps; i++) {
      const u = (i / steps) * Math.PI * 2;
      const x = (ring.R + ring.r * Math.cos(u * 2)) * Math.cos(u);
      const y = (ring.R + ring.r * Math.cos(u * 2)) * Math.sin(u);
      const z = ring.r * Math.sin(u * 2) * 0.35;
      const p = rot(x, y, z, ring.ax, ring.ay, ring.az);
      p.x += ring.x;
      p.y += ring.y;
      p.z += ring.z;
      const q = project(p, cx, cy);
      if (!started) { ctx.moveTo(q.x, q.y); started = true; }
      else ctx.lineTo(q.x, q.y);
    }
    ctx.strokeStyle = gold(ring.gold, 0.55);
    ctx.lineWidth = 2.2;
    ctx.shadowColor = "rgba(212,175,55,0.45)";
    ctx.shadowBlur = 18;
    ctx.stroke();
    ctx.shadowBlur = 0;
    ctx.beginPath();
    for (let i = 0; i <= steps; i++) {
      const u = (i / steps) * Math.PI * 2;
      const x = (ring.R - 10) * Math.cos(u);
      const y = (ring.R - 10) * Math.sin(u);
      const p = rot(x, y, 0, ring.ax, ring.ay, ring.az);
      p.x += ring.x; p.y += ring.y; p.z += ring.z;
      const q = project(p, cx, cy);
      if (i === 0) ctx.moveTo(q.x, q.y); else ctx.lineTo(q.x, q.y);
    }
    ctx.strokeStyle = gold(ring.gold, 0.18);
    ctx.lineWidth = 1;
    ctx.stroke();
  }

  function drawDisc(d, cx, cy) {
    const p = rot(d.x, d.y, d.z, 0.9, d.spin, 0.2);
    const q = project(p, cx, cy);
    const rad = d.r * q.f;
    const g = ctx.createRadialGradient(q.x - rad * 0.3, q.y - rad * 0.3, rad * 0.1, q.x, q.y, rad);
    g.addColorStop(0, "rgba(255, 236, 170, 0.55)");
    g.addColorStop(0.45, "rgba(176, 138, 42, 0.28)");
    g.addColorStop(1, "rgba(40, 30, 10, 0.0)");
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.ellipse(q.x, q.y, rad, rad * 0.62, d.spin, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = "rgba(246,226,122,0.5)";
    ctx.lineWidth = 1.5;
    ctx.stroke();
  }

  function frame(now) {
    if (!running) return;
    t = now * 0.001;
    mx += (tx - mx) * 0.04;
    my += (ty - my) * 0.04;
    const cx = w * 0.5 + mx * 28;
    const cy = h * 0.48 + my * 18;
    ctx.clearRect(0, 0, w, h);

    const fog = ctx.createRadialGradient(cx, cy, 40, cx, cy, Math.max(w, h) * 0.72);
    fog.addColorStop(0, "rgba(28, 22, 10, 0.18)");
    fog.addColorStop(1, "rgba(6, 7, 10, 0)");
    ctx.fillStyle = fog;
    ctx.fillRect(0, 0, w, h);

    rings.forEach((ring) => {
      ring.ax += ring.sx * 0.008;
      ring.ay += ring.sy * 0.008;
      ring.az += ring.sz * 0.008;
      drawRing(ring, cx, cy);
    });
    discs.forEach((d) => {
      d.spin += d.vs;
      drawDisc(d, cx, cy);
    });
    dust.forEach((p) => {
      p.y -= p.v;
      if (p.y < -360) p.y = 360;
      const q = project(p, cx, cy);
      const a = 0.15 + (p.z + 80) / 900;
      ctx.fillStyle = `rgba(246, 226, 122, ${Math.max(0.04, Math.min(0.55, a))})`;
      ctx.beginPath();
      ctx.arc(q.x, q.y, p.s * q.f, 0, Math.PI * 2);
      ctx.fill();
    });
    requestAnimationFrame(frame);
  }

  window.addEventListener("resize", resize, { passive: true });
  window.addEventListener("pointermove", (e) => {
    tx = (e.clientX / w) * 2 - 1;
    ty = (e.clientY / h) * 2 - 1;
  }, { passive: true });
  document.addEventListener("visibilitychange", () => {
    running = !document.hidden;
    if (running) requestAnimationFrame(frame);
  });
  resize();
  requestAnimationFrame(frame);
}
