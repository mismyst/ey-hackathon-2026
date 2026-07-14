"use client";

import { Activity, ShieldAlert } from "lucide-react";
import { useState } from "react";

import { Scene } from "@/components/scene";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { useWebSocket } from "@/hooks/useWebSocket";

export default function Home() {
  const { connected, lastMessage, send } = useWebSocket();
  const [message, setMessage] = useState("");
  return <main className="grid min-h-screen grid-cols-1 gap-px bg-slate-800 lg:grid-cols-[220px_1fr_280px]">
    <aside className="bg-slate-950 p-5"><div className="mb-10 flex items-center gap-2 text-lg font-bold text-cyan-300"><ShieldAlert /> SHELDRA</div><nav className="space-y-3 text-sm text-slate-400"><p className="text-cyan-300">Control room</p><p>Live hazards</p><p>Decision trees</p><p>Audit log</p></nav></aside>
    <section className="flex min-h-[70vh] flex-col gap-4 bg-slate-950 p-5"><header className="flex items-center justify-between"><div><h1 className="text-xl font-semibold">Safety intelligence</h1><p className="text-sm text-slate-400">Operational guidance and hazard awareness</p></div><span className={connected ? "text-sm text-emerald-400" : "text-sm text-amber-400"}>{connected ? "Live" : "Connecting…"}</span></header><Scene /><Card className="flex-1"><p className="text-sm text-slate-400">SHELDRA conversation</p><p className="mt-4">{lastMessage ? JSON.stringify(lastMessage) : "System ready. Ask SHELDRA about a safety condition."}</p></Card><form className="flex gap-2" onSubmit={(event) => { event.preventDefault(); if (message.trim()) { send({ message }); setMessage(""); } }}><Input value={message} onChange={(event) => setMessage(event.target.value)} placeholder="Describe a safety concern…" className="flex-1" /><Button type="submit">Send</Button></form></section>
    <aside className="space-y-4 bg-slate-950 p-5"><h2 className="font-semibold">Current context</h2><Card><p className="text-sm text-slate-400">Worker</p><p className="mt-1">Unassigned</p></Card><Card><p className="text-sm text-slate-400">Active hazard</p><p className="mt-1 text-emerald-400">None detected</p></Card><Card><div className="flex items-center gap-2 text-sm"><Activity className="h-4 w-4 text-cyan-300" /> Environment nominal</div></Card></aside>
  </main>;
}
