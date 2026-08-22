import { createHash, randomUUID } from "node:crypto";
import { getStore } from "@netlify/blobs";

const ADMIN_PASSWORD_HASH = "cb13a717bf8373e3af8204bcd27d83936a0f5a9675c37b15859d0c31b83938c8";
const json = (value, status = 200) => Response.json(value, { status, headers: { "Cache-Control": "no-store" } });
const isAdmin = (password = "") => createHash("sha256").update(String(password)).digest("hex") === ADMIN_PASSWORD_HASH;

export default async (request) => {
  const store = getStore({ name: "portfolio-certificates", consistency: "strong" });
  const certificates = await store.get("certificates", { type: "json", consistency: "strong" }) || [];
  if (request.method === "GET") return json(certificates);

  let body;
  try { body = await request.json(); } catch { return json({ error: "Invalid request body." }, 400); }
  if (!isAdmin(body.password)) return json({ error: "Admin access required." }, 403);

  if (request.method === "POST") {
    const certificate = body.certificate || {};
    if (!certificate.title || !certificate.type || !certificate.fileData) return json({ error: "Certificate title, type, and file are required." }, 400);
    const saved = { ...certificate, id: certificate.id || randomUUID() };
    await store.setJSON("certificates", [saved, ...certificates.filter(item => item.id !== saved.id)]);
    return json(saved, 201);
  }
  if (request.method === "DELETE") {
    const next = certificates.filter(item => item.id !== body.id);
    if (next.length === certificates.length) return json({ error: "Certificate not found." }, 404);
    await store.setJSON("certificates", next);
    return json({ deleted: true });
  }
  return json({ error: "Method not allowed." }, 405);
};
