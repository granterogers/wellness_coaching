// The one place logo files are referenced (requirement 7.4). A refined logo is a file swap in assets/brand/.
import iconRaw from '../../assets/brand/icon.svg?raw';
import logoUrl from '../../assets/brand/logo-currentcolor.svg?url';

/** Header icon, inline so it takes the text colour. The file's own colour rules are removed so they can't leak into the page. */
export const iconSvg = iconRaw
  .replace(/<style>[\s\S]*?<\/style>/, '')
  .replace('<svg ', '<svg class="icon" aria-hidden="true" focusable="false" ')
  .replace(/\s(role|aria-label)="[^"]*"/g, '');

/** Full figurative logo: footer and About page only, never under 64px (requirement 7.3). */
export const fullLogoUrl = logoUrl;

/** Language flags for the header switcher (requirement 12.2). Simple, decorative; the link carries the language name. */
export const flagUK = `<svg class="flag" viewBox="0 0 60 40" aria-hidden="true" focusable="false"><clipPath id="fuk"><rect width="60" height="40" rx="4"/></clipPath><g clip-path="url(#fuk)"><rect width="60" height="40" fill="#012169"/><path d="M0 0L60 40M60 0L0 40" stroke="#fff" stroke-width="8"/><path d="M0 0L60 40M60 0L0 40" stroke="#C8102E" stroke-width="3"/><path d="M30 0V40M0 20H60" stroke="#fff" stroke-width="12"/><path d="M30 0V40M0 20H60" stroke="#C8102E" stroke-width="7"/></g></svg>`;
export const flagES = `<svg class="flag" viewBox="0 0 60 40" aria-hidden="true" focusable="false"><clipPath id="fes"><rect width="60" height="40" rx="4"/></clipPath><g clip-path="url(#fes)"><rect width="60" height="40" fill="#AA151B"/><rect y="10" width="60" height="20" fill="#F1BF00"/></g></svg>`;
