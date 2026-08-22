import { createHash, randomUUID } from "node:crypto";
import { getStore } from "@netlify/blobs";

const ADMIN_PASSWORD_HASH = "cb13a717bf8373e3af8204bcd27d83936a0f5a9675c37b15859d0c31b83938c8";
const json = (value, status = 200) => Response.json(value, { status, headers: { "Cache-Control": "no-store" } });
const isAdmin = (password = "") => createHash("sha256").update(String(password)).digest("hex") === ADMIN_PASSWORD_HASH;

export default async (request) => {
  const store = getStore({ name: "portfolio-showcase", consistency: "strong" });
  const items = await store.get("items", { type: "json", consistency: "strong" }) || [];
  if (request.method === "GET") return json(items);

  let body;
  try { body = await request.json(); } catch { return json({ error: "Invalid request body." }, 400); }
  if (!isAdmin(body.password)) return json({ error: "Admin access required." }, 403);

  if (request.method === "POST") {
    const item = body.item || {};
    if (!item.title || !item.url) return json({ error: "Title and URL are required." }, 400);
    const saved = { ...item, id: item.id || randomUUID() };
    await store.setJSON("items", [saved, ...items.filter(existing => existing.id !== saved.id)]);
    return json(saved, 201);
  }
  if (request.method === "DELETE") {
    const next = items.filter(item => item.id !== body.id);
    if (next.length === items.length) return json({ error: "Showcase item not found." }, 404);
    await store.setJSON("items", next);
    return json({ deleted: true });
  }
  return json({ error: "Method not allowed." }, 405);
};
