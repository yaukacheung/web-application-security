// Chapters 6 & 8 Sample Code: Express Session Cookie Hardening & CSRF Middleware

const crypto = require("crypto");

function setHardenedSessionCookie(res, sessionId) {
  res.cookie("__Host-sid", sessionId, {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    path: "/",
    maxAge: 30 * 60 * 1000, // 30-minute idle/session window
  });
}

function onLoginSuccess(req, res, user) {
  // Regenerate session identifier on privilege change to prevent session fixation
  req.session.regenerate((err) => {
    if (err) return res.status(500).json({ error: "Session error" });
    req.session.userId = user.id;
    req.session.csrfToken = crypto.randomBytes(32).toString("hex");
    setHardenedSessionCookie(res, req.sessionID);
    return res.json({ status: "authenticated" });
  });
}

function verifyCsrfToken(req, res, next) {
  if (["GET", "HEAD", "OPTIONS"].includes(req.method)) return next();
  const submitted = req.get("X-CSRF-Token") || "";
  const expected = req.session?.csrfToken || "";
  if (
    submitted.length !== expected.length ||
    !crypto.timingSafeEqual(Buffer.from(submitted), Buffer.from(expected))
  ) {
    return res.status(403).json({ error: "Invalid CSRF token" });
  }
  return next();
}

module.exports = { setHardenedSessionCookie, onLoginSuccess, verifyCsrfToken };
