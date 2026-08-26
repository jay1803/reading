export function getDomain(url: string): string | null {
  try {
    return new URL(url).hostname.replace(/^www\./, '');
  } catch {
    return null;
  }
}

// Domains whose source URL points at a private mailbox/newsletter render
// rather than a publishable article — the outbound link would leak personal
// inbox content, so we suppress the "Source ↗" link for these.
const PRIVATE_SOURCE_DOMAINS = new Set(['newsletters.feedbinusercontent.com']);

export function isPrivateSourceDomain(domain: string | null): boolean {
  return !!domain && PRIVATE_SOURCE_DOMAINS.has(domain);
}
