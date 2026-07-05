import { jsx, jsxs } from "preact/jsx-runtime";
import { readFileSync } from "fs";
import { join } from "path";

function getQuartzVersion() {
  try {
    const pkg = JSON.parse(readFileSync(join(process.cwd(), "package.json"), "utf-8"));
    return pkg.version ?? "";
  } catch {
    return "";
  }
}

const style = `
footer.custom-footer {
  text-align: left;
  margin-bottom: 1.5rem;
  opacity: 0.7;
}

footer.custom-footer hr {
  margin: 0.75rem 0;
  border: none;
  border-top: 1px solid var(--lightgray);
}

footer.custom-footer .license {
  font-size: 0.85rem;
  margin: 0.5rem 0;
}

footer.custom-footer ul {
  list-style: none;
  margin: 0.5rem 0 0 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  gap: 1rem;
}
`;

export const Footer = (opts) => {
  const version = getQuartzVersion();
  const links = opts?.links ?? {};
  const licenseText = opts?.licenseText ?? "";
  const licenseUrl = opts?.licenseUrl;

  const FooterComponent = ({ displayClass }) => {
    return jsxs("footer", {
      class: `custom-footer ${displayClass ?? ""}`,
      children: [
        jsxs("p", {
          children: [
            "Created with ",
            jsx("a", {
              href: "https://quartz.jzhao.xyz/",
              children: `Quartz${version ? ` v${version}` : ""}`,
            }),
          ],
        }),
        jsx("hr", {}),
        jsx("p", {
          class: "license",
          children: licenseUrl
            ? jsx("a", { href: licenseUrl, children: licenseText })
            : licenseText,
        }),
        jsx("ul", {
          children: Object.entries(links).map(([text, link]) =>
            jsx("li", { children: jsx("a", { href: link, children: text }) }),
          ),
        }),
      ],
    });
  };

  FooterComponent.css = style;
  return FooterComponent;
};
