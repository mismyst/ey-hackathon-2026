"use client";

import { useCallback, useEffect, useRef, useState } from "react";

export function useWebSocket(url = process.env.NEXT_PUBLIC_WS_URL ?? "ws://localhost:8000/ws") {
  const socket = useRef<WebSocket | null>(null);
  const [connected, setConnected] = useState(false);
  const [lastMessage, setLastMessage] = useState<Record<string, unknown> | null>(null);

  useEffect(() => {
    const connection = new WebSocket(url);
    socket.current = connection;
    connection.onopen = () => setConnected(true);
    connection.onclose = () => setConnected(false);
    connection.onmessage = (event) => setLastMessage(JSON.parse(event.data));
    return () => connection.close();
  }, [url]);

  const send = useCallback((message: Record<string, unknown>) => {
    if (socket.current?.readyState === WebSocket.OPEN) socket.current.send(JSON.stringify(message));
  }, []);

  return { connected, lastMessage, send };
}
