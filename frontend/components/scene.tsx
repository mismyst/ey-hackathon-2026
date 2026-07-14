"use client";

import { OrbitControls } from "@react-three/drei";
import { Canvas } from "@react-three/fiber";

function Cube() {
  return <mesh rotation={[0.35, 0.45, 0]}><boxGeometry args={[1.7, 1.7, 1.7]} /><meshStandardMaterial color="#22d3ee" emissive="#164e63" /></mesh>;
}

export function Scene() {
  return <div className="h-48 overflow-hidden rounded-lg border border-cyan-900"><Canvas camera={{ position: [3, 2, 4] }}><ambientLight intensity={1} /><pointLight position={[4, 4, 4]} intensity={20} /><Cube /><OrbitControls enablePan={false} /></Canvas></div>;
}
