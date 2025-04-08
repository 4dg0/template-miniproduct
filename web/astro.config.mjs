// @ts-check
import { defineConfig } from "astro/config";
import node from "@astrojs/node";
import svelte from "@astrojs/svelte";

import sitemap from "@astrojs/sitemap";

import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  integrations: [svelte(), sitemap()],

  vite: {
    plugins: [tailwindcss()],
  },

  redirects: {
    "/": "/welcome",
  },

  adapter: node({
    mode: "standalone",
  }),
});
