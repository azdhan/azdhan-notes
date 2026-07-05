import { jsx, jsxs } from "preact/jsx-runtime";
import { formatDate } from "@quartz-community/utils/date";
import { byDateAndAlphabetical, getDate } from "@quartz-community/utils/sort";
import { isFolderPath, resolveRelative } from "@quartz-community/utils/path";
import { classNames } from "@quartz-community/utils/lang";

function isTagPageSlug(slug) {
  if (!slug) return false;
  return slug === "tags" || slug === "tags/index" || slug.startsWith("tags/");
}

function isFolderPageSlug(slug) {
  if (!slug) return false;
  return isFolderPath(slug);
}

function filterListedPages(pages) {
  return pages.filter((p) => p.unlisted !== true);
}

const defaultOptions = () => ({
  title: "Recent Notes",
  limit: 8,
  linkToMore: false,
  showTags: false,
  hideTagPages: true,
  hideFolderPages: true,
  filter: () => true,
  sort: byDateAndAlphabetical(),
});

export const RecentNotes = (userOpts) => {
  const opts = { ...defaultOptions(), ...userOpts };

  const RecentNotesComponent = ({ allFiles, fileData, displayClass }) => {
    const pages = filterListedPages(allFiles)
      .filter((p) => !opts.hideTagPages || !isTagPageSlug(p.slug))
      .filter((p) => !opts.hideFolderPages || !isFolderPageSlug(p.slug))
      .filter(opts.filter)
      .sort(opts.sort);
    const remaining = Math.max(0, pages.length - opts.limit);
    const slug = fileData.slug;

    const listItems = pages.slice(0, opts.limit).map((page) => {
      const title = page.frontmatter?.title ?? "Untitled";
      const tags = page.frontmatter?.tags ?? [];
      const date = page.dates ? getDate(page) : undefined;

      return jsx("li", {
        class: "recent-li",
        children: jsxs("div", {
          class: "section",
          children: [
            jsx("div", {
              class: "desc",
              children: jsx("h3", {
                children: jsx("a", {
                  href: resolveRelative(slug, page.slug),
                  class: "internal",
                  children: title,
                }),
              }),
            }),
            date &&
              jsx("p", {
                class: "meta",
                children: jsx("time", {
                  datetime: date.toISOString(),
                  children: formatDate(date),
                }),
              }),
            opts.showTags &&
              jsx("ul", {
                class: "tags",
                children: tags.map((tag) =>
                  jsx("li", {
                    children: jsx("a", {
                      class: "internal tag-link",
                      href: resolveRelative(slug, `tags/${tag}`),
                      children: tag,
                    }),
                  }),
                ),
              }),
          ],
        }),
      });
    });

    return jsxs("details", {
      class: classNames(displayClass, "recent-notes-details"),
      children: [
        jsx("summary", { children: opts.title }),
        jsxs("div", {
          class: "recent-notes",
          children: [
            jsx("ul", { class: "recent-ul", children: listItems }),
            opts.linkToMore &&
              remaining > 0 &&
              jsx("p", {
                children: jsx("a", {
                  href: resolveRelative(slug, opts.linkToMore),
                  children: `${remaining} more`,
                }),
              }),
          ],
        }),
      ],
    });
  };

  RecentNotesComponent.css = `
.recent-notes-details > summary {
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 500;
  margin: 0.5rem 0;
  list-style: revert;
}

@media all and (min-width: 801px) {
  .recent-notes-details > .recent-notes {
    display: block !important;
  }
  .recent-notes-details > summary {
    cursor: default;
    list-style: none;
  }
}
`;

  RecentNotesComponent.afterDOMLoaded = `
function fixTagLinkText() {
  document.querySelectorAll('a.tag-link[href*="/tags/"]').forEach((el) => {
    const href = el.getAttribute("href");
    const match = href.match(/\\/tags\\/([^?#]+?)\\/?$/);
    if (!match) return;
    const fullTag = decodeURIComponent(match[1]).toLowerCase();
    if (fullTag && el.textContent.toLowerCase() !== fullTag) {
      el.textContent = fullTag;
    }
  });
}
document.addEventListener("nav", fixTagLinkText);
fixTagLinkText();
`;

  return RecentNotesComponent;
};
