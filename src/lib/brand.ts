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
