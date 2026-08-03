import { jsx, jsxs } from "preact/jsx-runtime";

const style = `
.page-actions {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 0.35rem;
  margin: 0 0 0.75rem;
}

.page-actions button {
  width: 2rem;
  height: 2rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--darkgray);
  background: color-mix(in srgb, var(--light) 92%, transparent);
  border: 1px solid color-mix(in srgb, var(--lightgray) 78%, transparent);
  border-radius: 8px;
  box-shadow: none;
  cursor: pointer;
  opacity: 0.72;
  transition:
    background-color 160ms ease,
    border-color 160ms ease,
    color 160ms ease,
    opacity 160ms ease,
    transform 160ms ease;
}

.page-actions button:hover,
.page-actions button:focus-visible {
  color: var(--secondary);
  background: var(--light);
  border-color: color-mix(in srgb, var(--secondary) 34%, var(--lightgray));
  opacity: 1;
  transform: translateY(-1px);
}

.page-actions button:active {
  transform: translateY(0);
}

.page-actions svg {
  width: 1rem;
  height: 1rem;
  stroke-width: 1.8;
}

@media print {
  .page-actions {
    display: none !important;
  }
}
`;

const script = `
const actionSelector = ".page-actions";

function getSafeFilename(title) {
  return (title || "note")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 90) || "note";
}

async function getCurrentNote() {
  const slug = document.body.dataset.slug;
  const index = await window.fetchData;
  const note = index?.[slug];
  const title = note?.title || document.querySelector(".article-title, h1")?.textContent?.trim() || document.title;
  const content = note?.content || document.querySelector("article")?.innerText?.trim() || "";
  return { title, content };
}

function getMarkdown(note) {
  const title = note.title?.trim();
  const content = note.content?.trim();
  return [title ? "# " + title : "", content].filter(Boolean).join("\\n\\n") + "\\n";
}

function downloadBlob(filename, type, text) {
  const blob = new Blob([text], { type });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

function setCopied(button) {
  const previous = button.getAttribute("aria-label");
  button.setAttribute("aria-label", "Copied");
  button.dataset.copied = "true";
  window.setTimeout(() => {
    button.setAttribute("aria-label", previous || "Copy to clipboard");
    delete button.dataset.copied;
  }, 1400);
}

function bindPageActions() {
  const root = document.querySelector(actionSelector);
  if (!root || root.dataset.bound === "true") return;
  root.dataset.bound = "true";

  root.addEventListener("click", async (event) => {
    const button = event.target.closest("button[data-action]");
    if (!button) return;

    const note = await getCurrentNote();
    const markdown = getMarkdown(note);
    const filename = getSafeFilename(note.title);
    const action = button.dataset.action;

    if (action === "copy") {
      await navigator.clipboard.writeText(markdown);
      setCopied(button);
    } else if (action === "markdown") {
      downloadBlob(filename + ".md", "text/markdown;charset=utf-8", markdown);
    } else if (action === "pdf") {
      const originalTitle = document.title;
      document.title = note.title || originalTitle;
      window.print();
      window.setTimeout(() => {
        document.title = originalTitle;
      }, 500);
    }
  });
}

document.addEventListener("nav", bindPageActions);
bindPageActions();
`;

const iconProps = {
  xmlns: "http://www.w3.org/2000/svg",
  viewBox: "0 0 24 24",
  fill: "none",
  stroke: "currentColor",
  "stroke-linecap": "round",
  "stroke-linejoin": "round",
  "aria-hidden": "true",
};

function CopyIcon() {
  return jsxs("svg", {
    ...iconProps,
    children: [
      jsx("rect", { width: "14", height: "14", x: "8", y: "8", rx: "2", ry: "2" }),
      jsx("path", { d: "M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2" }),
    ],
  });
}

function DownloadIcon() {
  return jsxs("svg", {
    ...iconProps,
    children: [
      jsx("path", { d: "M12 3v12" }),
      jsx("path", { d: "m7 10 5 5 5-5" }),
      jsx("path", { d: "M5 21h14" }),
    ],
  });
}

function FileTextIcon() {
  return jsxs("svg", {
    ...iconProps,
    children: [
      jsx("path", { d: "M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" }),
      jsx("path", { d: "M14 2v6h6" }),
      jsx("path", { d: "M16 13H8" }),
      jsx("path", { d: "M16 17H8" }),
      jsx("path", { d: "M10 9H8" }),
    ],
  });
}

export const PageActions = () => {
  const PageActionsComponent = ({ displayClass }) =>
    jsxs("div", {
      class: `page-actions ${displayClass ?? ""}`,
      "aria-label": "Page actions",
      children: [
        jsx("button", {
          type: "button",
          "data-action": "copy",
          "aria-label": "Copy to clipboard",
          title: "Copy to clipboard",
          children: jsx(CopyIcon, {}),
        }),
        jsx("button", {
          type: "button",
          "data-action": "markdown",
          "aria-label": "Download Markdown",
          title: "Download Markdown",
          children: jsx(DownloadIcon, {}),
        }),
        jsx("button", {
          type: "button",
          "data-action": "pdf",
          "aria-label": "Download PDF",
          title: "Download PDF",
          children: jsx(FileTextIcon, {}),
        }),
      ],
    });

  PageActionsComponent.css = style;
  PageActionsComponent.afterDOMLoaded = script;
  return PageActionsComponent;
};
