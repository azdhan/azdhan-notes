import { FilePath, FullSlug, QUARTZ, joinSegments } from "../../util/path"
import { QuartzEmitterPlugin } from "../types"
import { BuildCtx } from "../../util/ctx"
import fs from "fs"
import { glob } from "../../util/glob"
import { dirname } from "path"
import { write } from "./helpers"

export const Static: QuartzEmitterPlugin = () => ({
  name: "Static",
  async *emit({ argv, cfg }) {
    const staticPath = joinSegments(QUARTZ, "static")
    const fps = await glob("**", staticPath, cfg.configuration.ignorePatterns)
    const outputStaticPath = joinSegments(argv.output, "static")
    await fs.promises.mkdir(outputStaticPath, { recursive: true })
    for (const fp of fps) {
      const src = joinSegments(staticPath, fp) as FilePath
      const dest = joinSegments(outputStaticPath, fp) as FilePath
      await fs.promises.mkdir(dirname(dest), { recursive: true })
      await fs.promises.copyFile(src, dest)
      yield dest
    }

    if (cfg.configuration.baseUrl) {
      const siteUrl = `https://${cfg.configuration.baseUrl}`
      const rootCtx = { argv, cfg } as BuildCtx

      yield write({
        ctx: rootCtx,
        slug: "robots" as FullSlug,
        ext: ".txt",
        content: [
          "User-agent: *",
          "Allow: /",
          "",
          `Sitemap: ${siteUrl}/sitemap.xml`,
          `LLM-Guide: ${siteUrl}/llms.txt`,
        ].join("\n"),
      })

      yield write({
        ctx: rootCtx,
        slug: "llms" as FullSlug,
        ext: ".txt",
        content: [
          "# azdhan's digital garden",
          "",
          "A public digital garden of notes by Azdhan Basha, focused on technology policy, AI, surveillance, censorship, cinema, books, and personal research trails.",
          "",
          "## Entry Points",
          `- Home: ${siteUrl}/`,
          `- Sitemap: ${siteUrl}/sitemap.xml`,
          `- RSS feed: ${siteUrl}/index.xml`,
          `- Machine-readable content index: ${siteUrl}/static/contentIndex.json`,
          `- Full LLM guide: ${siteUrl}/llms-full.txt`,
          "",
          "## Use",
          "The notes are public and shared under a Creative Commons Attribution 4.0 International license.",
        ].join("\n"),
      })

      yield write({
        ctx: rootCtx,
        slug: "llms-full" as FullSlug,
        ext: ".txt",
        content: [
          "# azdhan's digital garden",
          "",
          "This site is a public notes garden generated from Markdown. It has static HTML pages, a sitemap, an RSS feed, and a JSON content index suitable for search tools and AI agents.",
          "",
          "## Crawl Paths",
          `- Start page: ${siteUrl}/`,
          `- Sitemap: ${siteUrl}/sitemap.xml`,
          `- RSS: ${siteUrl}/index.xml`,
          `- Content index JSON: ${siteUrl}/static/contentIndex.json`,
          "",
          "## Content Notes",
          "Pages may include unfinished notes, source links, transcripts, research trails, lists, and draft-like public thinking. Prefer citing the canonical page URL for any referenced note.",
          "",
          "## License",
          "Unless otherwise noted, notes are licensed under Creative Commons Attribution 4.0 International.",
        ].join("\n"),
      })
    }
  },
  async *partialEmit() {},
})
