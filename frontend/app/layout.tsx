import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = { title: "SHELDRA Control Room", description: "Industrial safety intelligence" };

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en" className="dark"><body>{children}</body></html>;
}
